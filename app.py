from flask import Flask, send_from_directory
from api.routes import api_bp
import os

app = Flask(__name__, static_folder="dist", static_url_path="")
app.register_blueprint(api_bp, url_prefix="/api")

# Serve Vite build
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
