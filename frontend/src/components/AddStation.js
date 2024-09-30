import React, { useState } from "react";

const AddStation = ({ onAddStation, setModalMessage }) => {
  const [newStation, setNewStation] = useState({
    name: "",
    tax_id: "",
    address_id: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewStation((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/v1/stations/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newStation),
      });

      if (!response.ok) {
        const errorData = await response.json();
        // Обработка ошибок из JSON-ответа
        const errorMessages = errorData.detail
          .map((error) => error.msg)
          .join(", ");
        throw new Error(errorMessages || "Не удалось добавить вокзал");
      }

      const createdStation = await response.json();
      onAddStation(createdStation);
      setModalMessage("Вокзал успешно добавлен!"); // Устанавливаем сообщение для модального окна
      setNewStation({ name: "", tax_id: "", address_id: "" }); // Сброс формы
    } catch (error) {
      console.error("Ошибка при добавлении вокзала:", error);
      setModalMessage(error.message); // Устанавливаем сообщение об ошибке
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <h3>Добавить вокзал</h3>
        <input
          type="text"
          name="name"
          value={newStation.name}
          onChange={handleInputChange}
          placeholder="Название вокзала"
          required
        />
        <input
          type="text"
          name="tax_id"
          value={newStation.tax_id}
          onChange={handleInputChange}
          placeholder="ИНН (12 цифр)"
          required
        />
        <input
          type="text"
          name="address_id"
          value={newStation.address_id}
          onChange={handleInputChange}
          placeholder="ID адреса"
          required
        />
        <button type="submit">Добавить вокзал</button>
      </form>
    </div>
  );
};

export default AddStation;
