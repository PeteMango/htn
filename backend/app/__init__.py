import os
from flask import Flask
from supabase import create_client, Client

app = Flask(__name__)

SUPABASE_URL = os.getenv("API_URL")
SUPABASE_KEY = os.getenv("API_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

from app import routes
from app import toilet_routes
from app import user_routes
from app import building_routes
from app import review_routes
