import React from "react";
import { Link } from "react-router-dom";

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Главная</Link>
        </li>
        <li>
          <Link to="/stations">Вокзалы</Link>
        </li>
        <li>
          <Link to="/addresses">Адреса</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navigation;
