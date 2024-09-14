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
    return jsonify({"message": "Welcome to the Flask app with Supabase!"})

@app.route('/insert', methods=['POST'])
def insert_data():
    # Get data from the POST request
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    # Insert data into the Supabase 'toilets' table
    response = supabase.table(data.get("table", "Toilet")).insert({
        "tid": data.get("tid", 1),
        "lat": data.get("lat", 1.0),
        "long": data.get("long", 1.0),
        "info": data.get("info", "this is test toilet"),
        "gender": data.get("gender", True)
    }).execute()

    return jsonify(response.data)

@app.route('/toilets', methods=['GET'])
def get_toilets():
    # Retrieve all entries from the 'toilets' table
    data = request.json
    response = supabase.table(data.get("table", "Toilet")).select("*").execute()

    if response.data:
        return jsonify(response.data), 200
    else:
        return jsonify({"message": "No data found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
