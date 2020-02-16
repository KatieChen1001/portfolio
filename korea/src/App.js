import React from "react";
import Gallery from "react-photo-gallery";
import { photos } from "./components/photos.js";
import "./App.css";
function App() {
  return (
    <div className="App">
      <Gallery photos={photos} direction="column" />
    </div>
  );
}

export default App;
