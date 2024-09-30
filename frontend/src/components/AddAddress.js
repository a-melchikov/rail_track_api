import React, { useState } from "react";

const AddAddress = ({ onAdd, setModalMessage }) => {
  const [country, setCountry] = useState("");
  const [city, setCity] = useState("");
  const [street, setStreet] = useState("");
  const [house, setHouse] = useState("");
  const [apartment, setApartment] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newAddress = { country, city, street, house, apartment };

    try {
      const response = await fetch("http://localhost:8000/api/v1/addresses/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newAddress),
      });

      if (!response.ok) {
        const errorData = await response.json();
        // Обработка ошибок из JSON-ответа
        const errorMessages = errorData.detail
          .map((error) => error.msg)
          .join(", ");
        throw new Error(errorMessages || "Не удалось добавить адрес");
      }

      const createdAddress = await response.json(); // Получаем созданный адрес из ответа
      onAdd(createdAddress); // Передаем созданный адрес в родительский компонент

      // Очистка формы
      setCountry("");
      setCity("");
      setStreet("");
      setHouse("");
      setApartment("");
    } catch (error) {
      setModalMessage(error.message); // Устанавливаем сообщение для модального окна
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <h3>Добавить адрес</h3>
        <input
          type="text"
          placeholder="Страна"
          value={country}
          onChange={(e) => setCountry(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Город"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Улица"
          value={street}
          onChange={(e) => setStreet(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Дом"
          value={house}
          onChange={(e) => setHouse(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Квартира"
          value={apartment}
          onChange={(e) => setApartment(e.target.value)}
        />
        <button type="submit">Добавить адрес</button>
      </form>
    </div>
  );
};

export default AddAddress;
