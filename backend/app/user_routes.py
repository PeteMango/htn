from flask import Flask, jsonify, request
from app import app, supabase

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