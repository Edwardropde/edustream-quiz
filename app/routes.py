#!/usr/bin/env python3

from flask import render_template, url_for, flash, redirect, request
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User, Quiz, Question, QuizResult
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from datetime import datetime


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')


@main.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.form.get(f'question-{question.id}')
            if selected_answer == question.correct_answer:
                score += 1
        time_taken = float(request.form.get('time_taken', 0))
        feedback = request.form.get('feedback', '')
        result = QuizResult(score=score, time_taken=time_taken, feedback=feedback, user_id=current_user.id, quiz_id=quiz.id)
        db.session.add(result)
        db.session.commit()
        flash('Quiz completed! Your result has been saved.', 'success')
        return redirect(url_for('main.view_results', quiz_id=quiz.id))
    return render_template('take_quiz.html', quiz=quiz, questions=questions)


@main.route('/results/<int:quiz_id>')
@login_required
def view_results(quiz_id):
    results = QuizResult.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).all()
    return render_template('results.html', results=results)
