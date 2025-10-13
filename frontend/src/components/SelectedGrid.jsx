import React, { useEffect, useState } from "react";
import "./SelectedGrid.css";

export default function SelectedGrid({ items, removeItem, moveUp, moveDown }) {
  const [draggedIdx, setDraggedIdx] = useState(null);
  const [gridItems, setGridItems] = useState(items);

  useEffect(() => {
    setGridItems(items);
  }, [items]);

  const handleDragStart = (idx) => setDraggedIdx(idx);
  const handleDragOver = (e) => e.preventDefault();

  const handleDrop = (idx) => {
    if (draggedIdx === null || draggedIdx === idx) return;
    const newArr = [...gridItems];
    const [moved] = newArr.splice(draggedIdx, 1);
    newArr.splice(idx, 0, moved);
    setGridItems(newArr);
    setDraggedIdx(null);
    localStorage.setItem("selectedExams", JSON.stringify(newArr));
  };

  return (
    <div className="selected-grid">
      <h2>Esami selezionati</h2>
      <ul>
        {gridItems.map((item, idx) => (
          <li
            key={item.id}
            draggable
            onDragStart={() => handleDragStart(idx)}
            onDragOver={handleDragOver}
            onDrop={() => handleDrop(idx)}
            className="grid-item"
          >
            <span>{item.descrizione}</span>
            <div className="buttons">
              <button onClick={() => moveUp(idx)}>↑</button>
              <button onClick={() => moveDown(idx)}>↓</button>
              <button onClick={() => removeItem(idx)}>✕</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
