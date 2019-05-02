# -*- coding: utf-8 -*-
"""
generer niveau
"""
from math import floor
from random import random
from constantes import *
import pygame 
class Creation_niveau:
    def __init__(self,choix):
        self.nombre_de_bombes=choix[0]
        self.nombre_de_lignes=choix[1]
        self.nombre_de_colonnes=choix[2]
        self.nombre_de_cases=self.nombre_de_lignes*self.nombre_de_colonnes
        self.dimension_fenetre=dimension_case*self.nombre_de_lignes
        self.structure=[]
        
    def generer_niveau(self):
        for i in range(self.nombre_de_lignes):
            liste2=[]
            for j in range(self.nombre_de_colonnes):
                liste2.append('0')
            self.structure.append(liste2)
        bombes_restantes=self.nombre_de_bombes
        while bombes_restantes!=0:
            indice_y=int(floor(random()*self.nombre_de_colonnes))
            indice_x=int(floor(random()*self.nombre_de_lignes))

            if self.structure[indice_x][indice_y]=='0':
                self.structure[indice_x][indice_y]='B'
                bombes_restantes-=1
        ensemble=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        for i in range(self.nombre_de_lignes):
            for j in range(self.nombre_de_colonnes):
                nombre_de_bombes_autour=0
                if self.structure[i][j]!='B':
                    for k,l in ensemble:
                        if k+i>=0 and k+i<self.nombre_de_lignes:
                            if l+j>=0 and l+j<self.nombre_de_colonnes:
                                if self.structure[k+i][l+j]=='B':
                                    nombre_de_bombes_autour+=1
                    self.structure[i][j]=str(nombre_de_bombes_autour)
    def sauvegarder(self):
        chaine=""
        for i in self.structure:
            chaine=chaine+"".join(i)+'\n'
        with open('niveau','w') as fichier:
            fichier.write(chaine)


class Demineur:
    def __init__(self,choix):
        self.demineur=Creation_niveau(choix)
        self.demineur.generer_niveau()
        self.nombre_de_bombes_restantes=choix[0]
        self.fin=False
        self.position_x=0
        self.position_y=0
        self.image_debut=pygame.image.load(image_debut)
        self.image_case_1= pygame.image.load(image_case_1)
        self.image_case_2= pygame.image.load(image_case_2)
        self.image_case_3= pygame.image.load(image_case_3)
        self.image_case_4= pygame.image.load(image_case_4)
        self.image_case_5= pygame.image.load(image_case_5)
        self.image_case_6= pygame.image.load(image_case_6)
        self.image_case_7= pygame.image.load(image_case_7)
        self.image_case_8= pygame.image.load(image_case_8)
        #self.image_bombe = pygame.image.load(image_bombe)
        self.image_bombe_erreur=pygame.image.load(image_bombe_erreur)
        self.image_drapeau=pygame.image.load(image_drapeau)
        self.image_vide   =pygame.image.load(image_vide)
        self.nombre=[str(i) for i in range(1,9)]
        self.tableau_visible=[]
        for i in range(self.demineur.nombre_de_colonnes):
            tableau=[]
            for j in range(self.demineur.nombre_de_lignes):
                tableau.append('?')
            self.tableau_visible.append(tableau)
    def selection(self):
        pass

    def afficher(self,fenetre):

        for indice_x,i in enumerate(self.tableau_visible):
            for indice_y,j in enumerate(i):
                lettre=self.tableau_visible[indice_x][indice_y]
                if lettre=='?':
                    fenetre.blit(self.image_debut, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='0':
                    fenetre.blit(self.image_vide, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='1':
                    fenetre.blit(self.image_case_1, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='2':
                    fenetre.blit(self.image_case_2, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='3':
                    fenetre.blit(self.image_case_3, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='4':
                    fenetre.blit(self.image_case_4, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='5':
                    fenetre.blit(self.image_case_5, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='6':
                    fenetre.blit(self.image_case_6, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='7':
                    fenetre.blit(self.image_case_7, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='8':
                    fenetre.blit(self.image_case_8, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='D':
                    fenetre.blit(self.image_drapeau, (indice_x*dimension_case,indice_y*dimension_case))
                elif lettre=='B':
                    fenetre.blit(self.image_bombe_erreur, (indice_x*dimension_case,indice_y*dimension_case))

    def gagne(self):
        nombre=0
        for i in self.tableau_visible:
            for j in i:
                if j in ('D','?'):
                    nombre+=1
        if nombre==self.nombre_de_bombes_restantes:
            self.fin=True
    def click(self,position,type_click):
        self.position_x=int(position[0]/dimension_case) # ligne  
        self.position_y=int(position[1]/dimension_case) # colonne
        if type_click==1:
            self.procedure((self.position_x,self.position_y))
        else:
            self.drapeau()

    def drapeau(self):
        if self.tableau_visible[self.position_x][self.position_y]=='?':
            self.tableau_visible[self.position_x][self.position_y]='D'
        elif self.tableau_visible[self.position_x][self.position_y]=='D':
            self.tableau_visible[self.position_x][self.position_y]='?'
        
        
    def procedure(self,position):
        ensemble=[(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]
        if self.tableau_visible[position[0]][position[1]]=='?':
            if self.demineur.structure[position[0]][position[1]]=='B':
                self.tableau_visible[position[0]][position[1]]='B'
                self.fin=True
            elif self.demineur.structure[position[0]][position[1]] in self.nombre:
                self.tableau_visible[position[0]][position[1]]=self.demineur.structure[position[0]][position[1]]

            elif self.demineur.structure[position[0]][position[1]]=='0':
                self.tableau_visible[position[0]][position[1]]='0'                
                for  i,j in ensemble:
                    if self.demineur.nombre_de_lignes>position[0]+i>=0:
                        if self.demineur.nombre_de_colonnes>position[1]+j>=0:
                            self.procedure((position[0]+i,position[1]+j))
                    
    
# ne pasoublier de compter le nombre de case restantes pour savoir si on gagne
##ne pas oublier de verifier que le nombre de bombes est inferieur au nombre de cases