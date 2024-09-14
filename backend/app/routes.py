from flask import Flask, jsonify, request
from app import app, supabase

@app.route('/')
def home():
    """Entrypoint into flask app

    Returns:
        json: welcome message
    """
    return jsonify({"message": "Welcome to the Flask app with Supabase!"})


@app.route('/insert_toilet', methods=['POST'])
def insert_toilet():
    """Insert a toilet into the toilets table

    Returns:
        json: information inserted into the database or error message
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    required_fields = ["tid", "lat", "long", "info", "gender"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        response = supabase.table("Toilet").insert({
            "tid": data["tid"],
            "lat": data["lat"],
            "long": data["long"],
            "info": data["info"],
            "gender": data["gender"]
        }).execute()
        return jsonify(response.data), 201  # Return 201 Created for successful insertion
    except Exception as e:
        return jsonify({"error": f"Failed to insert data: {str(e)}"}), 500


@app.route('/insert_user', methods=['POST'])
def insert_user():
    """Insert a user into the user table

    Returns:
        json: information inserted into the database or error message
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    required_fields = ["uid", "email", "gender"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        response = supabase.table("User").insert({
            "uid": data["uid"],
            "email": data["email"],
            "gender": data["gender"]
        }).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": f"Failed to insert data: {str(e)}"}), 500


@app.route('/insert_tag', methods=['POST'])
def insert_tag():
    """Insert a tag into the tag table

    Returns:
        json: information inserted into the database or error message
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    if "tag_name" not in data:
        return jsonify({"error": "Tag name is required"}), 400

    try:
        response = supabase.table("Tag").insert({
            "tag_name": data["tag_name"]
        }).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": f"Failed to insert data: {str(e)}"}), 500


@app.route('/toilets', methods=['GET'])
def get_toilets():
    """Returns all the toilets & their location or a specific toilet by `tid`

    Returns:
        json: toilet information
    """
    tid = request.args.get("tid")

    try:
        if tid is None:
            response = supabase.table("Toilet").select("*").execute()
        else:
            response = supabase.table("Toilet").select("*").eq("tid", tid).execute()

        if response.data:
            return jsonify(response.data), 200
        return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500


@app.route('/users', methods=['GET'])
def get_users():
    """Returns all users or a specific user by `uid`

    Returns:
        json: user information
    """
    uid = request.args.get("uid")

    try:
        if uid is None:
            response = supabase.table("User").select("*").execute()
        else:
            response = supabase.table("User").select("*").eq("uid", uid).execute()

        if response.data:
            return jsonify(response.data), 200
        return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve data: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
