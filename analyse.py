import pandas as pd

# 1. Chargement du jeu de données
try:
    df = pd.read_csv("sequences_adn.csv")
    print("✅ Jeu de données chargé avec succès !")
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'sequences_adn.csv' est introuvable.")

# 2. Fonction pour calculer le taux de GC
def calculer_taux_gc(sequence):
    # Met la séquence en majuscules pour éviter les erreurs
    seq = sequence.upper()
    nb_g = seq.count('G')
    nb_c = seq.count('C')
    longueur = len(seq)
    
    if longueur == 0:
        return 0.0
    
    # Calcul du pourcentage
    return ((nb_g + nb_c) / longueur) * 100

# 3. Application de la fonction sur tout le Dataset
# On crée une nouvelle colonne appelée 'taux_gc'
df['taux_gc'] = df['sequence'].apply(calculer_taux_gc)

# 4. Affichage du résultat final
print("\n--- Résultats de l'analyse bioinformatique ---")
print(df[['id_sequence', 'organisme', 'taux_gc']])