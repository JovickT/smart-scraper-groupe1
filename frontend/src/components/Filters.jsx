// frontend/src/Filters.jsx
import React, { useState } from "react";

const Filters = ({ onFilter }) => {
  const [nom, setNom] = useState("");

  const handleChange = (e) => {
    const value = e.target.value;
    setNom(value);
    onFilter(value);
  };

  return (
    <div style={{ marginBottom: "1.5rem", width: "100%", maxWidth: "600px" }}>
      <input
        type="text"
        placeholder="Rechercher une gare..."
        value={nom}
        onChange={handleChange}
        style={{
          width: "100%",
          padding: "0.8rem",
          fontSize: "1rem",
          borderRadius: "8px",
          border: "1px solid #ccc",
          boxShadow: "0 2px 4px rgba(0,0,0,0.05)",
        }}
      />
    </div>
  );
};

export default Filters;
