import json

def compter_clients(fichier_json, nom_ou_id):
    try:
        # Ouvre le fichier JSON en mode lecture
        with open(fichier_json, 'r') as f:
            # Charge les données clients depuis le fichier
            clients_data = json.load(f)
    except FileNotFoundError:
        # Si le fichier n'existe pas, affiche un message d'erreur
        print(f"Le fichier {fichier_json} n'existe pas.")
        return None

    # Initialise un compteur pour le nombre de fois que le client est trouvé
    count = 0
    for client in clients_data:
        # Vérifie si l'ID ou le nom du client correspond à la recherche
        if client.get("id") == nom_ou_id or client.get("nom") == nom_ou_id:
            count += 1

    # Affiche le résultat en fonction du nombre de fois que le client est trouvé
    if count > 0:
        print(f"Le client avec l'ID ou le nom '{nom_ou_id}' est passé {count} fois chez nous.")
    else:
        print(f"Client avec l'ID ou le nom '{nom_ou_id}' non trouvé.")

# Exemple d'utilisation :
fichier_clients_json = "clients.json"
nom_ou_id_recherche = input("Entrez l'ID ou le nom du client à rechercher : ")
compter_clients(fichier_clients_json, nom_ou_id_recherche)
