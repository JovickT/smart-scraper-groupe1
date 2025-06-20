import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from models import Base, Gare, Voyageurs

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

API_URL = "https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/frequentation-gares/records"
LIMIT = 100  # Limite maximale imposée par l'API

def fetch_data():
    all_data = []
    for offset in range(0, 200, LIMIT):  # Modifier la plage selon le besoin
        print(f"[INFO] Récupération données offset={offset}")
        response = requests.get(API_URL, params={"limit": LIMIT, "offset": offset})
        if response.status_code != 200:
            print(f"[ERREUR] API status {response.status_code}")
            break
        batch = response.json().get("results", [])
        all_data.extend(batch)
    return all_data

def run_scraper():
    Base.metadata.create_all(engine)
    session = Session()

    data = fetch_data()
    count_gares = 0
    count_voyageurs = 0

    for item in data:
        nom_gare = item.get("nom_gare")
        if not nom_gare:
            continue  # Donnée invalide, on ignore

        # Vérifie si la gare existe déjà
        gare = session.query(Gare).filter_by(nom_gare=nom_gare).first()
        if not gare:
            gare = Gare(
                nom_gare=nom_gare,
                code_uic_complet=item.get("code_uic_complet"),
                code_postal=item.get("code_postal"),
                segmentation_drg=item.get("segmentation_drg")
            )
            session.add(gare)
            session.flush()  # Nécessaire pour récupérer gare.id sans commit
            count_gares += 1

        # Ajoute les données de fréquentation pour les années disponibles
        for annee in range(2015, 2024):
            total_voy = item.get(f"total_voyageurs_{annee}") or item.get(f"totalvoyageurs{annee}")
            total_non_voy = item.get(f"total_voyageurs_non_voyageurs_{annee}")
            if total_voy is None and total_non_voy is None:
                continue  # Aucune donnée pour cette année

            voyageurs = Voyageurs(
                gare_id=gare.id,
                annee=annee,
                total_voyageurs=total_voy or 0,
                total_non_voyageurs=total_non_voy or 0
            )
            session.add(voyageurs)
            count_voyageurs += 1
    session.commit()
    print(f"[INFO] {count_gares} gares ajoutées, {count_voyageurs} enregistrements voyageurs insérés.")
