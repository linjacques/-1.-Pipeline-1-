-- étape 1 :

--Créez une nouvelle base de données appelée "École". 
--Cette base de données 
--doit comporter deux tables : enseignants et élèves.--
CREATE DATABASE ecole;

--La table étudiants doit comporter des colonnes 
--student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe.
CREATE TABLE etudiants (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    telephone VARCHAR(15),
    email VARCHAR(100),
    annee_obtention YEAR,
    numero_classe INT
);

--La table enseignants  doit comporter des colonnes:
-- teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe
CREATE TABLE enseignants (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    departement VARCHAR(100),
    annee_obtention YEAR,
    email VARCHAR(100),
    telephone VARCHAR(15),
    numero_classe INT
);

-- Une fois les tables créées, insérez un étudiant nommé Mark Watney (student_id=1) dont le numéro de téléphone est 777-555-1234 et qui n'a pas d'adresse électronique. Il sera diplômé en 2035 et son numéro de classe est le 5.
INSERT INTO etudiants (student_id, prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
VALUES (1, 'Mark', 'Watney', 101, '777-555-1234', NULL, 2035, 5);

-- Insérez ensuite un enseignant nommé Jonas Salk (teacher_id = 1) dont le numéro de classe est 5 et qui fait partie du département de biologie. Ses coordonnées sont : jsalk@school.org et son numéro de téléphone est 777-555-4321.
INSERT INTO enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES (1, 'Jonas', 'Salk', 201, 'Biologie', NULL, 'jsalk@school.org', '777-555-4321', 5);

