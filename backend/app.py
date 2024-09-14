import os
from flask import Flask, jsonify, request
from supabase import create_client, Client

app = Flask(__name__)

# Initialize Supabase client
SUPABASE_URL = os.getenv("API_URL")
SUPABASE_KEY = os.getenv("API_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    """Entrypoint into flask app

    Returns:
        None
    """
    return jsonify({"message": "Welcome to the Flask app with Supabase!"})

@app.route('/insert', methods=['POST'])
def insert_data():
    """Insert into the database

    Args:
        Information dependent on the table inserted into 

    Returns:
        json: information inserted into the database
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    response = None
    if not data.get("table"):
        return jsonify({"error": "Table name is required"}), 400

    if data.get("table") == "Toilet":
        if not data.get("tid"):
            return jsonify({"error": "User ID is required"}), 400

        response = supabase.table("Toilet").insert({
            "tid":
            data.get("tid", -1),
            "lat":
            data.get("lat", 0),
            "long":
            data.get("long", 0),
            "info":
            data.get("info", ""),
            "gender":
            data.get("gender", "")
        }).execute()
        return jsonify(response.data)

    if data.get("table") == "User":
        if not data.get("uid"):
            return jsonify({"error": "User ID is required"}), 400

        response = supabase.table("User").insert({
            "uid":
            data.get("uid", -1),
            "email":
            data.get("email", ""),
            "gender":
            data.get("gender", ""),
        }).execute()
        return jsonify(response.data)

    return jsonify({"error": "invalid table name"}), 400

@app.route('/toilets', methods=['GET'])
def get_toilets():
    """Returns all the toilets & their location

    Returns:
        json: toilet information
    """
    data = request.json
    response = supabase.table(data.get("table",
                                       "Toilet")).select("*").execute()

    if response.data:
        return jsonify(response.data), 200

    return jsonify({"message": "No data found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
