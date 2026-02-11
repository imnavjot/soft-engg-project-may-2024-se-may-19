from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from __init__ import db  # Ensure we're using the same db instance

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    weeks = db.relationship('Week', backref='course', lazy=True)

class Week(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    lectures = db.relationship('Lecture', backref='week', lazy=True)
    questions = db.relationship('Question', backref='week', lazy=True)

class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    video_url = db.Column(db.String(100), nullable=False)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'), nullable=False)
    options = db.relationship('Option', backref='question', lazy=True)
    correct_answer = db.Column(db.String(1), nullable=True)  # Correct answer (A, B, C, or D)
    code = db.Column(db.Text, nullable=True)  # Code to run for the question
    test_cases = db.Column(db.JSON, nullable=True)  # Test cases for the question
    type = db.Column(db.String(50), nullable=False)  # Type of the question (MCQ or Coding)


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    label = db.Column(db.String(1), nullable=False)  # A, B, C, or D

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    selected_option = db.Column(db.String(1), nullable=False)  # Selected answer (A, B, C, or D)

class CourseEnrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
