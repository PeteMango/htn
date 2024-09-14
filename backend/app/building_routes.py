from flask import Flask, jsonify, request
from app import app, supabase
from geopy import distance

@app.route('/building_toilets', methods=['GET'])
def get_toilets():
    """Returns toilets in the specified building`
        
    Args:
        bid (int): the building id

    Returns:
        json: array of toilet information
    """

    bid = request.args.get("bid")

    try:
        if bid is None:
            return jsonify({"error": f"Bad request, did not provide bid"}), 400
        
        response = supabase.from_('BuildingToilet').select('Toilet(tid, info, gender)').eq("bid", bid)

        if response.data:
            return jsonify(response.data), 200

        return jsonify({"message": "No data found"}), 404
     
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500

@app.route('/add_building')
def add_building():
    """adds a buildings to the data base`
    
    Args:
        lat (float): latitude of the building
        long (float): longtitude of the building
        bid (int): building id
        bname (str): building name
        address (str): address of the building

    Returns:
        json: added building
    """ 
    data = request.json

    bid = data["bid"]
    lat, lng = data["lat"], data["long"]

    if lat < 0 or lng < 0 or lat > 180 or lng > 180:
        return jsonify({"Error": "Latitude and longtitude have to be between 0 and 180 degrees"})
    
    

@app.route('/near_buildings')
def get_nearbuildings():
    """Returns nearby buildings`
        - needs user's lat and long 
        - needs threshold 

    Returns:
        json: array of buildings
    """

    lat = request.args.get("lat")
    lon = request.args.get("lon")
    threshold_distance = request.args.get("threshold")

    try:
        if lat is None or lon is None:
            return jsonify({"error": f"Bad request, did not provide position (lon and lat)"}), 400
        
        if threshold_distance is None:
            threshold_distance = 0.5 # by default use 500m as threshold

        response = supabase.table("Building").select("*").execute()

        if not response.data:
            return jsonify({"message": "No data found"}), 404
        
        nearBuildings = []

        user_coord = (lat, lon)

        for row in response.data:
            building_coord = (row["lat"], row["lon"])
            if distance.distance(user_coord, building_coord).km <= threshold_distance:
                nearBuildings.insert(row)
        
        return jsonify(nearBuildings), 200
     
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500
