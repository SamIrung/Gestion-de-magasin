
#filtrage des ventes par date.

from datetime import datetime
def filtre_par_date():
    # Chargement du fichier JSON
    with open(fichiervente, "r") as f:
        données_ventes = json.load(f)

    # Définition des dates de début et de fin du filtre
    date_debut = "01-01-2024"
    date_fin = "30-07-2024"
    date_debut = datetime.strptime(date_debut, "%d-%m-%Y")
    date_fin = datetime.strptime(date_fin, "%d-%m-%Y")

    # Filtrage des ventes par date
    ventes_filtrées = []
    for vente in données_ventes:
        date_vente = datetime.strptime(vente["date"], "%d-%m-%Y")
        if date_debut <= date_vente <= date_fin:
            ventes_filtrées.append(vente) 
    try:
        with open(fichiervente, "w") as db:
            json.dump(ventes_filtrées, db, indent=2)
            print(f"Données enregistrées dans '{fichier}'.")
    except IOError as e:
        print(f"Erreur lors de l'écriture dans le fichier '{fichier}': {e}")

