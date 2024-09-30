import React, { useState, useEffect } from "react";
import AddStation from "./AddStation";
import Modal from "./Modal";

const StationList = () => {
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingStationId, setEditingStationId] = useState(null);
  const [editingStation, setEditingStation] = useState({});
  const [modalMessage, setModalMessage] = useState(""); // Состояние для сообщения модального окна

  const handleError = (error) => {
    console.error(error);
    setModalMessage(error.message);
  };

  useEffect(() => {
    const fetchStations = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/v1/stations/");
        if (!response.ok) {
          throw new Error("Не удалось загрузить вокзалы");
        }
        const data = await response.json();
        setStations(data);
      } catch (error) {
        handleError(error);
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
        throw new Error("Не удалось удалить вокзал");
      }

      setStations((prevStations) =>
        prevStations.filter((station) => station.id !== id)
      );
    } catch (error) {
      handleError(error);
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
        throw new Error("Не удалось обновить вокзал");
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
      handleError(error);
    }
  };

  const handleCloseModal = () => {
    setModalMessage(""); // Закрываем модальное окно
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  return (
    <div className="container">
      <h2>Список вокзалов</h2>
      <AddStation
        onAddStation={handleAddStation}
        setModalMessage={setModalMessage}
      />
      <ul>
        {stations.map((station) => (
          <li key={station.id}>
            {editingStationId === station.id ? (
              <div>
                <input
                  type="text"
                  value={editingStation.name || ""}
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
                  value={editingStation.tax_id || ""}
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
                  value={editingStation.address_id || ""}
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
      {modalMessage && (
        <Modal message={modalMessage} onClose={handleCloseModal} />
      )}{" "}
      {/* Добавляем модальное окно */}
    </div>
  );
};

export default StationList;
