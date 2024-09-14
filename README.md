# What's your Loo? 🚽

### Find Your Perfect Spot, Anytime, Anywhere!

👉  **What's your Loo?** is designed to make finding the best public washrooms simple and personalized. With location-based recommendations, users can instantly discover the nearest washroom, especially in unfamiliar areas or when time is of the essence. 

👉  The app combines all of the important factors — **gender suitability**, **location**, **cleanliness**, and **popularity** — so users are guaranteed to get the **best washroom experience**, in real time. Users can rate washrooms based on experience, functionality, hygiene, and aesthetics, which are are factored into future recommendations. Washrooms that consistently receive high scores and positive reviews are marked as popular, ensuring users have access to **community-driven insights** to find the best spots!

## Project Structure

### Frontend
The frontend is powered by Next.js and Leaflet. It allows users to view the locations of public washrooms on a map, submit reviews, and read reviews from other users.

**Tech Stack:** TypeScript, Next.js, Leaflet (leaflet-react starter kit)

**Main Features:**
- Live and interactive map of public washrooms
- Search for nearby washrooms based on location
- User reviews and ratings for each washroom

### Backend
The backend is built using Flask and serves as the API for managing user data and reviews. It connects to Supabase, which acts as the database to store washroom locations, reviews, and user data.

**Tech Stack:** Python, Flask, Supabase

**API Endpoints:**
- `GET /washrooms`: Retrieve a list of public washrooms and their locations
...
