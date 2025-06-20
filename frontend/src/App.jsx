// frontend/src/App.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";
import Filters from "./components/Filters";
import GareCard from "./components/GareCard";
import "./App.css";

const App = () => {
  const [gares, setGares] = useState([]);
  const [filteredGares, setFilteredGares] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchGares();
  }, []);

  const fetchGares = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/data");
      setGares(response.data);
      setFilteredGares(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Erreur lors du fetch :", error);
      setLoading(false);
    }
  };

  const handleFilter = (nomGare) => {
    const filtered = gares.filter((gare) =>
      gare.nom_gare.toLowerCase().includes(nomGare.toLowerCase())
    );
    setFilteredGares(filtered);
  };

  return (
    <div className="app-container">
      <h1>Liste des Gares</h1>
      <Filters onFilter={handleFilter} />
      {loading ? (
        <p>Chargement des données...</p>
      ) : (
        <div className="cards-grid">
          {filteredGares.map((gare) => (
            <GareCard key={gare.id} gare={gare} />
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
