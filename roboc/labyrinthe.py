# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


# fonction permettant de creer une instance de la classe Labyrinthe
def creer_labyrinthe_depuis_chaine(chaine):
	objet=Labyrinthe("X","O",".","U",' ',chaine)
	return objet


class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles,portes,sorties,espace,chaine):
        self.robot = robot 					# symbole  representant le robot
        self.obstacles=obstacles 				# symbole  representant les obstacles
	self.portes=portes 					# symbole  representant les portes
	self.sorties=sorties 					# symbole  representant les sorties
	self.largeur=len(chaine.split('\r\n')[0])  		# largeur  du labyrinthe
	self.longueur=len(chaine.split('\r\n'))	   		# longueur du labyrinthe
	self.espace= espace					# symbole representant un espace vide dans le labyrinthe
	self.sauvegarder = True                                 # on enregistre toujours
	self.partie_finie=False
	# on met la chaine en liste de liste sous le nom d'attribut self.chaine_liste
	self.chaine_liste=[]
	for i in chaine.split('\r\n'):
		tableau=[]
		for j in i:
			tableau.append(j)
		self.chaine_liste.append(tableau)

	self.position_robot=self.position(self.robot)[0]	# position initiale du robot
	self.position_portes=self.position(self.portes) 	# position des portes
	self.position_sorties=self.position(self.sorties)	# position des sorties

    # methode permettant d'afficher le labyrinthe
    def __repr__(self):
	liste=[]
	for i in self.chaine_liste:
		liste.append("".join(i))
	return "\n\n{}\n\n".format("\r\n".join(liste))

    # methode permettant de determiner les positions des objets du labyrinthe (utile lors de l'initialisation des portes,obstacles,etc.)
    def position(self,objet):
	resultat=[]
	test=0
	for indice,i in enumerate(self.chaine_liste):
		if objet in i:
			resultat.append([indice,self.chaine_liste[indice].index(objet)])
			test=1
	if test==0:
		print 'probleme ! il n y a pas de {} dans le labyrinthe !'.format(objet)
	else:			
		return resultat

    # methode permettant de verifier la possibilite au robot de bouger dans la direction demandee
    def deplacement_possible(self,information):
	direction=information[0]				# recuperation de la direction du robot avec les lettres N S O ou E
	nombre=information[1:]					# recuperation du nombre de pas 1 2 ou 3
	if nombre==""  : nombre="1"				# transformation du vide en 1 pour faciliter la suite
	if direction in "Nn":	
		repetition_Y=-1
		repetition_X=0
	if direction in "Ss":
		repetition_Y=1
		repetition_X=0
	if direction in "Ee":	
		repetition_Y=0
		repetition_X=1
	if direction in "Oo":
		repetition_Y=0
		repetition_X=-1	
	indice=1
	while indice<=int(nombre):
		nouv_pos_probable=self.position_robot
		nouv_pos_probable=[nouv_pos_probable[0]+repetition_Y,nouv_pos_probable[1]+repetition_X]
		if self.chaine_liste[nouv_pos_probable[0]][nouv_pos_probable[1]]!=self.obstacles:
			self.deplacement(nouv_pos_probable)
		else:
			print "Obstabcle ! Le robot ne peut plus se deplacer dans cette direction !"
			break
		indice+=1
    def lecture_entree(self,information="Q"):
	if (information[0] in ("N",'n','e','E','S','s','O','o')) and (information[1:] in ('',"1","2","3")):
		self.deplacement_possible(information)
		return 2
	elif information in ("Q","q"):
		return 1
	else:
		print "Veuillez saisir N,E,S,O pour avancer ou Q pour quitter"
		return 0
    # methode permettant d'effectuer un deplacement du robot
    def deplacement(self,nouv_pos):

	# verification de l'existence d'une reapartition d'une porte si on etait dessus
	reponse_porte=False
	for i in self.position_portes:
		if i==self.position_robot:
			reponse_porte=True	
	if reponse_porte==True:
		self.chaine_liste[self.position_robot[0]][self.position_robot[1]]=self.portes
	else:
		self.chaine_liste[self.position_robot[0]][self.position_robot[1]]=' '
	

	# actualisation de la nouvelle position du robot
	self.position_robot=nouv_pos
	# marquage de la position du robot dans le labyrinthe
	self.chaine_liste[self.position_robot[0]][self.position_robot[1]]=self.robot
	# affichage du labyrinthe
	print self.__repr__()
	self.gagner()

    #verification si le robot est a la sortie
    def gagner(self):
	# si on est a la sortie on gagne
	if self.position_robot in self.position_sorties:
		print "Felcitation ! vous avez trouve la sortie !"
		self.sauvegarder = False
		self.partie_finie=True		

