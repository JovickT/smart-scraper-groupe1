from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from scraper import run_scraper
from models import Gare, Voyageurs

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
CORS(app)

@app.route("/api/data", methods=["GET"])
def get_gares():
    nom_gare_param = request.args.get("nom_gare")

    query = db.session.query(Gare)
    if nom_gare_param:
        query = query.filter(Gare.nom_gare.ilike(f"%{nom_gare_param}%"))

    gares = query.all()

    result = []
    for gare in gares:
        voyageurs = [{
            "annee": v.annee,
            "total_voyageurs": v.total_voyageurs,
            "total_non_voyageurs": v.total_non_voyageurs
        } for v in gare.voyageurs]

        result.append({
            "id": gare.id,
            "nom_gare": gare.nom_gare,
            "code_uic_complet": gare.code_uic_complet,
            "code_postal": gare.code_postal,
            "segmentation_drg": gare.segmentation_drg,
            "voyageurs": voyageurs
        })

    return jsonify(result), 200

@app.route("/api/scrape", methods=["POST"])
def scrape_data():
    try:
        run_scraper()
        return jsonify({"message": "Scraping terminé avec succès."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/data/<filtre>/<valeur>", methods=["GET"])
def get_filtered_data(filtre, valeur):
    query = db.session.query(Gare).join(Gare.voyageurs)

    if filtre == "ville":
        query = query.filter(Gare.nom_gare.ilike(f"%{valeur}%"))
    elif filtre == "annee":
        try:
            annee = int(valeur)
            query = query.filter(Voyageurs.annee == annee)
        except ValueError:
            return jsonify({"error": "Année invalide"}), 400
    elif filtre == "code_postal":
        query = query.filter(Gare.code_postal == valeur)
    elif filtre == "segmentation":
        query = query.filter(Gare.segmentation_drg.ilike(valeur))
    else:
        return jsonify({"error": f"Filtre inconnu: {filtre}"}), 400

    gares = query.all()

    result = []
    for gare in gares:
        voyageurs_data = sorted([{
            "annee": v.annee,
            "total_voyageurs": v.total_voyageurs,
            "total_non_voyageurs": v.total_non_voyageurs
        } for v in gare.voyageurs if filtre != "annee" or v.annee == int(valeur)],
        key=lambda x: x["annee"])

        result.append({
            "id": gare.id,
            "nom_gare": gare.nom_gare,
            "code_uic_complet": gare.code_uic_complet,
            "code_postal": gare.code_postal,
            "segmentation_drg": gare.segmentation_drg,
            "voyageurs": voyageurs_data
        })

    return jsonify(result), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Ressource non trouvée"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erreur interne du serveur"}), 500

if __name__ == "__main__":
    app.run(debug=True)
