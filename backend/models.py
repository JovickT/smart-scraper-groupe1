# api/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vigilance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departement = db.Column(db.String(50), nullable=False)
    phenomene = db.Column(db.String(100), nullable=False)
    niveau = db.Column(db.String(20), nullable=False)
    debut = db.Column(db.String(100), nullable=False)
    fin = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "departement": self.departement,
            "phenomene": self.phenomene,
            "niveau": self.niveau,
            "debut": self.debut,
            "fin": self.fin
        }
