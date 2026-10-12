import pytest
from sqlalchemy.exc import IntegrityError
from app import create_app, db
from app.models.user import User, Role, Permission

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_user_creation(app):
    with app.app_context():
        user = User(username='testuser', email='test@example.com', password_hash='hash')
        db.session.add(user)
        db.session.commit()
        
        retrieved = User.query.filter_by(username='testuser').first()
        assert retrieved is not None
        assert retrieved.email == 'test@example.com'

def test_unique_constraints(app):
    with app.app_context():
        user1 = User(username='user1', email='dup@example.com', password_hash='hash')
        db.session.add(user1)
        db.session.commit()
        
        user2 = User(username='user2', email='dup@example.com', password_hash='hash')
        db.session.add(user2)
        with pytest.raises(IntegrityError):
            db.session.commit()
        db.session.rollback()

def test_rbac_relationships(app):
    with app.app_context():
        user = User(username='admin', email='admin@example.com', password_hash='hash')
        role = Role(name='Administrator', description='Admin role')
        permission = Permission(name='read:users', description='Can read users')
        
        role.permissions.append(permission)
        user.roles.append(role)
        
        db.session.add_all([user, role, permission])
        db.session.commit()
        
        saved_user = User.query.filter_by(username='admin').first()
        assert len(saved_user.roles) == 1
        assert saved_user.roles[0].name == 'Administrator'
        assert len(saved_user.roles[0].permissions) == 1
        assert saved_user.roles[0].permissions[0].name == 'read:users'
