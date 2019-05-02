# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:55:02 2018

@author: nicolas
"""

import pygame
from pygame.locals import *
from classes import *
import time
import engine
tableau=[]
for i in range(9):
    tableau.append(0)
tour='x'

pygame.init()
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre+100))
pygame.display.set_caption("JEU DU MORPION")
pygame.display.flip()
fond = pygame.image.load(image_fond).convert()


nouvelle_partie=1
while nouvelle_partie:
    tour='x'
    partie=Morpion(tour)
    continuer_partie=1
    fenetre.blit(fond, (0,100))
    pygame.display.flip()

    while continuer_partie:
        ok=0
        ia=engine.Ia()
        partie.afficher(fenetre,tableau)
        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                nouvelle_partie = 0
                continuer_partie = 0
            elif event.type == MOUSEBUTTONDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.button == 1:
                        if partie.selection(event,tableau,tour):
                            tour='o'
                            partie.afficher(fenetre,tableau)
                            pygame.display.flip()

                            ok=1
        
        if partie.fin_de_partie(tableau):
            continuer_partie=0
            tableau=[]
            for i in range(9):
                tableau.append(0)
            time.sleep(2)
            break
        if ok==1:
            if 0 in tableau:
                ia.choix(tableau,tour)
                tour='x'
        partie.afficher(fenetre,tableau)
        pygame.display.flip()

pygame.quit()