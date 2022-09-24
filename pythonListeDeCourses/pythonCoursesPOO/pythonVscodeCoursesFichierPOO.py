'''Récupérer le projet courses et faire en sorte que quand l'utilisateur choisisse de quitter avec
l'option 5, qu'il y ai un enregistrement sur dans un fichier'''

import os
import sys
import json

# from pythonVscodeCoursesFichier import CUR_DIR, LISTE_PATH, MENU_CHOICE, PANIER

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "listePOO.json")

PANIER = []
MENU_CHOICE = ["1", "2", "3", "4", "5"]
MENU =''' Voici 5 options :
1 : ajouter un élément au panier
2 : supprimer un élément du panier
3 : voir le panier
4 : vider le panier
5 : exit
Faites votre choix parmi ces 5 propositions'''

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        PANIER = json.load(f)
else:
    PANIER = [] 

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICE:
        print("Veuillez faire un choix valide !")
        continue
    if user_choice == "1":
        item = input("Quel élément voulez vous ajouter ?")
        PANIER.append(item)
        print(f"{item} a bien été ajouté au panier")
    elif user_choice == "2":
        item = input("Quel élément voulez vous enlever ?")
        if item in PANIER:
            PANIER.remove(item)
            print(f"{item} a bien été enlevé du panier")
        else:
            print(f"{item} n'est  pas présent dans le panier !")
    elif user_choice == "3":
        if PANIER:
            for i, capuchi in enumerate(PANIER, 1):
                print(f" {i}. {capuchi} ")
        else:
            print("Votre panier est vide")
    elif user_choice == "4":
        if PANIER == []:
            print("Votre panier est déjà vide")
        else:
            PANIER.clear()
            print("Votre panier a bien été vidé")
    elif user_choice == "5":
        while True:
            confirmation = input("Etes vous sur de vouloir quitter ? o/n")
            if confirmation == "o":
                with open(LISTE_PATH, "w") as f:
                    json.dump(PANIER, f, indent=4)
                print("Bonne journée, à bientôt")
                sys.exit()
            elif confirmation == "n":
                break
            elif confirmation != "o" or confirmation != "n":
                print("Votre réponse n'est pas valide !")
                continue
    print("-"*50)


