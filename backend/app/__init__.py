import os
import logging
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_class=None):
    app = Flask(__name__)

    # Configuration
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            'DATABASE_URL',
            'postgresql://postgres:postgres@localhost:5432/app_db'
        )
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
            'pool_size': 10,
            'pool_recycle': 3600,
            'pool_pre_ping': True
        }

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Logging setup
    logging.basicConfig(level=logging.INFO)
    app.logger.info('Flask application starting up...')

    # Centralized Error Handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": "Bad request",
            "error": str(error),
            "data": None
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": str(error),
            "data": None
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        app.logger.error(f"Server Error: {error}")
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": "An unexpected error occurred.",
            "data": None
        }), 500

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        db.session.rollback()
        app.logger.error(f"Unhandled Exception: {error}")
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": str(error) if app.debug else "An unexpected error occurred.",
            "data": None
        }), 500

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({
            "success": True,
            "message": "Application is healthy",
            "data": {"status": "ok"}
        }), 200

    return app
