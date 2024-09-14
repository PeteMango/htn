from flask import Flask, jsonify, request
from app import app, supabase

@app.route("/add_review", methods=["POST"])
def add_review():
    """Adds a review to a specific toilet
        
    Args:
        tid (int): the toilet id
        uid (int): the user id
        rating (float): the rating of the toilet out of 10
        review (str): text description of the review
        
    Returns:
        json: the added review object
    """
    data = request.json

    tid = data["tid"]
    if not supabase.table("Toilet").select("tid").eq("tid",
                                                     tid).execute().data:
        return jsonify({"Error": "Toilet does not exist"}), 404

    uid = data["uid"]
    if not supabase.table("User").select("uid").eq("uid", uid).execute().data:
        return jsonify({"Error": "User does not exist"}), 404

    rating, review = data["rating"], data["review"]

    print(data)

    if rating is None or review == "":
        return jsonify({"Error": "Did not provide a rating or review"}), 400

    if rating > 10 or rating < 0:
        return jsonify({"Error": "Rating must be between 0 and 10"}), 400

    response = supabase.table("Reviews").upsert({
        "tid": tid,
        "uid": uid,
        "rating": rating,
        "review": review
    }).execute()

    return jsonify(response.data), 201
