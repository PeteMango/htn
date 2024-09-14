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

@app.route('/insert_toilet', methods=['POST'])
def insert_toilet():
    """Insert into the toilets table

    Args:
        tid (int): toilet id
        lat (float): latitude
        long (float): longitude
        info (str): additional information
        geder (str): gender of the washroom

    Returns:
        json: information inserted into the database
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    if not data.get("tid"):
        return jsonify({"error": "User ID is required"}), 400

    response = supabase.table("Toilet").insert({
        "tid": data.get("tid", -1),
        "lat": data.get("lat", 0),
        "long": data.get("long", 0),
        "info": data.get("info", ""),
        "gender": data.get("gender", "")
    }).execute()
    return jsonify(response.data)

@app.route('/insert_user', methods=['POST'])
def insert_user():
    """Insert into the user table

    Args:
        uid (int): user id
        email (str): email
        gender (str): user gender

    Returns:
        json: information inserted into the database
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    if not data.get("uid"):
        return jsonify({"error": "User ID is required"}), 400

    response = supabase.table("User").insert({
        "uid": data.get("uid", -1),
        "email": data.get("email", ""),
        "gender": data.get("gender", ""),
    }).execute()
    return jsonify(response.data)

@app.route('/insert_tag', methods=['POST'])
def insert_tag():
    """Insert into the tag table

    Args:
        tag (str): accessibility tags

    Returns:
        json: information inserted into the database
    """
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    if not data.get("tag_name"):
        return jsonify({"error": "Tag name is required"}), 400

    response = supabase.table("Tag").insert({
        "tag_name": data.get("tag_name", "ERROR"),
    }).execute()
    return jsonify(response.data)

@app.route('/toilets', methods=['GET'])
def get_toilets():
    """Returns all the toilets & their location

    Returns:
        json: toilet information
    """
    tid = request.args.get("tid")

    if tid is None:
        response = supabase.table("Toilet").select("*").execute()
    else:
        response = supabase.table("Toilet").select("*").eq("tid",
                                                           tid).execute()

    if response.data:
        return jsonify(response.data), 200
    return jsonify({"message": "No data found"}), 404

@app.route('/users', methods=['GET'])
def get_users():
    """Returns all the users & their information

    Returns:
        json: user information
    """
    uid = request.args.get("uid")

    if uid is None:
        response = supabase.table("User").select("*").execute()
    else:
        response = supabase.table("User").select("*").eq("uid", uid).execute()

    if response.data:
        return jsonify(response.data), 200
    return jsonify({"message": "No data found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
