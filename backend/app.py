# api/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, Vigilance
from config import Config
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/scrape', methods=['GET'])
def scrape_vigilance():
    url = 'https://vigilance.meteofrance.fr/fr/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemple d'extraction - À adapter à la structure HTML réelle
    alertes = []

    # ⚠️ La structure réelle de la page peut varier. Voici un exemple général :
    table = soup.find('table')  
    if not table:
        return jsonify({"error": "Tableau non trouvé"}), 500

    rows = table.find_all('tr')[1:]  
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 5:
            departement = cols[0].get_text(strip=True)
            phenomene = cols[1].get_text(strip=True)
            niveau = cols[2].get_text(strip=True)
            debut = cols[3].get_text(strip=True)
            fin = cols[4].get_text(strip=True)

            vigilance = Vigilance(
                departement=departement,
                phenomene=phenomene,
                niveau=niveau,
                debut=debut,
                fin=fin
            )
            db.session.add(vigilance)
            alertes.append(vigilance.to_dict())

    db.session.commit()
    return jsonify(alertes), 201

@app.route('/api/vigilances', methods=['GET'])
def get_all_vigilances():
    all_data = Vigilance.query.all()
    return jsonify([v.to_dict() for v in all_data])

if __name__ == '__main__':
    app.run(debug=True)