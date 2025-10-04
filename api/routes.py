from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/data")
def get_data():
    # Example: return sample data for visualization
    return jsonify({
        "x": [1, 2, 3, 4],
        "y": [10, 15, 7, 20]
    })
