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