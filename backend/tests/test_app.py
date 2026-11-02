def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    assert data['data']['status'] == 'ok'

def test_404_error_handler(client):
    response = client.get('/non-existent-route')
    assert response.status_code == 404
    data = response.get_json()
    assert data['success'] is False
    assert 'Resource not found' in data['message']

def test_bcrypt_integration(app):
    from app import bcrypt
    password = "securepassword123"
    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    assert bcrypt.check_password_hash(hashed, password) is True
    assert bcrypt.check_password_hash(hashed, "wrongpassword") is False
