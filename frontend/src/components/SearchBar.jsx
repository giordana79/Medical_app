import React, { useState } from "react";

export default function SearchBar({ onSearch, onReset }) {
  const [campo, setCampo] = useState("descrizione");
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text) onSearch(campo, text);
  };

  return (
    <form className="search-bar" onSubmit={handleSubmit}>
      <select value={campo} onChange={(e) => setCampo(e.target.value)}>
        <option value="codice_ministeriale">Codice Ministeriale</option>
        <option value="codice_interno">Codice Interno</option>
        <option value="descrizione">Descrizione</option>
      </select>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Cerca..."
      />
      <button type="submit">Cerca</button>
      <button type="button" onClick={onReset}>
        Vedi tutti
      </button>
    </form>
  );
}
