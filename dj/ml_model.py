import pandas as pd
import os

# Définir le chemin du fichier CSV
csv_path = 'C:\\Users\\SIMPLON\\OneDrive\\Bureau\\voyage\\recommandation\\destinations.csv'

# Vérifier si le répertoire existe, sinon le créer
output_dir = os.path.dirname(csv_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Création du dataset
data = {
    "Pays": ["Côte d'Ivoire", "Afrique du Sud", "Seychelles", "Comores", "Égypte", "Maroc", "Turquie", "Algérie", 
             "Botswana", "Sénégal", "Ghana", "Cap-Vert", "Kenya", "Zimbabwe", "Tunisie", "Madagascar", "Angola",
             "Namibie", "Nigeria", "Mali", "Ouganda", "Tanzanie", "Maurice", "Rwanda", "Ethiopie", 
             "Gabon", "Zambie", "Malawi", "Mozambique", "Burkina Faso", "Libye"],
    "Budget Moy./Jour (FCFA)": [45850, 52400, 98250, 32750, 39300, 45850, 52400, 32750, 65500, 39300, 32750, 45850, 58950, 52400, 39300, 45850, 52400,
                               52400, 45850, 39300, 32750, 45850, 65500, 39300, 32750, 58950, 39300, 32750, 26200, 39300, 45850],
    "Duree Moy. (jours)": [10, 14, 7, 7, 10, 10, 10, 7, 10, 10, 10, 10, 14, 10, 10, 10, 10,
                           10, 7, 7, 7, 10, 7, 7, 7, 10, 7, 7, 7, 7, 7],
    "Preferences": ["Plage", "Nature", "Plage", "Plage", "Culture", "Culture", "Culture", "Culture", 
                    "Nature", "Plage", "Culture", "Plage", "Nature", "Nature", "Plage", "Nature", "Nature",
                    "Nature", "Culture", "Culture", "Nature", "Nature", "Plage", "Nature", "Culture", 
                    "Nature", "Nature", "Nature", "Nature", "Culture", "Culture"],
    "Activites": ["Culture", "Aventure", "Détente", "Plongée", "Histoire", "Détente", "Histoire", "Histoire", 
                  "Safari", "Culture", "Plage", "Détente", "Safari", "Aventure", "Histoire", "Plongée", "Culture",
                  "Safari", "Histoire", "Histoire", "Safari", "Safari", "Détente", "Culture", "Histoire", 
                  "Safari", "Safari", "Nature", "Nature", "Histoire", "Histoire"],
    "Hotel 3* (FCFA)": [45850, 52400, 131000, 39300, 45850, 52400, 58950, 39300, 78600, 45850, 39300, 52400, 65500, 58950, 45850, 52400, 58950,
                 58950, 45850, 39300, 39300, 52400, 98250, 45850, 39300, 65500, 39300, 39300, 32750, 39300, 45850],
    "Hotel 4* (FCFA)": [78600, 98250, 196500, 65500, 78600, 85150, 91700, 72050, 131000, 78600, 72050, 85150, 111350, 98250, 78600, 85150, 98250,
                 98250, 78600, 72050, 72050, 85150, 163750, 78600, 72050, 111350, 72050, 72050, 58950, 72050, 78600],
    "Hotel 5* (FCFA)": [131000, 163750, 327500, 98250, 131000, 144100, 150650, 117900, 229250, 131000, 117900, 144100, 196500, 163750, 131000, 144100, 163750,
                 163750, 131000, 117900, 117900, 144100, 262000, 131000, 117900, 196500, 117900, 117900, 98250, 117900, 131000],
    "Saison Propice": ["Hiver", "Été", "Été", "Été", "Printemps", "Printemps", "Printemps", "Printemps",
                       "Hiver", "Hiver", "Hiver", "Hiver", "Printemps", "Printemps", "Printemps", "Été", "Été",
                       "Été", "Hiver", "Hiver", "Printemps", "Été", "Été", "Printemps", "Printemps",
                       "Été", "Hiver", "Été", "Été", "Hiver", "Printemps"],
    "Budget Repas Simple (FCFA)": [3275, 4585, 9825, 2620, 3275, 3930, 4585, 3275, 5240, 3275, 2620, 3930, 4585, 3930, 3275, 3930, 4585,
                                  4585, 3275, 2620, 2620, 3930, 6550, 3275, 2620, 5240, 3275, 2620, 1965, 3275, 3930]
}

df = pd.DataFrame(data)

# Sauvegarder le dataset en CSV
df.to_csv(csv_path, index=False)
