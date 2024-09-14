from flask import Flask, jsonify, request
from app import app, supabase

@app.route("/add_review", methods=["POST"])
def add_review():
    """Adds a review to a specific toilet
        - requires a toilet id (tid)
        - requires a rating
        - requires a review
    Returns:
        json: the added review object
    """

    tid = request.args.get("tid")
    rating = request.args.get("rating")
    review = request.args.get("review")

    try:
        if tid is None:
            return jsonify({"error": f"Bad request, did not provide a tid, rating, review"}), 400
        
        

        supabase.table("ToiletUser")

    except Exception as e:
        return jsonify({"error": f"Failed to add review: {str(e)}"}), 500