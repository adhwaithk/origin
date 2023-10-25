from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import chat
# Import the load_dotenv function to load environment variables

# Load environment variables from .env

load_dotenv(r'C:\Users\235768\.env')


# Create a Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Access the environment variables
SECRET_KEY = os.environ.get("SECRET_KEY")
MONGO_URI = os.environ.get("MONGO_URI")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Set the configuration variables
app.config["MONGO_URI"] = MONGO_URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['Access-Control-Allow-Origin'] = '*'
app.config["Access-Control-Allow-Headers"] = "Content-Type"

# Initialize the PyMongo extension
mongo = PyMongo(app)

if __name__ == '__main__':
    from chat.chat import routes_bp
    from authorization.auth import auth_bp

    # Register the Blueprints
    app.register_blueprint(routes_bp) 
    app.register_blueprint(auth_bp)

    app.run(host='0.0.0.0', port=5000, debug=True)
