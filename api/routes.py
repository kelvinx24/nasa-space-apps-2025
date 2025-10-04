from flask import Blueprint, request, jsonify
from .physics import simulate_impact

api_bp = Blueprint("api", __name__)

@api_bp.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    mass = float(data.get("mass", 1e9))       # kg
    velocity = float(data.get("velocity", 20000))  # m/s
    angle = float(data.get("angle", 45))      # degrees

    result = simulate_impact(mass, velocity, angle)
    return jsonify(result)
