# projet-Bioinfo

## Description et documentation du jeu de données (Metadata)

L'objectif de ce projet est de créer un flux de travail reproductible pour analyser des données génomiques légères.

- **Nom du projet :** Analyse de la composition nucléotidique et du taux de GC dans des séquences génomiques
- **Auteur :** Bouchra Boudis
- **Date :** Juillet 2026
- **Origine de l'échantillon (Sample origin) :** Séquences de fragments de gènes simulées à partir du génome du Bactériophage T4.
- **Logiciels & Versions :** Python 3 (Thonny IDE), Pandas (Analyse de données), Git / GitHub (Version contrôle).
- **Version du projet :** v1.0.0
- **Licence :** Open Source (MIT License)
### Format de fichier identifié
Le format retenu pour stocker le jeu de données est le **CSV (`.csv`)**. Ce format textuel est idéal pour garantir la légèreté de l'analyse, l'interopérabilité, et une manipulation performante sous Python avec la bibliothèque
Pandas.
Structure prévue pour le fichier `sequences_adn.csv` :
- `id_sequence` : Identifiant unique de la séquence d'ADN
- `organisme` : Nom de l'organisme d'origine
- `sequence` : Chaîne de caractères contenant la suite de nucléotides (A, T, C, G)
