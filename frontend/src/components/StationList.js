import React, { useState, useEffect } from "react";
import AddStation from "./AddStation";

const StationList = () => {
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStations = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/v1/stations/");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setStations(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchStations();
  }, []);

  const handleAddStation = (newStation) => {
    setStations((prev) => [...prev, newStation]);
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  return (
    <div>
      <h2>Список вокзалов</h2>
      <AddStation onAddStation={handleAddStation} />
      <ul>
        {stations.map((station) => (
          <li key={station.id}>
            {station.name} - {station.tax_id} (ID адреса: {station.address_id})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StationList;
