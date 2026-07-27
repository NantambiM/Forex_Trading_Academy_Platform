from flask import Blueprint, render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, timedelta

from .forms import RegisterForm, LoginForm, UpdateProfileForm, ChangePasswordForm
from .models import  Question, Quiz, Lesson
from .models import User, TradingAccount, Trade
from . import db

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("Email already exists!", "danger")
            return redirect(url_for("main.register"))

        hashed_password = generate_password_hash(form.password.data)

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()
        
        account = TradingAccount(
            user_id=user.id,
            balance=10000.00,
            equity=10000.00
        )
        db.session.add(account)
        db.session.commit()

        flash("Registration successful! Please login.", "success")

        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)

            flash("Login successful!", "success")

            return redirect(url_for("main.dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@main.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    profile_form = UpdateProfileForm()
    password_form = ChangePasswordForm()

    if request.method == "GET":
        profile_form.username.data = current_user.username
        profile_form.email.data = current_user.email

    form_type = request.form.get("form_type")

    if request.method == "POST" and form_type == "profile":
        if profile_form.validate_on_submit():
            existing_email = User.query.filter(User.email == profile_form.email.data, User.id != current_user.id).first()
            existing_username = User.query.filter(User.username == profile_form.username.data, User.id != current_user.id).first()

            if existing_email:
                flash("That email is already registered to another account.", "danger")
            elif existing_username:
                flash("That username is already taken.", "danger")
            else:
                current_user.username = profile_form.username.data
                current_user.email = profile_form.email.data
                db.session.commit()
                flash("Profile details updated successfully!", "success")
                return redirect(url_for("main.profile"))

    elif request.method == "POST" and form_type == "password":
        if password_form.validate_on_submit():
            if not check_password_hash(current_user.password, password_form.current_password.data):
                flash("Incorrect current password.", "danger")
            else:
                current_user.password = generate_password_hash(password_form.new_password.data)
                db.session.commit()
                flash("Password updated successfully!", "success")
                return redirect(url_for("main.profile"))

    account = TradingAccount.query.filter_by(user_id=current_user.id).first()
    all_trades = Trade.query.filter_by(user_id=current_user.id).all()
    closed_trades = [t for t in all_trades if t.status == "CLOSED"]
    winning_trades = [t for t in closed_trades if (t.profit_loss or 0) >= 0]
    total_pnl = sum(t.profit_loss or 0 for t in closed_trades)
    win_rate = (len(winning_trades) / len(closed_trades) * 100) if closed_trades else 0.0

    stats = {
        "balance": account.balance if account else 10000.00,
        "equity": account.equity if account else 10000.00,
        "total_trades": len(all_trades),
        "closed_trades": len(closed_trades),
        "open_trades": len(all_trades) - len(closed_trades),
        "win_rate": win_rate,
        "total_pnl": total_pnl
    }

    return render_template(
        "profile.html",
        profile_form=profile_form,
        password_form=password_form,
        account=account,
        stats=stats
    )


@main.route("/logout")
@login_required
def logout():
    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(url_for("main.login")) 

@main.route("/lesson/<int:id>")
def lesson(id):
    lesson = Lesson.query.get(id)
    if not lesson:
        flash("Lesson not found.", "danger")
        return redirect(url_for("main.dashboard"))
    return render_template("lesson.html", lesson=lesson)

@main.route("/quiz/<int:id>", methods=["GET", "POST"])
def quiz(id):
    quiz = Quiz.query.get(id)
    questions = Question.query.filter_by(quiz_id=id).all()
    if not quiz:
        flash("Quiz not found.", "danger")
        return redirect(url_for("main.dashboard"))
    score = None
    if request.method == "POST":
        score=0
        for question in questions:
            selected_option = request.form.get(f"question_{question.id}")
            if selected_option == question.correct_option:
                score += 1


    return render_template("quiz.html", quiz=quiz,questions=questions,score=score)


@main.route("/analytics")
@login_required
def analytics():
    range_param = request.args.get("range", "30d")

    since = None
    if range_param == "7d":
        since = datetime.utcnow() - timedelta(days=7)
    elif range_param == "30d":
        since = datetime.utcnow() - timedelta(days=30)
    # "all" -> since stays None

    account = TradingAccount.query.filter_by(user_id=current_user.id).first()

    trade_query = Trade.query.filter_by(user_id=current_user.id, status="CLOSED")
    if since:
        trade_query = trade_query.filter(Trade.closed_at >= since)
    trades = trade_query.order_by(Trade.closed_at.asc()).all()

    wins = [t for t in trades if (t.profit_loss or 0) >= 0]
    losses = [t for t in trades if (t.profit_loss or 0) < 0]
    total_pnl = sum(t.profit_loss or 0 for t in trades)
    avg_win = (sum(t.profit_loss for t in wins) / len(wins)) if wins else 0
    avg_loss = (abs(sum(t.profit_loss for t in losses)) / len(losses)) if losses else 0
    gross_loss = abs(sum(t.profit_loss for t in losses))
    profit_factor = (sum(t.profit_loss for t in wins) / gross_loss) if gross_loss else 0.0

    # Equity curve always starts with a real "Start" point, then one point
    # per closed trade. This guarantees at least 2 points so the line chart
    # always has something to draw, even for a brand-new account.
    starting_balance = round((account.balance if account else 10000.00) - total_pnl, 2)
    running = starting_balance
    equity_curve = [{"date": "Start", "value": starting_balance}]
    for t in trades:
        running += (t.profit_loss or 0)
        equity_curve.append({
            "date": t.closed_at.strftime("%b %d") if t.closed_at else "",
            "value": round(running, 2),
        })

    trading = {
        "equity": account.equity if account else 10000.00,
        "initial_capital": 10000.00,
        "total_pnl": total_pnl,
        "total_trades": len(trades),
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": (len(wins) / len(trades) * 100) if trades else 0,
        "profit_factor": profit_factor,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "equity_curve": equity_curve,
        "recent_trades": [
            {
                "date": t.closed_at.strftime("%Y-%m-%d") if t.closed_at else "-",
                "pair": t.pair,
                "type": t.trade_type,
                "entry": t.open_price,
                "exit": t.close_price,
                "volume": t.lot_size,
                "pnl": t.profit_loss or 0,
            }
            for t in reversed(trades[-10:])
        ],
    }

    # Learning: only counts of what exists — no per-user progress yet since
    # quiz attempts aren't saved anywhere in the current schema. The template
    # shows this as real numbers plus a "Coming Soon" panel for the rest.
    learning = {
        "total_lessons": Lesson.query.count(),
        "total_quizzes": Quiz.query.count(),
    }

    return render_template(
        "analytics.html",
        trading=trading,
        learning=learning,
        range=range_param,
    )