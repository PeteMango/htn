import random

def test_insert_and_get_toilet(client):
    """Test inserting a toilet and then retrieving it."""
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

    # Insert a new toilet
    insert_response = client.post('/insert_toilet', json=toilet_data)
    assert insert_response.status_code == 201
    insert_json = insert_response.get_json()

    # Retrieve the toilet by tid
    get_response = client.get(f'/toilets?tid={tid}')  # Correct format for tid in the URL
    assert get_response.status_code == 200
    get_json = get_response.get_json()
    
    # Compare the values with precision for lat and long
    assert get_json[0]['tid'] == tid
    assert round(get_json[0]['lat'], 6) == lat
    assert round(get_json[0]['long'], 6) == long
    assert get_json[0]['info'] == info
    assert get_json[0]['gender'] == gender
