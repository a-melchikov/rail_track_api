// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import StationList from "./components/StationList";
import AddressList from "./components/AddressList";
import "./styles.css";

const App = () => {
  return (
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stations" element={<StationList />} />
          <Route path="/addresses" element={<AddressList />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
