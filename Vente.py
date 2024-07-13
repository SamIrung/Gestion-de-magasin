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
