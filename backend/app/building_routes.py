from flask import Flask, jsonify, request
from app import app, supabase
from geopy import distance
from geopy.geocoders import Nominatim

@app.route('/building_toilets', methods=['GET'])
def get_toilets():
    """Returns toilets in the specified building`
        
    Args:
        bid (int): the building id

    Returns:
        json: All the toilets in a building
    """

    data = request.json
    bid = data["bid"]
    print(bid)

    try:
        if bid is None:
            return jsonify({"Error": "Bad request, did not provide bid"}), 400

        response = supabase.from_('BuildingToilet').select(
            'Toilets(tid, info, gender)').eq("bid", bid).execute()

        if response.data:
            return jsonify(response.data), 200

        return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500

@app.route('/add_building', methods=['POST'])
def add_building():
    """Adds a building to the database
    
    Args:
        lat (float): latitude of the building
        long (float): longtitude of the building
        bid (str): building id  
        bname (str): building name

    Returns:
        json: added building
    """
    data = request.json

    bid = data["bid"]
    lat, lng = data["lat"], data["lng"]

    if abs(lat) > 180 or abs(lng) > 180:
        return jsonify({
            "Error":
            "Latitude and longtitude have to be between 0 and 180 degrees"
        })

    geolocator = Nominatim(user_agent="my_geocoding_application")
    location = geolocator.reverse((lat, lng), exactly_one=True)

    adress = location.address if location else "Address not found"

    response = supabase.table("Buildings").upsert({
        "bid": bid,
        "bname": data["bname"],
        "lat": lat,
        "lng": lng,
        "address": adress
    }).execute()

    return jsonify(response.data), 201


@app.route('/near_buildings')
def get_nearbuildings():
    """Returns nearby buildings

    Args:
        lat (float): user's latitude
        lng (float): user's longtitude
        threshold (float): kilometer distance from user

    Returns:
        json: array of buildings
    """
    data = request.json
    lat, lng, threshold_distance = data["lat"], data["lng"], data["threshold"]

    try:
        if lat is None or lng is None:
            return jsonify({
                "error":
                "Bad request, did not provide position (lon and lat)"
            }), 400

        if threshold_distance is None:
            threshold_distance = 0.5  # by default use 500m as threshold

        response = supabase.table("Buildings").select("*").execute()

        if not response.data:
            return jsonify({"message": "No data found"}), 404

        near_buildings = []

        user_coord = (lat, lng)

        for row in response.data:
            building_coord = (row["lat"], row["lon"])
            if distance.distance(user_coord,
                                 building_coord).km <= threshold_distance:
                near_buildings.insert(row)

        return jsonify(near_buildings), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500
