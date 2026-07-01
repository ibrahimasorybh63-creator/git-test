
CREATE DATABASE geschool;
use geschool
CREATE table eleves(
    matricule int PRIMARY KEY ,
    prenom VARCHAR(30),
    nom VARCHAR(30),
    classe_id int,
    adresse VARCHAR(30),
    FOREIGN KEY (classe_id) REFERENCES classes(id)
);
CREATE table classes (
    id int PRIMARY key AUTO_INCREMENT,
    libelle VARCHAR(30),
    salle int UNIQUE,
    capacite int
);
CREATE table notes (
    id int PRIMARY KEY,
    valeur int ,
    eleve_id int,
    matiere_id int ,
    FOREIGN KEY (eleve_id) REFERENCES eleves(matricule) ,
    FOREIGN KEY  (matiere_id) REFERENCES matieres(id)
);
CREATE table matieres(
    id int PRIMARY KEY,
    nom VARCHAR(30),
    coef int ,
    classe_id int,
    FOREIGN KEY (classe_id) REFERENCES classes(id)
);
ALTER TABLE notes add appreciation VARCHAR(10);
ALTER TABLE classes MODIFY salle VARCHAR(30);
ALTER TABLE matieres CHANGE coef coefficient int;
/* table classes */
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Informatique A', 101, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Informatique B', 102, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Informatique A', 103, 35);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Informatique B', 104, 35);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Informatique A', 105, 40);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Informatique B', 106, 40);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Mathématiques A', 107, 25);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Mathématiques B', 108, 25);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Mathématiques A', 109, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Mathématiques B', 110, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Mathématiques A', 111, 35);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Mathématiques B', 112, 35);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Physique A', 113, 28);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Physique B', 114, 28);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Physique A', 115, 32);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Physique B', 116, 32);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Physique A', 117, 36);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Physique B', 118, 36);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Chimie A', 119, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Chimie B', 120, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Chimie A', 121, 34);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Chimie B', 122, 34);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Chimie A', 123, 38);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Chimie B', 124, 38);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Biologie A', 125, 30);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Biologie A', 126, 35);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L3 Biologie A', 127, 40);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L1 Réseaux', 128, 25);
INSERT INTO Classes(libelle,salle,capacite) VALUES ('L2 Réseaux', 129, 30);
/* table eleves */
INSERT INTO Eleves VALUES (1001, 'Ibrahima', 'Bah', 1, 'Conakry');
INSERT INTO Eleves VALUES (1002, 'Mamadou', 'Diallo', 2, 'Kindia');
INSERT INTO Eleves VALUES (1003, 'Fatoumata', 'Camara', 3, 'Labé');
INSERT INTO Eleves VALUES (1004, 'Alpha', 'Barry', 4, 'Mamou');
INSERT INTO Eleves VALUES (1005, 'Aissatou', 'Sow', 5, 'Kankan');
INSERT INTO Eleves VALUES (1006, 'Moussa', 'Balde', 6, 'Boké');
INSERT INTO Eleves VALUES (1007, 'Mariama', 'Sylla', 7, 'Coyah');
INSERT INTO Eleves VALUES (1008, 'Oumar', 'Keita', 8, 'Dubréka');
INSERT INTO Eleves VALUES (1009, 'Kadiatou', 'Bangoura', 9, 'Faranah');
INSERT INTO Eleves VALUES (1010, 'Saliou', 'Touré', 10, 'Nzérékoré');
INSERT INTO Eleves VALUES (1011, 'Nene', 'Condé', 11, 'Conakry');
INSERT INTO Eleves VALUES (1012, 'Abdoulaye', 'Cissé', 12, 'Kindia');
INSERT INTO Eleves VALUES (1013, 'Hawa', 'Diallo', 13, 'Labé');
INSERT INTO Eleves VALUES (1014, 'Mohamed', 'Bah', 14, 'Mamou');
INSERT INTO Eleves VALUES (1015, 'Binta', 'Camara', 15, 'Kankan');
INSERT INTO Eleves VALUES (1016, 'Sekou', 'Barry', 16, 'Boké');
INSERT INTO Eleves VALUES (1017, 'Aminata', 'Sow', 17, 'Coyah');
INSERT INTO Eleves VALUES (1018, 'Fode', 'Balde', 18, 'Dubréka');
INSERT INTO Eleves VALUES (1019, 'Ramatoulaye', 'Sylla', 19, 'Faranah');
INSERT INTO Eleves VALUES (1020, 'Yaya', 'Keita', 20, 'Nzérékoré');
INSERT INTO Eleves VALUES (1021, 'Mory', 'Bangoura', 21, 'Conakry');
INSERT INTO Eleves VALUES (1022, 'Hadja', 'Touré', 22, 'Kindia');
INSERT INTO Eleves VALUES (1023, 'Tidiane', 'Condé', 23, 'Labé');
INSERT INTO Eleves VALUES (1024, 'Assetou', 'Cissé', 24, 'Mamou');
INSERT INTO Eleves VALUES (1025, 'Souleymane', 'Diallo', 25, 'Kankan');
INSERT INTO Eleves VALUES (1026, 'Maimouna', 'Bah', 26, 'Boké');
INSERT INTO Eleves VALUES (1027, 'Ousmane', 'Camara', 27, 'Coyah');
INSERT INTO Eleves VALUES (1028, 'Korka', 'Barry', 28, 'Dubréka');
INSERT INTO Eleves VALUES (1029, 'Aicha', 'Sow', 29, 'Faranah');
/*table matieres*/
INSERT INTO Matieres VALUES (1, 'Algorithmique', 4, 1);
INSERT INTO Matieres VALUES (2, 'Programmation Python', 5, 2);
INSERT INTO Matieres VALUES (3, 'Bases de Données', 4, 3);
INSERT INTO Matieres VALUES (4, 'Systèmes d''Exploitation', 3, 4);
INSERT INTO Matieres VALUES (5, 'Réseaux Informatiques', 4, 5);
INSERT INTO Matieres VALUES (6, 'Développement Web', 3, 6);
INSERT INTO Matieres VALUES (7, 'Analyse Mathématique', 5, 7);
INSERT INTO Matieres VALUES (8, 'Algèbre Linéaire', 4, 8);
INSERT INTO Matieres VALUES (9, 'Probabilités', 3, 9);
INSERT INTO Matieres VALUES (10, 'Statistiques', 3, 10);
INSERT INTO Matieres VALUES (11, 'Calcul Différentiel', 5, 11);
INSERT INTO Matieres VALUES (12, 'Calcul Intégral', 5, 12);
INSERT INTO Matieres VALUES (13, 'Mécanique', 4, 13);
INSERT INTO Matieres VALUES (14, 'Électricité', 4, 14);
INSERT INTO Matieres VALUES (15, 'Thermodynamique', 5, 15);
INSERT INTO Matieres VALUES (16, 'Optique', 3, 16);
INSERT INTO Matieres VALUES (17, 'Physique Quantique', 5, 17);
INSERT INTO Matieres VALUES (18, 'Physique Nucléaire', 4, 18);
INSERT INTO Matieres VALUES (19, 'Chimie Générale', 4, 19);
INSERT INTO Matieres VALUES (20, 'Chimie Organique', 5, 20);
INSERT INTO Matieres VALUES (21, 'Chimie Minérale', 4, 21);
INSERT INTO Matieres VALUES (22, 'Biochimie', 5, 22);
INSERT INTO Matieres VALUES (23, 'Microbiologie', 4, 23);
INSERT INTO Matieres VALUES (24, 'Génétique', 5, 24);
INSERT INTO Matieres VALUES (25, 'Biologie Cellulaire', 4, 25);
INSERT INTO Matieres VALUES (26, 'Écologie', 3, 26);
INSERT INTO Matieres VALUES (27, 'Administration Réseau', 4, 27);
INSERT INTO Matieres VALUES (28, 'Sécurité Informatique', 5, 28);
INSERT INTO Matieres VALUES (29, 'Architecture des Réseaux', 4, 29);
/* table notes */
INSERT INTO Notes VALUES (1, 15, 1001, 1, 'Bien');
INSERT INTO Notes VALUES (2, 18, 1002, 2, 'Très Bien');
INSERT INTO Notes VALUES (3, 12, 1003, 3, 'Assez Bien');
INSERT INTO Notes VALUES (4, 10, 1004, 4, 'Passable');
INSERT INTO Notes VALUES (5, 17, 1005, 5, 'Très Bien');
INSERT INTO Notes VALUES (6, 14, 1006, 6, 'Bien');
INSERT INTO Notes VALUES (7, 9, 1007, 7, 'Faible');
INSERT INTO Notes VALUES (8, 16, 1008, 8, 'Bien');
INSERT INTO Notes VALUES (9, 13, 1009, 9, 'Assez Bien');
INSERT INTO Notes VALUES (10, 19, 1010, 10, 'Excellent');
INSERT INTO Notes VALUES (11, 11, 1011, 11, 'Passable');
INSERT INTO Notes VALUES (12, 15, 1012, 12, 'Bien');
INSERT INTO Notes VALUES (13, 8, 1013, 13, 'Faible');
INSERT INTO Notes VALUES (14, 17, 1014, 14, 'Très Bien');
INSERT INTO Notes VALUES (15, 20, 1015, 15, 'Excellent');
INSERT INTO Notes VALUES (16, 12, 1016, 16, 'Assez Bien');
INSERT INTO Notes VALUES (17, 14, 1017, 17, 'Bien');
INSERT INTO Notes VALUES (18, 10, 1018, 18, 'Passable');
INSERT INTO Notes VALUES (19, 16, 1019, 19, 'Bien');
INSERT INTO Notes VALUES (20, 18, 1020, 20, 'Très Bien');
INSERT INTO Notes VALUES (21, 7, 1021, 21, 'Faible');
INSERT INTO Notes VALUES (22, 13, 1022, 22, 'Assez Bien');
INSERT INTO Notes VALUES (23, 15, 1023, 23, 'Bien');
INSERT INTO Notes VALUES (24, 11, 1024, 24, 'Passable');
INSERT INTO Notes VALUES (25, 17, 1025, 25, 'Très Bien');
INSERT INTO Notes VALUES (26, 9, 1026, 26, 'Faible');
INSERT INTO Notes VALUES (27, 14, 1027, 27, 'Bien');
INSERT INTO Notes VALUES (28, 18, 1028, 28, 'Très Bien');
INSERT INTO Notes VALUES (29, 20, 1029, 29, 'Excellent');
/* affichage */
SELECT e.prenom,e.nom,c.libelle
FROM eleves as e
JOIN classes as c  ON e.classe_id = c.id 
ORDER BY c.libelle;            
select * FROM classes;
select m.nom,c.libelle
from matieres as m
JOIN classes as c on m.id = c.id 
ORDER BY libelle;
select * from matieres;
select * from notes;
UPDATE eleves set prenom="Ibrahima sory" WHERE matricule = '1001';
/* pas de coefficient 2 pour moi de base */
UPDATE matieres set coefficient = 2 WHERE coefficient = 3;
/* j'ai sauté l'avant derniere question*/
DROP TABLE notes;
/* maintenant l'avant derniere */
DELETE FROM eleves WHERE classe_id = 3;
DELETE FROM matieres WHERE classe_id = 3;
DELETE FROM classes WHERE id = 3;
