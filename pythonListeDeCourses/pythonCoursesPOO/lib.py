import logging
import os
import json

from constants import DATA_DIR


LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, nom):
        self.nom = nom


    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajoutez que des chaines de caractères !")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
            return False
        
        self.append(element)
        return True


    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        else:
            return False


    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    
    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True



if __name__ == "__main__":
    liste = Liste("courses")
    liste.ajouter("pain")
    liste.ajouter("beurre")
    print(liste)
    liste.enlever("pain")
    liste.afficher()
    liste.sauvegarder()
    liste.ajouter("coca")
    liste.ajouter("avoine")
    liste.ajouter("farine")
    liste.ajouter("glace")
    liste.ajouter("litière")
    liste.afficher()
    liste.sauvegarder()

    demain = Liste("tâches")
    demain.ajouter("Aller à la commune")
    demain.ajouter("Faire la vaisselle")
    demain.ajouter("conduire les enfants au tennis")
    demain.ajouter("Donner à manger aux chats")
    demain.afficher()
    demain.sauvegarder()

    print(liste)
    print(demain)




