import React, { useState, useEffect } from "react";
import AddAddress from "./AddAddress";

const AddressList = () => {
  const [addresses, setAddresses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAddresses = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/v1/addresses/");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setAddresses(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchAddresses();
  }, []);

  const handleAddAddress = (newAddress) => {
    setAddresses((prevAddresses) => [...prevAddresses, newAddress]);
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  return (
    <div>
      <h2>Список адресов</h2>
      <AddAddress onAdd={handleAddAddress} />
      <ul>
        {addresses.map((address) => (
          <li key={address.id}>
            {address.country}, {address.city}, {address.street}, {address.house}
            , {address.apartment}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AddressList;
