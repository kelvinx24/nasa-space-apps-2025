from flask import Flask, render_template
from api.routes import api_bp

app = Flask(__name__)

# Register blueprint for API routes
app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
