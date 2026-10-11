import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_name=None):
    app = Flask(__name__)
    
    database_url = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgrespassword@localhost:5432/app_db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'fallback-secret-key')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({
            "success": True,
            "message": "Service is healthy",
            "data": {"status": "UP"}
        }), 200

    return app
