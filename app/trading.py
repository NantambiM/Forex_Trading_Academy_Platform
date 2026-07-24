from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
import random
from datetime import datetime

from .models import TradingAccount, Trade, CurrencyPair
from . import db

trading = Blueprint("trading", __name__)

DEFAULT_PAIRS = [
    {"symbol": "EUR/USD", "buy_price": 1.0850, "sell_price": 1.0848},
    {"symbol": "GBP/USD", "buy_price": 1.2720, "sell_price": 1.2717},
    {"symbol": "USD/JPY", "buy_price": 155.40, "sell_price": 155.37},
    {"symbol": "AUD/USD", "buy_price": 0.6650, "sell_price": 0.6647},
    {"symbol": "USD/CAD", "buy_price": 1.3680, "sell_price": 1.3677},
    {"symbol": "XAU/USD", "buy_price": 2350.50, "sell_price": 2349.80},
]


def seed_currency_pairs():
    """Ensure default currency pairs exist in DB."""
    if CurrencyPair.query.count() == 0:
        for p in DEFAULT_PAIRS:
            pair = CurrencyPair(
                symbol=p["symbol"],
                buy_price=p["buy_price"],
                sell_price=p["sell_price"]
            )
            db.session.add(pair)
        db.session.commit()


@trading.route("/trading/dashboard")
@login_required
def trading_dashboard():
    seed_currency_pairs()

    account = TradingAccount.query.filter_by(
        user_id=current_user.id
    ).first()

    # Create account if user doesn't have one yet
    if account is None:
        account = TradingAccount(
            user_id=current_user.id,
            balance=10000.00,
            equity=10000.00
        )
        db.session.add(account)
        db.session.commit()

    open_trades = Trade.query.filter_by(
        user_id=current_user.id,
        status="OPEN"
    ).all()

    closed_trades = Trade.query.filter_by(
        user_id=current_user.id,
        status="CLOSED"
    ).order_by(Trade.closed_at.desc()).limit(20).all()

    pairs = CurrencyPair.query.all()

    # Calculate live simulated P&L for open trades
    total_floating_pnl = 0.0
    pair_price_map = {p.symbol: p for p in pairs}

    for trade in open_trades:
        pair_obj = pair_price_map.get(trade.pair)
        if pair_obj:
            curr_price = pair_obj.sell_price if trade.trade_type == "BUY" else pair_obj.buy_price
            price_diff = curr_price - trade.open_price if trade.trade_type == "BUY" else trade.open_price - curr_price
            
            # Standard lot size multiplier (100,000 units per standard lot)
            multiplier = 100000 if "XAU" not in trade.pair else 100
            floating_pnl = round(price_diff * trade.lot_size * multiplier, 2)
            trade.current_pnl = floating_pnl
            trade.current_price = curr_price
            total_floating_pnl += floating_pnl
        else:
            trade.current_pnl = 0.0
            trade.current_price = trade.open_price

    total_floating_pnl = round(total_floating_pnl, 2)
    account_equity = round(account.balance + total_floating_pnl, 2)
    account.equity = account_equity
    db.session.commit()

    margin_used = sum([t.lot_size * 1000 for t in open_trades])
    free_margin = round(account_equity - margin_used, 2)

    return render_template(
        "trading_dashboard.html",
        account=account,
        equity=account_equity,
        floating_pnl=total_floating_pnl,
        margin_used=margin_used,
        free_margin=free_margin,
        open_trades=open_trades,
        closed_trades=closed_trades,
        pairs=pairs
    )


@trading.route("/trading/place_order", methods=["POST"])
@login_required
def place_order():
    pair_symbol = request.form.get("pair")
    trade_type = request.form.get("trade_type", "BUY").upper()
    try:
        lot_size = float(request.form.get("lot_size", 0.1))
    except (ValueError, TypeError):
        lot_size = 0.1

    pair = CurrencyPair.query.filter_by(symbol=pair_symbol).first()
    if not pair:
        flash("Invalid currency pair selected.", "danger")
        return redirect(url_for("trading.trading_dashboard"))

    account = TradingAccount.query.filter_by(user_id=current_user.id).first()
    if not account:
        flash("Trading account not found.", "danger")
        return redirect(url_for("trading.trading_dashboard"))

    open_price = pair.buy_price if trade_type == "BUY" else pair.sell_price

    new_trade = Trade(
        user_id=current_user.id,
        pair=pair.symbol,
        trade_type=trade_type,
        lot_size=lot_size,
        open_price=open_price,
        status="OPEN",
        opened_at=datetime.utcnow()
    )

    db.session.add(new_trade)
    db.session.commit()

    flash(f"Order executed: {trade_type} {lot_size} lot(s) of {pair.symbol} @ {open_price}", "success")
    return redirect(url_for("trading.trading_dashboard"))


@trading.route("/trading/close_trade/<int:trade_id>", methods=["POST"])
@login_required
def close_trade(trade_id):
    trade = Trade.query.filter_by(id=trade_id, user_id=current_user.id, status="OPEN").first()
    if not trade:
        flash("Trade position not found or already closed.", "warning")
        return redirect(url_for("trading.trading_dashboard"))

    pair = CurrencyPair.query.filter_by(symbol=trade.pair).first()
    close_price = pair.sell_price if trade.trade_type == "BUY" else pair.buy_price if pair else trade.open_price
    
    price_diff = close_price - trade.open_price if trade.trade_type == "BUY" else trade.open_price - close_price
    multiplier = 100000 if "XAU" not in trade.pair else 100
    pnl = round(price_diff * trade.lot_size * multiplier, 2)

    trade.close_price = close_price
    trade.profit_loss = pnl
    trade.status = "CLOSED"
    trade.closed_at = datetime.utcnow()

    account = TradingAccount.query.filter_by(user_id=current_user.id).first()
    if account:
        account.balance = round(account.balance + pnl, 2)
        account.equity = round(account.balance, 2)

    db.session.commit()

    flash_type = "success" if pnl >= 0 else "danger"
    flash(f"Closed {trade.pair} position with P&L: ${pnl:+.2f}", flash_type)
    return redirect(url_for("trading.trading_dashboard"))


@trading.route("/api/market_data")
@login_required
def market_data():
    """Simulated market data feed with minor random fluctuations for chart & ticker updates."""
    pairs = CurrencyPair.query.all()
    results = []
    
    for p in pairs:
        # Slight random tick shift (-0.0005 to +0.0005)
        delta = round(random.uniform(-0.0008, 0.0008), 4)
        if "JPY" in p.symbol or "XAU" in p.symbol:
            delta = round(random.uniform(-0.15, 0.15), 2)
            
        p.buy_price = round(max(0.0001, p.buy_price + delta), 4)
        p.sell_price = round(max(0.0001, p.sell_price + delta), 4)
        db.session.commit()

        change_pct = round(random.uniform(-0.85, 1.25), 2)
        results.append({
            "symbol": p.symbol,
            "buy_price": p.buy_price,
            "sell_price": p.sell_price,
            "change_pct": change_pct
        })

    return jsonify({"pairs": results})