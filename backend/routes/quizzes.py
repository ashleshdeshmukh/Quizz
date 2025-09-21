from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.models import db, Quiz, Question, QuizResult, User

quiz_bp = Blueprint('quiz', __name__)

# Admin: Create a quiz
@quiz_bp.route('/create', methods=['POST'])
#@jwt_required()
def create_quiz():
    identity = get_jwt_identity()
    if not identity['is_admin']:
        return jsonify(message="Admins Only"), 403

    data = request.json
    new_quiz = Quiz(title=data['title'])
    db.session.add(new_quiz)
    db.session.flush()

    for q in data['questions']:
        question = Question(
            quiz_id=new_quiz.id,
            question_text=q['question'],
            options=q['options'],
            correct_answer=q['answer']
        )
        db.session.add(question)

    db.session.commit()
    return jsonify(message='Quiz created')

# List all quizzes
@quiz_bp.route('/all', methods=['GET'])
#@jwt_required()
def get_all_quizzes():
    quizzes = Quiz.query.all()
    quiz_list = [{'id': q.id, 'title': q.title} for q in quizzes]
    return jsonify(quiz_list)

# Get questions for a selected quiz by title
@quiz_bp.route('/by-title', methods=['POST'])
#@jwt_required()
def get_quiz_by_title():
    data = request.json
    title = data.get('title')
    if not title:
        return jsonify(message="Quiz title is required"), 400

    quiz = Quiz.query.filter_by(title=title).first()
    if not quiz:
        return jsonify(message="Quiz not found"), 404

    questions = Question.query.filter_by(quiz_id=quiz.id).all()
    questions_list = []
    for q in questions:
        questions_list.append({
            'id': q.id,
            'question': q.question_text,
            'options': q.options,
            'correct_answer': q.correct_answer
        })

    return jsonify({
        'quiz_id': quiz.id,
        'title': quiz.title,
        'questions': questions_list
    })


# backend/routes/quizzes.py
@quiz_bp.route('/submit-score', methods=['POST'])
#@jwt_required()
def submit_score():
    try:
       # identity = get_jwt_identity()
       # if not identity or 'id' not in identity:
       #     return jsonify(message="Invalid user"), 401
       # user_id = identity['id']

        #data = request.json
        #user_id = 1

        data = request.get_json(force=True)
        print("Incoming JSON:", data)

        user_id=data.get('user_IDD')
        quiz_id = data.get('quiz_id')
        score = data.get('score')
        total_questions = data.get('total_questions')

        if quiz_id is None or score is None or total_questions is None:
            return jsonify(message="Incomplete data"), 400

        # Check if user already has a score for this quiz
        existing = QuizResult.query.filter_by(user_id=user_id, quiz_id=quiz_id).first()
        if existing:
            # Update the score if needed
            existing.score = score
            existing.total_questions = total_questions
        else:
            # Create new entry
            result = QuizResult(
                user_id=user_id,
                quiz_id=quiz_id,
                score=score,
                total_questions=total_questions
            )
            db.session.add(result)

        db.session.commit()
        return jsonify(message="Score submitted successfully"), 200

    except Exception as e:
        db.session.rollback()
        print("Error in submit-score:", e)
        return jsonify(message="Could not submit score"), 500


@quiz_bp.route('/leaderboard/<int:quiz_id>', methods=['GET'])
def leaderboard(quiz_id):
    # Ensure quiz_id is int
    #try:
     #   quiz_id = int(quiz_id)
    #except:
     #   return jsonify(message="Invalid quiz ID"), 400

    # Fetch top 10 results for this quiz
    results = QuizResult.query.filter_by(quiz_id=quiz_id) \
        .order_by(QuizResult.score.desc()) \
        .limit(10) \
        .all()

    leaderboard_data = []

    if not results:
        return jsonify(message="No scores yet", leaderboard=[])

    for r in results:
        user = User.query.get(r.user_id)
        if user:  # just in case
            leaderboard_data.append({
                'username': user.username,
                'score': r.score,
                'total': r.total_questions
            })

    return jsonify(leaderboard=leaderboard_data)
