import React, { useEffect } from "react";
import Mappedin from "@mappedin/mappedin-js";
import "@mappedin/mappedin-js/lib/index.css";
import "./styles.css";

const MappedinMap: React.FC = () => {
  useEffect(() => {
    const initializeMap = async () => {
      try {
        const mappedin = new Mappedin.Platform({
          apiKey: "mik_WkkfvbPrlL67HdtXj590107d5", // replace with your actual key
          apiSecret: "mis_5fIaY1OsJLTLIseuTDpVrXr6YmSkqibt8DuyyZE9kYI91e610d2", // replace with your actual secret
        });

        // Fetch map data
        const mapData = await mappedin.getVenue("66e5fe99ecc9c8000baa8e03"); // replace with your actual map ID

        // Show the 3D map in the container
        const mapView = await Mappedin.show3dMap(
          document.getElementById("mappedin-map") as HTMLElement,
          mapData
        );

        // Optionally, display all labels
        mapView.Labels.all();
      } catch (error) {
        console.error("Error loading the map:", error);
      }
    };

    initializeMap();
  }, []);

  return <div id="mappedin-map" style={{ width: "100%", height: "500px" }} />;
};

export default MappedinMap;
