# -*- coding: utf-8 -*-
"""
Jeu Demineur

Script Python
Fichiers : demineur.py, images
"""


import time
import pygame
from pygame.locals import *
from classes import *
from constantes import *

pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
     #Chargement et affichage de l'écran d'accueil
     fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))     
     accueil = pygame.image.load(image_accueil).convert()
     fenetre.blit(accueil, (0,0))

     #Rafraichissement
     pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
     continuer_jeu = 1
     continuer_accueil = 1

	#BOUCLE D'ACCUEIL
     while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				

				if event.key == K_F1:
					continuer_accueil = 0
					choix = (5,5,5)		

				elif event.key == K_F2:
					continuer_accueil = 0
					choix = (10,10,10)
				elif event.key == K_F3:
					continuer_accueil = 0
					choix = (20,15,15)
				elif event.key == K_F4:
					continuer_accueil = 0
					choix = (150,30,30)
			


	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
     if choix != 0:
         #Chargement du fond
         fenetre = pygame.display.set_mode((choix[1]*dimension_case,choix[2]*dimension_case ))
         pygame.display.set_caption(titre_fenetre)
         fond = pygame.image.load(image_accueil).convert()
         jeu=Demineur(choix)
         jeu.afficher(fenetre)
         
         
				
	#BOUCLE DE JEU
     while continuer_jeu:
         
         #Limitation de vitesse de la boucle
         pygame.time.Clock().tick(30)
         for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == MOUSEBUTTONDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.button == 1:
					jeu.click(event.pos,event.button)
				elif event.button == 3:
					jeu.click(event.pos,event.button)
			
         #Affichages aux nouvelles positions
         fenetre.blit(fond, (0,0))
         jeu.afficher(fenetre)
         jeu.gagne()
         print jeu.fin
         pygame.display.flip()
         #Victoire -> Retour à l'accueil
         if jeu.fin == True:
                
                continuer_jeu = 0
                time.sleep(2)
pygame.quit()
