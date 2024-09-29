import React, { useState } from "react";

const AddStation = ({ onAddStation }) => {
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
        throw new Error("Network response was not ok");
      }

      const createdStation = await response.json();
      onAddStation(createdStation);
      setNewStation({ name: "", tax_id: "", address_id: "" }); // сброс формы
    } catch (error) {
      console.error("Ошибка при добавлении вокзала:", error);
    }
  };

  return (
    <div>
      <h3>Добавить новый вокзал</h3>
      <form onSubmit={handleSubmit}>
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
