import pytest
import random

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Welcome to the Flask app with Supabase!'

def test_insert_toilet_missing_fields(client):
    """Test inserting a toilet with missing fields."""
    response = client.post('/insert_toilet', json={})
    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['error'] == "Invalid input, JSON expected"


def test_insert_toilet_success(client):
    """Test inserting a toilet successfully."""
    tid = random.randint(100, 1000)

    # Set precision for lat and long
    lat = round(random.uniform(0, 180), 6)
    long = round(random.uniform(0, 180), 6)

    info = f'random toilet at {lat} {long}'
    gender = "male" if random.randint(0, 1) == 0 else "female"

    toilet_data = {
        "tid": tid,
        "lat": lat,
        "long": long,
        "info": info,
        "gender": gender
    }

    response = client.post('/insert_toilet', json=toilet_data)
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data is not None  # Ensure data was inserted (mock for real)

def test_get_toilets(client):
    """Test retrieving all toilets."""
    response = client.get('/toilets')
    assert response.status_code == 200 or response.status_code == 404
    json_data = response.get_json()
    if response.status_code == 200:
        assert isinstance(json_data, list)  # Should return a list of toilets
