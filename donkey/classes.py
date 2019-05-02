"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de creer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Methode permettant de generer le niveau en fonction du fichier.
		On cree une liste generale, contenant une liste par ligne a afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite a la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne a la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Methode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyee par generer()"""
		#Chargement des images (seule celle d'arrivee contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position reelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Depart
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivee
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
			
			
			
			
class Perso:
	"""Classe permettant de creer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par defaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de deplacer le personnage"""
		
		#Deplacement vers la droite
		if direction == 'droite':
			#Pour ne pas depasser l'ecran
			if self.case_x < (nombre_sprite_cote - 1):
				#On verifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Deplacement d'une case
					self.case_x += 1
					#Calcul de la position "reelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Deplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Deplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Deplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
