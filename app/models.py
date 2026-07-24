from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>" 

class Lesson(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    lesson_name=db.Column(db.String(100),unique=True)
    content=db.Column(db.Text,nullable=False)
    video_url=db.Column(db.String(255),nullable=True)
    quiz=db.relationship('Quiz', backref='lesson', lazy=True)

class Quiz(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    quiz_topic=db.Column(db.String(200),unique=True)
    lesson_id=db.Column(db.Integer,db.ForeignKey('lesson.id'),nullable=False)
    questions=db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question_text=db.Column(db.Text,nullable=False)
    quiz_id=db.Column(db.Integer,db.ForeignKey('quiz.id'),nullable=False)
    option1=db.Column(db.String(255),nullable=False)
    option2=db.Column(db.String(255),nullable=False)
    option3=db.Column(db.String(255),nullable=True)
    option4=db.Column(db.String(255),nullable=True)
    correct_option=db.Column(db.String(255),nullable=False)
    