import React, { useState } from "react";
import axios from "axios";

const AddStation = () => {
  const [name, setName] = useState("");
  const [taxId, setTaxId] = useState("");
  const [addressId, setAddressId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const newStation = {
        name,
        tax_id: taxId,
        address_id: parseInt(addressId),
      };
      await axios.post("http://localhost:8000/api/v1/stations/", newStation);
      alert("Station added successfully");
    } catch (error) {
      console.error("Failed to add station", error);
      alert("Failed to add station");
    }
  };

  return (
    <div>
      <h2>Add New Station</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Tax ID:
          <input
            type="text"
            value={taxId}
            onChange={(e) => setTaxId(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Address ID:
          <input
            type="number"
            value={addressId}
            onChange={(e) => setAddressId(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Add Station</button>
      </form>
    </div>
  );
};

export default AddStation;
