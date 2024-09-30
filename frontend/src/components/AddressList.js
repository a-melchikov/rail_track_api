import React, { useState, useEffect } from "react";
import AddAddress from "./AddAddress";
import Modal from "./Modal"; // Импортируйте модальное окно

const AddressList = () => {
  const [addresses, setAddresses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingAddressId, setEditingAddressId] = useState(null);
  const [editingAddress, setEditingAddress] = useState({});

  // Состояние для модального окна
  const [modalMessage, setModalMessage] = useState(null);

  const handleError = (error) => {
    console.error(error);
    setModalMessage(error.message);
  };

  useEffect(() => {
    const fetchAddresses = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/v1/addresses/");
        if (!response.ok) {
          throw new Error("Не удалось загрузить адреса");
        }
        const data = await response.json();
        setAddresses(data);
      } catch (error) {
        handleError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchAddresses();
  }, []);

  const handleAddAddress = (newAddress) => {
    setAddresses((prevAddresses) => [...prevAddresses, newAddress]);
  };

  const handleDeleteAddress = async (id) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/addresses/${id}/`,
        {
          method: "DELETE",
        }
      );

      if (!response.ok) {
        throw new Error("Не удалось удалить адрес");
      }

      setAddresses((prevAddresses) =>
        prevAddresses.filter((address) => address.id !== id)
      );
    } catch (error) {
      handleError(error);
    }
  };

  const handleEditAddress = (id) => {
    const addressToEdit = addresses.find((address) => address.id === id);
    setEditingAddressId(id);
    setEditingAddress({ ...addressToEdit });
  };

  const handleUpdateAddress = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/addresses/${editingAddressId}/`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(editingAddress),
        }
      );

      if (!response.ok) {
        throw new Error("Не удалось обновить адрес");
      }

      const updatedAddress = await response.json();
      setAddresses((prevAddresses) =>
        prevAddresses.map((address) =>
          address.id === editingAddressId ? updatedAddress : address
        )
      );

      setEditingAddressId(null);
      setEditingAddress({});
    } catch (error) {
      handleError(error);
    }
  };

  const closeModal = () => {
    setModalMessage(null);
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  return (
    <div className="container">
      <h2>Список адресов</h2>
      <AddAddress onAdd={handleAddAddress} setModalMessage={setModalMessage} />
      <ul>
        {addresses.map((address) => (
          <li key={address.id}>
            {editingAddressId === address.id ? (
              <div>
                <input
                  type="text"
                  value={editingAddress.country || ""}
                  onChange={(e) =>
                    setEditingAddress({
                      ...editingAddress,
                      country: e.target.value,
                    })
                  }
                  placeholder="Страна"
                />
                <input
                  type="text"
                  value={editingAddress.city || ""}
                  onChange={(e) =>
                    setEditingAddress({
                      ...editingAddress,
                      city: e.target.value,
                    })
                  }
                  placeholder="Город"
                />
                <input
                  type="text"
                  value={editingAddress.street || ""}
                  onChange={(e) =>
                    setEditingAddress({
                      ...editingAddress,
                      street: e.target.value,
                    })
                  }
                  placeholder="Улица"
                />
                <input
                  type="text"
                  value={editingAddress.house || ""}
                  onChange={(e) =>
                    setEditingAddress({
                      ...editingAddress,
                      house: e.target.value,
                    })
                  }
                  placeholder="Дом"
                />
                <input
                  type="text"
                  value={editingAddress.apartment || ""}
                  onChange={(e) =>
                    setEditingAddress({
                      ...editingAddress,
                      apartment: e.target.value,
                    })
                  }
                  placeholder="Квартира"
                />
                <div>
                  <button onClick={handleUpdateAddress}>Сохранить</button>
                  <button onClick={() => setEditingAddressId(null)}>
                    Отмена
                  </button>
                </div>
              </div>
            ) : (
              <div>
                <strong>ID: {address.id}</strong> - Адрес: {address.country}, г.{" "}
                {address.city}, ул. {address.street}, д. {address.house}, кв.{" "}
                {address.apartment}
                <div>
                  <button
                    className="top-button"
                    onClick={() => handleEditAddress(address.id)}
                  >
                    Редактировать
                  </button>
                  <button
                    className="bottom-button"
                    onClick={() => handleDeleteAddress(address.id)}
                  >
                    Удалить
                  </button>
                </div>
              </div>
            )}
          </li>
        ))}
      </ul>
      {modalMessage && <Modal message={modalMessage} onClose={closeModal} />}
    </div>
  );
};

export default AddressList;
