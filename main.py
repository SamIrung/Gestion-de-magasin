from article import *
from ventes import *
from mise_en_forme import *

def menu_principal():
    """
    menu principal qui affiche les fonctonnaliés principales
    """
    clear()
    blanc()
    position(7,70)
    print("==== GESTION DE MAGASIN ====")
    bleu()
    position(9,75)
    print("-"*20)
    position(10,75)
    print("1. Ajouter un produit")
    position(11,75)
    print("2. Afficher les produits")
    position(12,75)
    print("3. Rechercher un produit")
    position(13,75)
    print("4. Supprimer un produit")
    position(14,75)
    print("5. Enregistrer la vente")
    position(15,75)
    print("6. Afficher les ventes")
    position(16,75)
    print("7. Ventes par client")
    position(17,75)
    print("8. Générer rapport de ventes")
    position(18,75)
    print("9. Charger les données")
    position(19,75)
    print("10. Quitter")
    position(20,75)
    print("-"*20)
    jaune()
    position(21,75)
    return input(">> ")

def main():
    """
    fonction principale
    """
    while True:
        choix = menu_principal()
        if os.path.exists("produits.json"):
            pass
        else:
            donnedebut()
            print(f"le fichier n'est pas trouvé, donc on vous crée le fichier POUR LE PRODUIT automatiquement")
            pause()
        if os.path.exists("fichiervente.json"):
            pass
        else:
            donnedebutvente()
            print(f"le fichier n'est pas trouvé, donc on vous crée le fichier POUR LA VENTTE automatiquement")
            pause()            
        if choix == '1':
            #interface_ajout_produit()
            ajout_article(donne_produit())
        elif choix == '2':
            #interface_affichage_produits()
           afficher_article()
        elif choix == '3':
            #interface_recherche_produit()
            echangeverifier()
        elif choix == '4':
            #interface pour supprimer un produit()
            supprimer_produit() 
        elif choix == '5':
            #interface_enregistrement_vente()
            charger_historique_ventes()
            ajouter_vente()
        elif choix == '6':
            #interface_affichage_ventes()
            lister_ventes()
        elif choix == '7':
            #interface_ventes_par_client()
            client()





        elif choix == '8':
            #generer_rapport_ventes()
            rapport_vente()
            rap_csv()
            break
        elif choix == '9':
            #charger_donnees()
            print("charger_donnees")
        elif choix == '10':
            break
        else:
            rouge()
            position(22,75)
            print("Choix invalide, veuillez réessayer.")
            pause()

if __name__ == "__main__":
    main()
