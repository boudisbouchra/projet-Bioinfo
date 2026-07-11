# Analyse de Séquences d'ADN - Bactériophage T4

## Description et documentation du jeu de données (Metadata)

Ce projet implémente un flux de travail reproductible en Python pour analyser des fragments de gènes issus du génome officiel du Bactériophage T4.

- **Nom du projet :** Analyse de la composition nucléotidique et du taux de GC dans des séquences génomiques
- **Auteur :** Bouchra Boudis
- **Date :** Juillet 2026
- **Origine de l'échantillon (Sample origin) :** Les séquences analysées proviennent de la base de données officielle de la **NCBI** (National Center for Biotechnology Information).
- **Numéro d'accession NCBI :** `NC_000866`
- **Logiciels & Versions :** Python 3 (Spyder), Pandas (Analyse de données), Git / GitHub (Version contrôle).
- **Version du projet :** v1.0.0
- **Licence :** Open Source (MIT License)
### Format de fichier identifié
Le format retenu pour stocker le jeu de données est le **CSV (`.csv`)**. Ce format textuel est idéal pour garantir la légèreté de l'analyse, l'interopérabilité, et une manipulation performante sous Python avec la bibliothèque
Pandas.
## Résultats de l'Analyse
Le script calcule automatiquement le taux de GC (%) pour chaque fragment d'ADN. Voici les résultats obtenus :

| ID Séquence | Organisme | Taux de GC (%) |
| :--- | :--- | :--- |
| **seq_01** | Bactériophage T4 | 42.86 % |
| **seq_02** | Bactériophage T4 | 37.14 % |
| **seq_03** | Bactériophage T4 | 17.14 % |
| **seq_04** | Bactériophage T4 | 37.14 % |

**Moyenne globale :** ~33.57 %, ce qui est parfaitement cohérent avec la réalité biologique du virus (~34 %).)
