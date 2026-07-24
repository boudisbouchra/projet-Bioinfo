import pandas as pd

class AnalyseurADN:
    # Le code génétique partagé par toutes les instances
    CODE_GENETIQUE = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
    }

    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier
        self.df = None

    def charger_donnees(self):
        """Charge le fichier CSV."""
        self.df = pd.read_csv(self.chemin_fichier)
        print("Données chargées avec succès.")

    def calculer_taux_gc(self):
        """Calcule le taux de GC (%)."""
        if self.df is None:
            return
        self.df['taux_gc'] = self.df['sequence'].apply(
            lambda seq: round(((seq.count('G') + seq.count('C')) / len(seq)) * 100, 2)
        )

    def traduire_en_proteine(self, sequence):
        """Prend une séquence d'ADN et renvoie la chaîne d'acides aminés."""
        proteine = ""
        # On avance de 3 en 3 caractères
        for i in range(0, len(sequence) - 2, 3):
            codon = sequence[i:i+3].upper()
            acide_amine = self.CODE_GENETIQUE.get(codon, "?") # "?" si le codon est inconnu
            if acide_amine == "_":  # Si c'est un codon Stop, on arrête la traduction
                break
            proteine += acide_amine
        return proteine

    def traduire_toutes_les_sequences(self):
        """Applique la traduction à tout le DataFrame."""
        if self.df is None:
            print("Chargez les données d'abord.")
            return
        
        self.df['proteine'] = self.df['sequence'].apply(self.traduire_en_proteine)
        print("Traduction des séquences en protéines terminée !")

    def afficher_resultats(self):
        """Affiche le tableau final."""
        if self.df is not None:
            print("\n------ Résultats de l'analyse ------")
            # On affiche l'ID, le taux de GC et la protéine générée
            print(self.df[['id_sequence', 'taux_gc', 'proteine']])
        else:
            print("Aucun résultat à afficher.")

# ==========================================
# ==========================================
if __name__ == "__main__":
    analyseur = AnalyseurADN("sequences_adn.csv")
    analyseur.charger_donnees()
    analyseur.calculer_taux_gc()
    analyseur.traduire_toutes_les_sequences()
    analyseur.afficher_resultats()