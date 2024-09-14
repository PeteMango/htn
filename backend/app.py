import os
from supabase import create_client, Client

url: str = os.environ.get("API_URL")
key: str = os.environ.get("API_KEY")
supabase: Client = create_client(url, key)

# response = (supabase.table("toilets").insert({
#     "tid": 1,
#     "lat": 1.0,
#     "lng": 1.0,
#     "info": "this is test toilet",
#     "gender": True
# }).execute())

response = supabase.table("toilets").select("*").execute()

print(response)