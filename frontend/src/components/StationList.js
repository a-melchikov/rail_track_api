import React, { useState, useEffect } from 'react';

function StationList() {
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Функция для получения данных с API
    const fetchStations = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/v1/stations');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log(data); // Проверяем, что данные пришли
        setStations(data); // Устанавливаем данные в состояние
      } catch (error) {
        console.error('Error fetching stations:', error);
      } finally {
        setLoading(false); // Останавливаем индикатор загрузки
      }
    };

    fetchStations();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>Stations</h1>
      <ul>
        {stations.map((station) => (
          <li key={station.id}>
            <strong>{station.name}</strong><br />
            <em>Tax ID:</em> {station.tax_id}<br />
            <em>Address:</em> {station.address.country}, {station.address.city}, {station.address.street}, {station.address.house}, {station.address.apartment}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StationList;
