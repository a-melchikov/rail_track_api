import React, { useState, useEffect } from "react";
import AddStation from "./AddStation"; // Предполагается, что этот компонент существует

const StationList = () => {
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStations = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/v1/stations");
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
    setStations((prevStations) => [...prevStations, newStation]);
  };

  const handleDeleteStation = async (id) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/stations/${id}`,
        {
          method: "DELETE",
        }
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // Обновление списка станций после удаления
      setStations((prevStations) =>
        prevStations.filter((station) => station.id !== id)
      );
    } catch (error) {
      console.error("Ошибка при удалении вокзала:", error);
    }
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  return (
    <div className="container">
      <h2>Список вокзалов</h2>
      <AddStation onAdd={handleAddStation} />
      <ul>
        {stations.map((station) => (
          <li key={station.id}>
            <div>
              <strong>ID: {station.id} - {station.name}, ИНН({station.tax_id})</strong>
            </div>
            <div>
              Адрес: {station.address.country}, г. {station.address.city},{" "}
              ул. {station.address.street}, д. {station.address.house},{" "}
              кв. {station.address.apartment}
            </div>
            <button onClick={() => handleDeleteStation(station.id)}>
              Удалить
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StationList;
