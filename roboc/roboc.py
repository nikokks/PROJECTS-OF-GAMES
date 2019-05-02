# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            nouvelle_carte=Carte(nom_fichier[:-4],contenu)
	    cartes.append(nouvelle_carte)           
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("\n\nLabyrinthes existants :")
i=0
while i<len(cartes):
    print("  {} - {}".format(i + 1, cartes[i].nom))
    i+=1

# S'il y a une partie sauvegardée, on l'affiche
sauvegardes=[]
for nom_fichier in os.listdir("sauvegardes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("sauvegardes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            nouvelle_carte=Carte(nom_fichier[:-4],contenu)
	    sauvegardes.append(nouvelle_carte)           

# On affiche les cartes existantes sauvegardees
print("\nLabyrinthes enregistres :")
while i<len(cartes)+len(sauvegardes):
    print("  {} - {}".format(i + 1, sauvegardes[i-len(cartes)].nom))
    i+=1

# demande de saisie du numero du labyrinthe
reponse=0
liste=[str(i) for i in range(1,i+1)]
while reponse not in liste:
	print "\n\nEntrez un numéro de labyrinthe pour commencer a jouer : "
	reponse=raw_input()
reponse=int(reponse)

# on conserve la carte selectionnee sous le nom carte
carte=[cartes+sauvegardes][0][reponse-1]
print(carte.labyrinthe)
reponse2=0
while reponse2!=1: # tant que l'on a pas 1 cest a dire tant que l'on ordonne pas de quitter repeter
    reponse2=carte.labyrinthe.lecture_entree(raw_input())

    if reponse2 in (1,2) and carte.labyrinthe.sauvegarder==True:# si le joueur vient de jouer ou quil decide de quitter sauvegarder
         carte.sauvegarder()
    if carte.labyrinthe.partie_finie==True:# si on vient de terminer la partie
         reponse2=1
    if reponse2!=1: #astuce pour eviter les bugs lors du input
         reponse2=3

if carte.labyrinthe.partie_finie==True:
	os.remove("sauvegardes/"+carte.nom+'.txt')
