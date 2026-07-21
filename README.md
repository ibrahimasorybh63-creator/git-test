# git-test

Dépôt regroupant plusieurs projets pratiques réalisés dans le cadre de mon apprentissage de la programmation (Python, SQL, HTML/CSS/JS).

## 📂 Structure du dépôt

```
git-test/
├── rpg_game/            # Jeu de combat RPG en Python (projet principal)
├── calculatrice/        # Calculatrice Python + version web
├── gestionnaire_taches/ # Gestionnaire de tâches en terminal
├── mini_jeu/            # Prototype de mini-jeu de combat
├── sql/                 # Gestionnaire de boutique (Python + SQLite + pandas)
└── site_web/            # Portfolio personnel (HTML/CSS/JS)
```

## ⚔️ rpg_game/ — Jeu de combat RPG (projet principal)
`rpg_project.py`, `player.py`, `assassin.py`, `barbare.py`, `chevalier.py`, `mage.py`, `combat_manager.py`

Jeu de combat 1v1 au tour par tour, jouable dans le terminal. Deux joueurs choisissent chacun une classe de combattant et s'affrontent jusqu'à ce que l'un des deux tombe à 0 PV.

**Classes jouables :**
| Classe | Style de jeu |
|---|---|
| **Assassin** | Faibles dégâts mais réguliers ; poison, double frappe et camouflage |
| **Barbare** | Dégâts très élevés, défense faible ; plus il perd de PV, plus il frappe fort (mode rage) |
| **Chevalier** | Faibles dégâts, mais peut se défendre, se soigner et contre-attaquer |
| **Mage** | Profil équilibré, dégâts élémentaires (feu, glace, foudre), vol de mana, armure magique temporaire |

Concepts mis en œuvre : héritage (`Player` → 4 sous-classes), polymorphisme (chaque classe redéfinit `subir_degats()`), gestion de cooldowns/mana, effets temporaires (poison, brûlure, froid), orchestration des tours via `CombatManager`.

**Lancer le jeu :**
```bash
cd rpg_game
python combat_manager.py
```

## 🧮 calculatrice/ — Calculatrice
`calculatrice.py`, `calculatrice.html`

Calculatrice en ligne de commande (addition, soustraction, multiplication, division, puissance, racine carrée), avec une version interface web.

```bash
cd calculatrice
python calculatrice.py
```

## 📝 gestionnaire_taches/ — Gestionnaire de tâches
`gestache.py`

Petit gestionnaire de tâches en terminal avec sauvegarde dans un fichier texte : ajouter, valider et supprimer des tâches.

```bash
cd gestionnaire_taches
python gestache.py
```

## 🎲 mini_jeu/ — Prototype de mini-jeu
`mini_jeu.py`

Premier prototype d'un jeu de combat 1v1 (attaque, attaque spéciale, soin) — version simplifiée ayant servi de base au projet RPG ci-dessus.

## 🗄️ sql/ — Gestionnaire de boutique (Python + SQLite)
`schema.sql`, `script.py`, `entite.py`, `main.py`

Application console de gestion d'une boutique (produits, clients, commandes), en Python et SQLite (module `sqlite3`), avec affichage des résultats via `pandas`.

**Structure :**
- `schema.sql` — définition des 4 tables (`clients`, `produits`, `commandes`, `details_comm`), avec clés étrangères et clé primaire composite pour la table de jonction `details_comm`
- `script.py` — initialise la base `boutique.db` à partir de `schema.sql` (à lancer une seule fois)
- `entite.py` — classes `Produit`, `Clients`, `Commandes` (CRUD complet, méthodes statiques pour les opérations sans état, jointure à 4 tables pour l'affichage d'une commande)
- `main.py` — menu console : gestion des produits, des clients, et des commandes (avec insertion en masse de produits par commande et validation des saisies)

**Concepts mis en œuvre :** connexion/curseur SQLite, requêtes paramétrées (`?`), clés étrangères (`PRAGMA foreign_keys`), jointures multi-tables, méthodes statiques vs méthodes d'instance, conversion de résultats SQL en DataFrame pandas.

**Lancer le projet :**
```bash
cd sql
python script.py   # initialise la base (une seule fois)
python main.py      # lance l'application
```

## 🌐 site_web/ — Portfolio personnel
`index.html`, `script.js`, `style.css`

Page one-page présentant mon parcours et mes projets (Bootstrap + JS), avec les sections Accueil, À propos, Projets, Compétences et Contact.

## 🎯 Objectif du dépôt

Ce dépôt regroupe des exercices et projets réalisés au fil de mon apprentissage. Le projet le plus abouti est le **jeu de combat RPG**.

## 👤 Auteur

**Bah Ibrahima Sory**
Étudiant en Prépa Ingénieur (L1) à BEM Conakry, Guinée
📧 ibrahimasorybh63@gmail.com
