from flask import Flask, jsonify, request
from app import app, supabase

@app.route('/insert_toilet', methods=['POST'])
def insert_toilet():
    """Insert a toilet into the toilets table

    Returns:
        json: information inserted into the database or error message
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    required_fields = ["bid", "tid", "info", "gender", "tags"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        response = supabase.table("Toilets").insert({
            "tid": data["tid"],
            "info": data["info"],
            "gender": data["gender"]
        }).execute()

        for tag in data["tags"]:
            supabase.table("ToiletTag").upsert({
                "tid": data["tid"],
                "tag_name": tag
            }).execute()


        supabase.table("BuildingToilet").upsert({
            "bid": data["bid"],
            "tid": data["tid"]
        }).execute()


        return jsonify(response.data), 201  # Return 201 Created for successful insertion
    except Exception as e:
        return jsonify({"error": f"Failed to insert data: {str(e)}"}), 500

@app.route('/toilet', methods=['GET'])
def get_toilet():
    """Gets the toilet by tid

    Returns:
        json: toilet information
    """
    tid = request.args.get("tid")

    try:
        if tid is None:
            return jsonify({"error": "Bad request, did not provide tid"}), 400

        response = supabase.from_("Toilets").select(
            "tid, info, gender,Tag(tag_name), Reviews(uid, rating, review)"
        ).eq("tid", tid).execute()

        if response.data:
            return jsonify(response.data), 200
        return jsonify({"message": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to reetrieve data: {str(e)}"}), 500

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
        response = supabase.table("Tags").insert({
            "tag_name": data["tag_name"]
        }).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": f"Failed to insert data: {str(e)}"}), 500
