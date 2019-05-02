# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import *


import os
class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
	
    def sauvegarder(self):
	chemin = os.path.join("sauvegardes", self.nom+'.txt')
        with open(chemin, "w") as fichier:
		fichier.write(repr(self.labyrinthe))	
