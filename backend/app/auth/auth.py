from flask import Flask, jsonify, request
from app import app, supabase

@app.route('/register', methods=['POST'])
def register_user():
    """Registers a new user into the website

    Returns:
        json: Registered user data or error message
    """
    data = request.json
    email = data['email']
    password = data['password']

    if not email or not password:
        return jsonify({"Error": "Email and password are required"}), 400

    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        if 'error' in response:
            return jsonify({"Error": "could not register"}), 400
        return jsonify({"Message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Logs in a user into the website

    Returns:
        json: Authentication token or error message
    """
    data = request.json
    email = data['email']
    password = data['password']

    if not email or not password:
        return jsonify({"Error": "Email and password are required"}), 400

    try:
        response = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )


        if 'error' in response:
            return jsonify({"Error": "Unauthorized login"}), 401

        return response.json(), 200
    except Exception as e:
        print(f'found error: {e}')
        return jsonify({"Error": str(e)}), 500
