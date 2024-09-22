from .tables import BDD
from .BaseDeDonnee import SessionLocal, ConnexionBDD

# Étape 1 : Création des tables si elles n'existent pas déjà
BDD.metadata.create_all(bind=ConnexionBDD)

# Étape 2 : Connexion à la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Étape 3 : Extraction des données
def fetch_data():
    with ConnexionBDD.connect() as connection:
        sql_eleve = "SELECT * FROM eleves"
        session = connection.execute(sql_eleve)
        resultats_eleves = session.fetchall()
        
        sql_enseignant = "SELECT * FROM enseignants"
        session = connection.execute(sql_enseignant)
        resultats_enseignants = session.fetchall()

    # Affichage des résultats
    print("Contenu de la table élèves :")
    for eleve in resultats_eleves:
        print(eleve)
    
    print("\nContenu de la table enseignants :")
    for enseignant in resultats_enseignants:
        print(enseignant)

