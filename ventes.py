import json
import csv
from mise_en_forme import *
from article import *
from datetime import date



fichiervente="fichiervente.json"
rapport="rapport.json"
rapcsv="rapcsv.csv"

#LIB
import json
from datetime import datetime

# Initialisation de la liste des ventes
ventes_liste = []

# Fonction pour générer un nouvel ID unique
def generer_nouveau_id():
    try:
        with open('fichiervente.json', 'r') as fichier:
            historique = json.load(fichier)
        if historique:
            derniers_id = [vente['id'] for vente in historique]
            nouveau_id = max(derniers_id) + 1
            return nouveau_id
        else:
            return 1
    except FileNotFoundError:
        return 1

# Fonction pour vérifier si un produit existe dans l'inventaire
def verifier_produit(nom_produit):
    try:
        with open("produits.json", "r") as f:
            produits = json.load(f)
        for produit in produits:
            if nom_produit== produit["nom_produit"]:
                return produit
    except FileNotFoundError:
        print("Erreur : le fichier 'produits.json' n'a pas été trouvé.")
        pause()
    return None

# Fonction pour mettre à jour le stock d'un produit
def mettre_a_jour_stock(nom_produit, quantite_vendue):
    try:
        with open("produits.json", 'r') as f:
            produits = json.load(f)
        for produit in produits:
            if produit["nom_produit"].lower() == nom_produit.lower():
                produit["quantite"] -= quantite_vendue
                break
        with open("produits.json", 'w') as f:
            json.dump(produits, f, indent=2)
    except FileNotFoundError:
        print("Erreur : le fichier 'produits.json' n'a pas été trouvé.")
        pause()

# Fonction pour ajouter une nouvelle vente
def ajouter_vente():
    while True:
        produit_nom = input("Entrez le nom du produit : ")
        produit = verifier_produit(produit_nom)
        if produit:
            while True:
                try:
                    quantite_vendue = int(input("Entrez la quantité vendue : "))
                    if produit["quantite"] >= quantite_vendue:
                        client_nom = input("Entrez le nom du client : ")
                        nouveau_id = generer_nouveau_id()
                        date_actuelle = date.today().strftime("%d-%m-%Y")
                        prix_total = produit["prix"] * quantite_vendue
                        nouvelle_vente = {
                            'id': nouveau_id,
                            'client': client_nom,
                            'produit': produit_nom,
                            'quantite': quantite_vendue,
                            'prix': prix_total,
                            'date': date_actuelle
                        }
                        ventes_liste.append(nouvelle_vente)
                        mettre_a_jour_stock(produit_nom, quantite_vendue)

                        with open('fichiervente.json', 'w') as fichier:
                            json.dump(ventes_liste, fichier, indent=2)

                        print("Vente ajoutée avec succès.")
                        pause()
                        filtre_par_date()
                        break
                    else:
                        print("Quantité insuffisante en stock.")
                        pause()
                except ValueError:
                    print("Erreur : la quantité doit être un nombre entier. Veuillez réessayer.")
                    pause()
            break
        else:
            print(f"Erreur : le produit '{produit_nom}' n'existe pas. Veuillez réessayer.")
            pause()

# Fonction pour afficher toutes les ventes
def lister_ventes():
    charger_historique_ventes()
    for vente in ventes_liste:
        print(vente)
        pause()

# Fonction pour charger l'historique des ventes
def charger_historique_ventes():
    global ventes_liste
    try:
        with open('fichiervente.json', 'r') as fichier:
            ventes_liste = json.load(fichier)
    except FileNotFoundError:
        ventes_liste = []




#SPI

def compter_clients(nomClient):
    try:
        with open(fichiervente, 'r') as f:
            clients_data = json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {fichiervente} n'existe pas.")
        return None

    count = 0
    for client in clients_data:
        if client.get("client") == nomClient:
            count += 1

    if count > 0:
        print(f"Le client le nom '{nomClient}' est passé {count} fois chez nous.")
        pause()
    else:
        print(f"Client avec  le nom '{nomClient}' non trouvé.")
        pause()
        
def validerNomAr(nomArt):
    """
    controle de saisi
    """
    while nomArt =="" or not nomArt.isalpha():
        nomArt = input("erreur! ressayer : ")
    return nomArt

def client():
    nomClient = input("Entrez le nom du client à rechercher : ")
    nomClient=validerNomAr(nomClient)
    compter_clients(nomClient)


#JO
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

        

#SAM

def rapport_vente():
    with open(fichiervente, "r") as f:
        vente=json.load(f)
    with open(rapport, "w") as db:
        json.dump(vente, db, indent=2)
    print(f"le rapport de ventes est enregistrer dans le fichier '{rapport}'")
    pause()

def rap_csv():
    with open(rapport, "r") as f:
        vente=json.load(f)
        trans=vente[0].keys()

    with open(rapcsv, "w", newline="") as db:
        writer = csv.DictWriter(db, fieldnames=trans)
        writer.writeheader()
        for row in vente:
            writer.writerow(row)
            print("ok")
    jaune()
    print(f"le rapport de ventes est enregistrer dans le fichier excel '{rapcsv}'")
    pause()



def donnedebutvente():
    """
    ecrire dans le fichier en premiere position si le fichier est vide
    """
    prod=[]
    produitdeb =   {
    "id": 0,
    "client": "V",
    "produit": "JE",
    "quantite": 0,
    "prix": 0,
    "date": "13-07-2024"
  }
    prod.append(produitdeb)
    with open(fichiervente, "w") as f:
        json.dump(prod, f, indent=2)



