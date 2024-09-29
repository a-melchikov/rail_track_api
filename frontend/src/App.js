import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import StationList from "./components/StationList";
import AddStation from "./components/AddStation";

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<StationList />} />
          <Route path="/add-station" element={<AddStation />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
