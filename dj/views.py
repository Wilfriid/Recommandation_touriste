from django.shortcuts import render
import pandas as pd
import pickle

# Charger le modèle entraîné
with open('C:\\Users\\SIMPLON\\OneDrive\\Bureau\\voyage\\recommandation\\recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Charger le dataset
data = pd.read_csv('C:\\Users\\SIMPLON\\OneDrive\\Bureau\\voyage\\recommandation\\destinations.csv', names=[
    'Pays', 'Budget Moy./Jour (EUR)', 'Durée Moy. (jours)', 'Preferences', 'Activites',
    'Hotel 3*', 'Hotel 4*', 'Hotel 5*', 'Saison Propice', 'Budget Repas Simple (FCFA)'
])

# Vue de recommandation
def recommendation(request):
    if request.method == 'POST':
        budget_jour = float(request.POST.get('budget_jour'))
        duree_sejour = int(request.POST.get('duree_sejour'))
        preferences_voyage = request.POST.get('preferences_voyage').capitalize()
        activites_voyage = request.POST.get('activites_voyage').capitalize()
        hotel_etoiles = request.POST.get('hotel_etoiles').strip()
        saison_propice = request.POST.get('saison_propice').capitalize()  # Assurez-vous de la casse
        budget_repas_simple = float(request.POST.get('budget_repas_simple'))

        # Préparer les features pour la recommandation
        if hotel_etoiles == "Hotel 3*":
            hotel_field = 'Hotel 3*'
        elif hotel_etoiles == "Hotel 4*":
            hotel_field = 'Hotel 4*'
        elif hotel_etoiles == "Hotel 5*":
            hotel_field = 'Hotel 5*'
        else:
            hotel_field = None

        if hotel_field:
            input_features = [[budget_jour, duree_sejour, 0, 0, 0, budget_repas_simple]]
            if hotel_field == 'Hotel 3*':
                input_features[0][2] = budget_jour
            elif hotel_field == 'Hotel 4*':
                input_features[0][3] = budget_jour
            elif hotel_field == 'Hotel 5*':
                input_features[0][4] = budget_jour

            # Ajouter la saison propice comme critère de filtrage
            print(f"Saison Propice reçue: {saison_propice}")  # Débogage
            filtered_data = data[data['Saison Propice'] == saison_propice]

            # Faire une prédiction avec le modèle
            if not filtered_data.empty:
                try:
                    features_filtered = filtered_data[['Budget Moy./Jour (EUR)', 'Durée Moy. (jours)', 'Hotel 3*', 'Hotel 4*', 'Hotel 5*', 'Budget Repas Simple (FCFA)']]
                    model.fit(features_filtered)
                    distances, indices = model.kneighbors(input_features)

                    recommendations = []
                    for index in indices[0]:
                        recommendation = filtered_data.iloc[index]
                        recommendations.append({
                            'Pays': recommendation["Pays"],
                            'Budget': recommendation["Budget Moy./Jour (EUR)"],
                            'Duree': recommendation["Durée Moy. (jours)"],
                            'Preferences': recommendation["Preferences"],
                            'Activites': recommendation["Activites"],
                            'Hotel': recommendation[hotel_field],  # Afficher seulement l'hôtel choisi
                            'Budget_Repas_Simple': recommendation["Budget Repas Simple (FCFA)"],
                            'Saison_Propice': recommendation["Saison Propice"],  # Assurez-vous que le champ est inclus
                        })

                    return render(request, 'results.html', {'recommendations': recommendations, 'hotel_etoiles': hotel_etoiles})
                except KeyError as e:
                    return render(request, 'home.html', {'error': f"Erreur: {e}"})

    return render(request, 'home.html')




