from flask_login import UserMixin
from . import db
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"


class TradingAccount(db.Model):
    __tablename__ = "trading_accounts"

    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, default=10000.00)
    equity = db.Column(db.Float, default=10000.00)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        unique=True
    )

    user = db.relationship(
        "User",
        backref="trading_account"
    )


class CurrencyPair(db.Model):
    __tablename__ = "currency_pairs"

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20), unique=True, nullable=False)
    buy_price = db.Column(db.Float, nullable=False)
    sell_price = db.Column(db.Float, nullable=False)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


class Trade(db.Model):
    __tablename__ = "trades"

    id = db.Column(db.Integer, primary_key=True)

    trade_type = db.Column(db.String(10), nullable=False)

    pair = db.Column(db.String(20), nullable=False)

    lot_size = db.Column(db.Float, nullable=False)

    open_price = db.Column(db.Float, nullable=False)

    close_price = db.Column(db.Float)

    profit_loss = db.Column(db.Float, default=0)

    status = db.Column(db.String(20), default="OPEN")

    opened_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    closed_at = db.Column(db.DateTime)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    user = db.relationship(
        "User",
        backref="trades"
    )