from sqlalchemy import Column, Integer, String, ForeignKey, Year
from sqlalchemy.orm import relationship
from .BaseDeDonnee import BDD

class Enseignant(BDD):
    __tablename__ = 'enseignants'

    teacher_id = Column(Integer, primary_key=True, index=True)
    prenom = Column(String(50), nullable=False)
    nom = Column(String(50), nullable=False)
    numero_salle = Column(Integer, nullable=False)
    departement = Column(String(100))
    annee_obtention = Column(Year)
    email = Column(String(100))
    telephone = Column(String(15))
    numero_classe = Column(Integer, unique=True)  # Chaque enseignant a une seule classe

    # Relation avec la table Etudiants (One-to-Many)
    etudiants = relationship("Etudiant", back_populates="enseignant", cascade="all, delete-orphan")


class Etudiant(BDD):
    __tablename__ = 'etudiants'

    student_id = Column(Integer, primary_key=True, index=True)
    prenom = Column(String(50), nullable=False)
    nom = Column(String(50), nullable=False)
    numero_salle = Column(Integer, nullable=False)
    telephone = Column(String(15))
    email = Column(String(100))
    annee_obtention = Column(Year)
    numero_classe = Column(Integer, ForeignKey("enseignants.numero_classe"))  # Clé étrangère vers Enseignant

    # Relation avec la table Enseignants
    enseignant = relationship("Enseignant", back_populates="etudiants")