import os
from flask import Flask, jsonify
from app.extensions import db, migrate, jwt, bcrypt

def create_app(config_name=None):
    app = Flask(__name__)

    # Configuration
    database_url = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/app_db")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-jwt-key-change-in-production")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "success": True,
            "message": "Backend service is running and connected to database.",
            "data": {}
        }), 200

    return app
