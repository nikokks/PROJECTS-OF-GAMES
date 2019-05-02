# -*- coding: utf-8 -*-

"""
fichier contenant la classe Morpion
"""

from constantes import *
import pygame

class Morpion:
    def __init__(self,tour):
        self.o=pygame.image.load(image_o) 
        self.x=pygame.image.load(image_x)
        self.tour=tour
        self.fin=""
            
    def fin_de_partie(self,tableau):
        liste=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in liste:
            resultat=0
            for j in i:
                resultat+=tableau[j]
            if resultat==30:
                self.fin="o"
                return True
            elif resultat==3:
                self.fin="x"
                return True
        if self.fin=="":
            for i in range(9):
                if self.vide(i,tableau):
                    return False
            self.fin="e"
            return True
    def afficher(self,fenetre,tableau):
        for indice,i in enumerate(tableau):
            if i==10:
                fenetre.blit(self.o,((indice/3)*dimension_case+decalage_case,(indice%3)*dimension_case+decalage_case+100))
            elif i==1:
                fenetre.blit(self.x,((indice/3)*dimension_case+decalage_case,(indice%3)*dimension_case+decalage_case+100))
                
    def vide(self,case,tableau):
        if tableau[case]==0:
            return True
        else:
            return False

    def selection(self,event,tableau,tour):
        i,j=[int((event.pos[0])/200.),int((event.pos[1]-100)/200.)]
        indice=i*3+j
        if tableau[indice]==0:
            if tour=="x":
                tableau[indice]=1
                return True
            else:
                tableau[indice]=10
                return True
            