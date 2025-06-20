from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gare(Base):
    __tablename__ = 'gares'
    id = Column(Integer, primary_key=True)
    nom_gare = Column(String(255), nullable=False)
    code_uic_complet = Column(String(20))
    code_postal = Column(String(10))
    segmentation_drg = Column(String(10))

    voyageurs = relationship("Voyageurs", back_populates="gare")


class Voyageurs(Base):
    __tablename__ = 'voyageurs'
    id = Column(Integer, primary_key=True)
    gare_id = Column(Integer, ForeignKey('gares.id'), nullable=False)
    annee = Column(Integer, nullable=False)
    total_voyageurs = Column(Integer)
    total_non_voyageurs = Column(Integer)

    gare = relationship("Gare", back_populates="voyageurs")
