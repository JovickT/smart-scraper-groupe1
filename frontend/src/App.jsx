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
  const [filters, setFilters] = useState({});

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

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters); // garde les filtres

    const filtered = gares.filter((gare) => {
      const matchNom = newFilters.nom_gare
        ? gare.nom_gare.toLowerCase().includes(newFilters.nom_gare.toLowerCase())
        : true;

      const matchAnnee = newFilters.annee
        ? gare.voyageurs.some((v) => v.annee === parseInt(newFilters.annee))
        : true;

      const matchCP = newFilters.code_postal
        ? gare.code_postal === newFilters.code_postal
        : true;

      const matchSeg = newFilters.segmentation
        ? gare.segmentation_drg?.toLowerCase().includes(newFilters.segmentation.toLowerCase())
        : true;

      return matchNom && matchAnnee && matchCP && matchSeg;
    });

    setFilteredGares(filtered);
  };
  return (
    <div className="app-container">
      <h1>Liste des Gares</h1>
      <Filters onFilterChange={handleFilterChange} />
      {loading ? (
        <p>Chargement des données...</p>
      ) : (
        <div className="cards-grid">
          {filteredGares.map((gare) => (
            <GareCard
              key={gare.id}
              gare={{
                ...gare,
                voyageurs: filters.annee
                  ? gare.voyageurs.filter((v) => v.annee === parseInt(filters.annee))
                  : gare.voyageurs,
              }}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default App;