import React from "react";

export default function Panel({ title, items, selectedId, onSelect }) {
  return (
    <div className="panel">
      <h2>{title}</h2>
      <ul>
        {items.map((item) => (
          <li
            key={item.id}
            className={selectedId === item.id ? "selected" : ""}
            onClick={() => onSelect(item.id)}
          >
            {item.nome}
          </li>
        ))}
      </ul>
    </div>
  );
}
