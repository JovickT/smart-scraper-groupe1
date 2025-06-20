# 🚄 Smart Scraper - Groupe 1

Ce projet est une application web qui **scrape les données de fréquentation des gares SNCF** et les affiche sur une interface web. Il utilise un backend Flask connecté à une base de données MySQL, et un frontend en React.

---

## 📦 Technologies utilisées

* **Backend** : Flask + SQLAlchemy
* **Frontend** : React
* **Base de données** : MySQL 8
* **Scraping** : API publique de la SNCF
* **Conteneurisation** : Docker & Docker Compose

---

## 🚀 Installation & Lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/JovickT/smart-scraper-groupe1.git
cd smart-scraper-groupe1
```

### 2. Créer un environnement virtuel pour le backend (optionnel pour dev local)

```bash
cd backend
python -m venv venv
```

> Active l’environnement selon ton OS si tu veux travailler hors Docker.

### 3. Revenir à la racine et démarrer les conteneurs

```bash
cd ..
docker compose up -d
```

> Cela lance :
>
> * le backend Flask (port `5000`)
> * le frontend React (port `3000`)
> * la base MySQL (port `3306`)

---

## 📡 Utilisation

### 1. Lancer le scraping via Postman (ou curl)

Après avoir démarré les conteneurs avec `docker compose up -d`, **attends quelques secondes** que la base de données et le backend soient bien prêts.

Ensuite, effectue une requête **POST** :

```
POST http://localhost:5000/api/scrape
```

📌 **Important** :
Il se peut que la base de données prenne un petit moment à être prête. Si la requête échoue au début, réessaie jusqu'à ce que tu obtiennes dans la réponse :

```json
{
  "message": "Scraping terminé avec succès."
}
```

👉 Cela signifie que les données ont bien été insérées dans la base MySQL.

---

### 2. Accéder à l'application

Ouvre ton navigateur :

```
http://localhost:3000/
```

Tu verras l’interface React avec les données affichées.

---

## 📁 Structure du projet

```
smart-scraper-groupe1/
│
├── backend/          # Code Flask
├── frontend/         # Code React
├── database/         # init.sql pour la BDD
├── docker-compose.yml
└── README.md
```

---

## ✅ À venir

* Filtrage avancé des données (dates, régions…)
* Export CSV
* Authentification

---

## 🧑‍💻 Auteurs

Projet réalisé par le **Groupe 1** — Mastere EEDSI

Encadré dans le cadre du cours de scraping web.



