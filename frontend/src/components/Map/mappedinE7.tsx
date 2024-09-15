import React, { useEffect } from "react";
import { MapView, useMap, useMapData, Label} from "@mappedin/react-sdk";
// import "@mappedin/react-sdk/lib/esm/index.css"
// import "./styles.css";


const MappedinMap: React.FC = () => {

  const { isLoading, error, mapData} = useMapData({
    key: "mik_WkkfvbPrlL67HdtXj590107d5",
    secret: "mis_5fIaY1OsJLTLIseuTDpVrXr6YmSkqibt8DuyyZE9kYI91e610d2",
    mapId: "66e5fe99ecc9c8000baa8e03"
  })

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>

  return mapData? (
    <MapView mapData={mapData} style={{ width: "100%", height: "500px" }}>
    </MapView>
  ) : <div></div>

  // useEffect(() => {
  //   const initializeMap = async () => {
  //     try {
  //       const mappedin = new Mappedin.pl({
  //         apiKey: "mik_WkkfvbPrlL67HdtXj590107d5", // replace with your actual key
  //         apiSecret: "mis_5fIaY1OsJLTLIseuTDpVrXr6YmSkqibt8DuyyZE9kYI91e610d2", // replace with your actual secret
  //       });

  //       // Fetch map data
  //       const mapData = await mappedin.getVenue("66e5fe99ecc9c8000baa8e03"); // replace with your actual map ID

  //       // Show the 3D map in the container
  //       const mapView = await Mappedin.show3dMap(
  //         document.getElementById("mappedin-map") as HTMLElement,
  //         mapData
  //       );

  //       // Optionally, display all labels
  //       mapView.Labels.all();
  //     } catch (error) {
  //       console.error("Error loading the map:", error);
  //     }
  //   };
  //   initializeMap();
  // }, []);


 // return <div id="mappedin-map" style={{ width: "100%", height: "500px" }} />;
};

export default MappedinMap;
