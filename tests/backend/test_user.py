import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
pyenv app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_password_hashing(app):
    with app.app_context():
        user = User(username='testuser')
        user.password = 'SecurePassword123!'
        
        assert user.password_hash is not None
        assert user.password_hash != 'SecurePassword123!'
        assert user.check_password('SecurePassword123!') is True
        assert user.check_password('WrongPassword') is False

def test_user_database_operations(app):
    with app.app_context():
        user = User(username='dbuser')
        user.password = 'Password123'
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(username='dbuser').first()
        assert retrieved_user is not None
        assert retrieved_user.username == 'dbuser'
        assert retrieved_user.is_active is True
        assert retrieved_user.password_hash is not None
        assert retrieved_user.check_password('Password123') is True
