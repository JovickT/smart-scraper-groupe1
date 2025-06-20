import React, { useState } from 'react';
import "../App.css"

const Filters = ({ onFilterChange }) => {
  const [nomGare, setNomGare] = useState('');
  const [annee, setAnnee] = useState('');
  const [codePostal, setCodePostal] = useState('');
  const [segmentation, setSegmentation] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Envoie les filtres non vides au parent
    const filters = {};
    if (nomGare) filters.nom_gare = nomGare;
    if (annee) filters.annee = annee;
    if (codePostal) filters.code_postal = codePostal;
    if (segmentation) filters.segmentation = segmentation;

    onFilterChange(filters);
  };

  const handleReset = () => {
    setNomGare('');
    setAnnee('');
    setCodePostal('');
    setSegmentation('');
    onFilterChange({});
  };

  return (
    <form onSubmit={handleSubmit} className="filter-form">
      <input
        type="text"
        placeholder="Nom de la gare"
        value={nomGare}
        onChange={(e) => setNomGare(e.target.value)}
      />
      <input
        type="number"
        placeholder="Année (ex: 2020)"
        value={annee}
        onChange={(e) => setAnnee(e.target.value)}
      />
      <input
        type="text"
        placeholder="Code postal"
        value={codePostal}
        onChange={(e) => setCodePostal(e.target.value)}
      />
      <input
        type="text"
        placeholder="Segmentation DRG"
        value={segmentation}
        onChange={(e) => setSegmentation(e.target.value)}
      />

      <button type="submit">Filtrer</button>
      <button type="button" onClick={handleReset}>Réinitialiser</button>
    </form>
  );
};

export default Filters;