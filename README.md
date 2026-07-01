# git-test

Dépôt regroupant plusieurs projets pratiques réalisés dans le cadre de mon apprentissage de la programmation (Python, SQL, HTML/CSS/JS).

## 📂 Structure du dépôt

```
git-test/
├── rpg_game/            # Jeu de combat RPG en Python (projet principal)
├── calculatrice/        # Calculatrice Python + version web
├── gestionnaire_taches/ # Gestionnaire de tâches en terminal
├── mini_jeu/            # Prototype de mini-jeu de combat
├── sql/                 # Script SQL de gestion scolaire
└── site_web/            # Page web (HTML/CSS/JS)
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

## 🗄️ sql/ — Base de données Gestion scolaire
`geschool.sql`

Script SQL de création et manipulation d'une base de données pour la gestion d'un établissement scolaire (tables, contraintes, requêtes).

## 🌐 site_web/ — Page web
`index.html`, `script.js`, `style.css`

Page web front-end (HTML, CSS, JavaScript).

## 🎯 Objectif du dépôt

Ce dépôt regroupe des exercices et projets réalisés au fil de mon apprentissage. Le projet le plus abouti est le **jeu de combat RPG**.

## 👤 Auteur

**Bah Ibrahima Sory**
Étudiant en Prépa Ingénieur (L1) à BEM Conakry, Guinée
📧 ibrahimasorybh63@gmail.com
