import json
from mise_en_forme import *
import sys
import os

produits = []
fichier="produits.json"
Id=1
def charger_donne():
    """
    charger les donnes du fichier JSON produits.json
    """
    try:
        with open(fichier, "r") as f:
            return json.load(f)#charger le fichier
    #fichier non trouvé
    except FileNotFoundError:
        print(f"le fichier n'est pas trouvé, donc on vous crée le fichier '{fichier}' automatiquement")
        pause()
        donnedebut()
    #fichier vide
    except json.decoder.JSONDecodeError:
        donnedebut()

#ID incremente
def validerId():
    """
    incrementtation automatique de l'ID
    """
    try:
        trier()
        produits=charger_donne()
        if produits:
            for i in produits:   
                dernier=i["ID_article"]#on recupere la derniere valeur de l'ID
                if dernier==None:
                    None==1
                    dernier=1                    
            Id=int(dernier)+1
            return Id
        else:
            print("il n'ya rien dans le fichier")
            donnedebut()
    except KeyError:
        print("erreur!")
    except FileNotFoundError:
        print("le fichier n'est pas trouvé")
        Id=1
#controle de saisi
def validerNomArt(nomArt):
    """
    controle de saisi
    """
    while nomArt =="" or not nomArt.isalpha():
        rouge()
        position(11,75)
        nomArt = input("erreur! ressayer : ")
    return nomArt
#controle de saisi
def validerprixArt(prixArt):
    """
    controle de saisi
    """
    while prixArt == "" or not prixArt.isdigit() or int(prixArt) < 1:
        rouge()
        position(13,75)
        prixArt =input("erreur! ressayer :  ")
    return prixArt
#controle de saisi
def validerqteArt(qteArt):
    """
    controle de saisi
    """
    while  qteArt == "" or not qteArt.isdigit() or int(qteArt) < 1:
        rouge()
        position(15,75)
        qteArt = input("erreur! ressayer :  ")
    return qteArt

#obtenir les donnees sur l'article
def donne_produit():
    """
    les données sur les produits
    """
    Id=1
    Id=validerId()
    clear()
    blanc()
    position(8,75)
    print("++++ Ajouter un produit ++++")
    bleu()
    position(10,75)
    nomArt = input("saisir le nom de l'article: ")
    nomArt=validerNomArt(nomArt)
    bleu()
    position(12,75)
    prixArt =input("saisir le prix de l'article : ")
    prixArt=validerprixArt(prixArt)
    prixArt=int(prixArt)
    bleu()
    position(14,75)
    qteArt = input("saisir le quantite de l'article : ")
    qteArt=validerqteArt(qteArt)
    qteArt=int(qteArt)
    return  [Id,nomArt,prixArt,qteArt]
#ajouter les articles dans le tableau
def ajout_article(donneArt):
    """
    ajouter un produit dans le fichier
    """
    nouveau_produit = {
        "ID_article":donneArt[0],
        "nom_produit":donneArt[1],
        "prix":donneArt[2],
        "quantite":donneArt[3]
        }
    #ajouter les produits a la liste produits
    produits.append(nouveau_produit)
    enregistrerData(nouveau_produit)
    delDoublons()
    trier()

    clear()
    jaune()
    position(14,50)
    print("*"*30)
    vert()
    position(16,50)
    print(">  Article ajouté  <")
    jaune()
    position(18,50)
    print("*"*30)
    pause()
            
#afficher les articles qui sont dans le fichier database.json
def afficher_article():
    """
    afficher les produits qui sont dans le fichier
    """
    try:
        produits = charger_donne()
        clear()
        blanc()
        position(2,10)
        print("++++++++++++++++++++ Produits +++++++++++++++++++")
        x=4
        position(x,50)
        jaune()
        print("*"*80)
        for art in produits:
            vert()
            x+=1
            print(art)
    except json.decoder.JSONDecodeError as e:
        print("Erreur de decodage JSON: ",e)
    except TypeError:
        print("le fichier est vide")
    jaune()
    print("*"*80)
    pause()  
#enregistrer les articles dans le fichier database.json
def enregistrerData(newArt):
    """
    enregistrer les donnees dans le fichier
    """
    try:
        produits = charger_donne()
        if produits:
            produits.append(newArt)
        else:
            print("le ficher est vide")
            donnedebut()
    except json.decoder.JSONDecodeError as e:
        print("Erreur de deodage JSON: ",e)
    with open(fichier, "w") as db:
        json.dump(produits, db, indent=2)

#recherche par le nom
def rechercheNom(nomA):
    """
    chercher nom
    """
    try:
        produits = charger_donne()
        for nom in produits:
            if nomA==nom["nom_produit"]:
                return True
        return False
    except TypeError:
        print("le fichier est vide")
#faire recherche par nom
def chercherparnom():
    """
    recherche par le nom
    """
    clear()
    blanc()
    position(8,80)
    print("++++ le nom ++++")
    bleu()
    position(10,75)
    nomA=input("Entrez le nom de larticle a rechercher : ")
    nomA=validerNomArt(nomA)
    resultat=rechercheNom(nomA)
    clear()
    jaune()
    if resultat:
        position(14,50)
        print("*"*30)
        vert()
        position(16,50)
        print(f"le nom {nomA} existe")
        jaune()
        position(18,50)
        print("*"*30)
        pause()
    else:
        position(14,50)
        print("*"*30)
        vert()
        position(16,50)
        print(f"le nom {nomA} n'existe pas")
        jaune()
        position(18,50)
        print("*"*30)
        pause()
#recherche par l'ID
def rechercheId(IdA):
    """
    chercher ID
    """
    try:
        produits = charger_donne()
        for i in produits:
            if IdA==i["ID_article"]:
                return True
        return False
    except TypeError:
        print("le fichier est vide")
#faire recherche par ID
def chercherparid():
    """
    recherche par l'ID
    """
    clear()
    blanc()
    position(8,80)
    print("++++ l' ID ++++")
    bleu()
    position(10,75)
    IdA=input("Entrez l'ID de larticle a rechercher : ")
    IdA=validerprixArt(IdA)
    IdA=int(IdA)
    resultat=rechercheId(IdA)
    clear()
    jaune()
    if resultat:
        position(14,50)
        print("*"*30)
        vert()
        position(16,50)
        print(f"l'ID '{IdA}' existe")
        jaune()
        position(18,50)
        print("*"*30)
        pause()
    else:
        position(14,50)
        print("*"*30)
        vert()
        position(16,50)
        print(f"l'ID '{IdA}' n'existe pas")
        jaune()
        position(18,50)
        print("*"*30)
        pause()
#controle de saisi
def validerverification(verification):
    """
    controle de saisi
    """
    while verification == "" or not verification.isdigit() or int(verification) < 1 or  int(verification) > 2 :
        rouge()
        position(14,75)
        verification=input("erreur! ressayer : ")
    return verification
#rechercher
def echangeverifier():
    """
    faire la recherche  par rapport a l'ID ou le nom
    """
    clear()
    blanc()
    position(8,80)
    print("+++++ rechercher produit +++++")
    bleu()
    position(10,75)
    print("par quoi voulez vous faire la recherche:")
    position(11,80)
    print("1. le nom")
    position(12,80)
    print("2. l' ID")
    jaune()
    position(13,75)
    verification=input(">> ")
    verification=validerverification(verification)
    if int(verification)  ==  1:
        chercherparnom()
    elif int(verification) == 2:
        chercherparid()

#Supprimer les doublons
def delDoublons():
    """
    verificie si il y'a des doublons par rapport au nom et au prix 
    et si oui on supprime l'un et on additionne la quantité
    """ 
    try:
        produits = charger_donne()
        unique={}
        if produits:
            for el in produits:
                cle=el["nom_produit"],el["prix"]
                if cle in unique:
                    unique[cle]["quantite"] += el["quantite"]
                else:
                    unique[cle]=el
            with open(fichier, "w") as db:
                json.dump(list(unique.values()), db, indent=2)
        else:
            print("le fichier est vide")
            pause()
            donnedebut()
    except KeyError:
        print("doublons n'existe pas!")
#trie dans le fichier
def trier():
    """
    trie les données dans le fichier par rapport au ID d'une maniere croissante
    """ 
    try:
        produits = charger_donne()
        if produits:
            try:
                produits.sort(key=lambda item: item["ID_article"])
            except TypeError:
                print("erreur de type null")
        else:
            donnedebut()
    except KeyError:
        print("erreur!")
    except json.decoder.JSONDecodeError:
        donnedebut()
    with open(fichier, "w") as db:
        json.dump(produits, db, indent=2)

#validation aavant de supprimer
def pour_suppr(produits, nomA, nom):
    """
    verifie si l'utilisateur veut vraiment supprimer et afficher les resultat
    """
    clear()
    blanc()
    position(7,80)
    print("++++ Supprimer produit ++++")
    vert()
    position(9,75)
    print(f"voulez vous vraiment supprimé l'article {nomA}")
    position(10,80)
    print("1. Oui")
    position(11,80)
    print("2. non")
    jaune()
    position(12,75)
    rep=input(">> ")
    rep=validerprixArt(rep)
    while True:
        if rep=="1":
            produits.remove(nom)
            clear()
            jaune()
            position(14,50)
            print("*"*30)
            vert()
            position(16,50)
            print(f"L'article '{nomA}' a été supprimé.")
            jaune()
            position(18,50)
            print("*"*30)
            pause()
            break
        elif rep=="2":
            clear()
            jaune()
            position(14,50)
            print("*"*30)
            vert()
            position(16,50)
            print(f"Annuler!")
            jaune()
            position(18,50)
            print("*"*30)
            pause()
            break
        else:
            rouge()
            position(12,75)
            rep=input("erreur! réessayer (1. Oui,2. non>> ")
            rep=validerprixArt(rep)
            continue
#suppprimer produits
def supprimer_produit():
    """
    supprimer un produit dans le fichier
    """
    try:
        produits = charger_donne()
        clear()
        blanc()
        position(8,80)
        print("++++ Supprimer produit ++++")
        bleu()
        position(10,75)
        nomA=input("Entrez le nom de l'article à Supprimer : ")
        nomA=validerNomArt(nomA)
        for nom in produits:
            if nomA==nom["nom_produit"]:
                pour_suppr(produits, nomA, nom)
                break
        else:
            clear()
            jaune()
            position(14,50)
            print("*"*30)
            vert()
            position(16,50)
            print(f"L'article '{nomA}' n'a pas été trouvé.")
            jaune()
            position(18,50)
            print("*"*30)
            pause()
        # Écrire les modifications dans le fichier
        with open(fichier, 'w') as f:
            json.dump(produits, f, indent=2)
        trier()
    except FileNotFoundError:
        print(f"Le fichier '{database.json}' n'existe pas.")
    except TypeError:
        print("le fichier est vide")
        pause()

def donnedebut():
    """
    ecrire dans le fichier en premiere position si le fichier est vide
    """
    prod=[]
    produitdeb = {
    "ID_article": 0,
    "nom_produit": "P",
    "prix": 0,
    "quantite": 0
        }
    prod.append(produitdeb)
    with open(fichier, "w") as f:
        json.dump(prod, f, indent=2)
