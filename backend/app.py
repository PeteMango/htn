import os
from supabase import create_client, Client

url: str = "https://abhuhlniginkudwghcfx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiaHVobG5pZ2lua3Vkd2doY2Z4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYzMjUxODQsImV4cCI6MjA0MTkwMTE4NH0.mHMFsGtSX_3XofoYyVzMnN3x0m-129rkHtDr9dHBGgI"
supabase: Client = create_client(url, key)

print('done')
