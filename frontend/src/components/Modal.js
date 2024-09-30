import React, { useEffect } from "react";

const Modal = ({ message, onClose }) => {
  useEffect(() => {
    if (!message) return;

    // Таймер для автоматического закрытия через 3 секунды
    const timer = setTimeout(() => {
      onClose();
    }, 3000);

    return () => clearTimeout(timer); // Очищаем таймер при размонтировании
  }, [message, onClose]);

  if (!message) return null; // Если нет сообщения, не показываем модальное окно

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>
          &times;
        </button>
        <p>{message}</p>
      </div>
    </div>
  );
};

export default Modal;
