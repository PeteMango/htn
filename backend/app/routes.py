from flask import Flask, jsonify, request
from app import app, supabase

@app.route('/')
def home():
    """Entrypoint into flask app

    Returns:
        json: welcome message
    """
    return jsonify({"message": "Welcome to the Flask app with Supabase!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
