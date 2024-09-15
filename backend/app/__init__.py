import os
from flask import Flask
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = "Content-Type"

SUPABASE_URL = os.getenv("API_URL")
SUPABASE_KEY = os.getenv("API_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

from app.api import routes, toilets, users, building, reviews
from app.auth import auth