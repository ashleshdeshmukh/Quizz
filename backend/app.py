from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.models import db
from routes.auth import auth_bp
from routes.quizzes import quiz_bp
from routes.students import student_bp
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__, static_folder='../frontend')
CORS(app)

@app.route('/frontend/<path:path>')
def serve_frontend(path):
    return send_from_directory(app.static_folder, path)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # folder where app.py is
db_path = os.path.join(BASE_DIR, "database.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///backend/database.db'
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(quiz_bp, url_prefix='/quiz')
app.register_blueprint(student_bp, url_prefix='/student')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8000)