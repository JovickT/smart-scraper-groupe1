-- Création de la base de données (optionnel si déjà créée dans Docker)
CREATE DATABASE IF NOT EXISTS smartscraper CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE smartscraper;

CREATE TABLE gares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_gare VARCHAR(255) NOT NULL,
    code_uic_complet VARCHAR(50),
    code_postal VARCHAR(20),
    segmentation_drg VARCHAR(5)
);

CREATE TABLE voyageurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gare_id INT NOT NULL,
    annee INT NOT NULL,
    total_voyageurs INT,
    total_non_voyageurs INT,
    FOREIGN KEY (gare_id) REFERENCES gares(id)
);

