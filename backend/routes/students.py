from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import db, Quiz, Question, Submission

student_bp = Blueprint('student', __name__)

@student_bp.route('/quizzes', methods=['GET'])
@jwt_required()
def list_quizzes():
    quizzes = Quiz.query.all()
    return jsonify([
        {'id': q.id, 'title': q.title} for q in quizzes
    ])

@student_bp.route('/quiz/<int:quiz_id>', methods=['GET'])
@jwt_required()
def get_quiz(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    return jsonify([
        {'id': q.id, 'question': q.question_text, 'options': q.options} for q in questions
    ])

@student_bp.route('/submit/<int:quiz_id>', methods=['POST'])
@jwt_required()
def submit_quiz(quiz_id):
    identity = get_jwt_identity()
    answers = request.json['answers']
    score = 0

    for qid, ans in answers.items():
        question = Question.query.get(qid)
        if question and question.correct_answer == ans:
            score += 1

    submission = Submission(user_id=identity['id'], quiz_id=quiz_id, score=score)
    db.session.add(submission)
    db.session.commit()

    return jsonify(score=score)