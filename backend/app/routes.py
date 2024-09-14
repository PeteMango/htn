from flask import Flask, jsonify, request
from app import app, supabase
from geopy import distance

@app.route('/')
def home():
    """Entrypoint into flask app

    Returns:
        json: welcome message
    """
    return jsonify({"message": "Welcome to the Flask app with Supabase!"})


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
