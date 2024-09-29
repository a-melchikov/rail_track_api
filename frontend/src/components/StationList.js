import React, { useState, useEffect } from "react";
import AddStation from "./AddStation";

const StationList = () => {
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editingStationId, setEditingStationId] = useState(null); // Для отслеживания редактируемого вокзала
  const [editingStation, setEditingStation] = useState({}); // Для хранения редактируемого вокзала

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
    setStations((prevStations) => [...prevStations, newStation]);
  };

  const handleDeleteStation = async (id) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/stations/${id}/`,
        {
          method: "DELETE",
        }
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      setStations((prevStations) =>
        prevStations.filter((station) => station.id !== id)
      );
    } catch (error) {
      console.error("Ошибка при удалении вокзала:", error);
    }
  };

  const handleEditStation = (id) => {
    const stationToEdit = stations.find((station) => station.id === id);
    setEditingStationId(id);
    setEditingStation({ ...stationToEdit });
  };

  const handleUpdateStation = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/stations/${editingStationId}/`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(editingStation),
        }
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const updatedStation = await response.json();
      setStations((prevStations) =>
        prevStations.map((station) =>
          station.id === editingStationId ? updatedStation : station
        )
      );

      setEditingStationId(null);
      setEditingStation({});
    } catch (error) {
      console.error("Ошибка при обновлении вокзала:", error);
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
      <AddStation onAddStation={handleAddStation} />
      <ul>
        {stations.map((station) => (
          <li key={station.id}>
            {editingStationId === station.id ? (
              <div>
                <input
                  type="text"
                  value={editingStation.name}
                  onChange={(e) =>
                    setEditingStation({
                      ...editingStation,
                      name: e.target.value,
                    })
                  }
                  placeholder="Название вокзала"
                />
                <input
                  type="text"
                  value={editingStation.tax_id}
                  onChange={(e) =>
                    setEditingStation({
                      ...editingStation,
                      tax_id: e.target.value,
                    })
                  }
                  placeholder="ИНН"
                />
                <input
                  type="text"
                  value={editingStation.address_id}
                  onChange={(e) =>
                    setEditingStation({
                      ...editingStation,
                      address_id: e.target.value,
                    })
                  }
                  placeholder="ID адреса"
                />
                <div>
                  <button onClick={handleUpdateStation}>Сохранить</button>
                  <button onClick={() => setEditingStationId(null)}>
                    Отмена
                  </button>
                </div>
              </div>
            ) : (
              <div>
                <strong>ID: {station.id}</strong> - Название: {station.name},
                ИНН: {station.tax_id}, Адрес: {station.address_id}
                <div>
                  <button
                    className="top-button button-spacing"
                    onClick={() => handleEditStation(station.id)}
                  >
                    Редактировать
                  </button>
                  <button
                    className="bottom-button button-spacing"
                    onClick={() => handleDeleteStation(station.id)}
                  >
                    Удалить
                  </button>
                </div>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StationList;
