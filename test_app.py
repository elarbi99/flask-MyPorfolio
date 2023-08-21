import pytest
from app import app
from flask import url_for

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b"Testimonial" in response.data

def test_contact_form_submission(client):
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '1234567890',
        'comment': 'This is a test comment'
    }
    response = client.post('/contact', data=data, follow_redirects=True)
    assert b"Submission Successful" in response.data

def test_testimonial_form_submission(client):
    data = {
        'name': 'John Smith',
        'comment': 'This is a test testimonial'
    }
    response = client.post('/testimonial', data=data, follow_redirects=True)
    assert b"Submission Successful" in response.data

if __name__ == '__main__':
    pytest.main()