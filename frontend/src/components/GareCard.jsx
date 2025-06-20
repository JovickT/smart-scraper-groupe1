// frontend/src/GareCard.jsx
import React, { useState } from "react";
import "../App.css";

const GareCard = ({ gare }) => {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="card" onClick={() => setExpanded(!expanded)}>
      <div className="card-title">{gare.nom_gare}</div>

      {expanded && (
        <div className="card-details">
          <p><strong>Code UIC :</strong> {gare.code_uic_complet}</p>
          <p><strong>Code postal :</strong> {gare.code_postal}</p>
          <p><strong>Segmentation :</strong> {gare.segmentation_drg}</p>
          <hr />
          {gare.voyageurs.map((v) => (
            <p key={v.annee}>
              <strong>{v.annee} :</strong> {v.total_voyageurs.toLocaleString()} voyageurs
            </p>
          ))}
        </div>
      )}
    </div>
  );
};

export default GareCard;
