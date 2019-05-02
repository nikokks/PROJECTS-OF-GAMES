# -*- coding: utf-8 -*-
from Tkinter import *
from math import sin,cos,sqrt
from random import randrange

c=0                         # nombre de seconndes avant le debut de la partie
niveau_suivant =0           # niveau
x,y=0,0                     # position du clic
nombre_de_balle_0= 3        # nombre de balles initiales au niveau 0
nombre_de_balle= nombre_de_balle_0 # nombre de balles au niveau niveau_suivant
taille_ecran= [758*16/10.,600] # dimensions de l'ecran
vitesse_balle=3             # vitesse des balles
rayon = 60                  # rayon des balles
score=0                     # score réalisé
dx,dy=[0]*nombre_de_balle, [0]*nombre_de_balle  # tableau contenant les vitesses des balles
compteur = nombre_de_balle_0 # compteur de balles restantes avant prochain niveau
temps = 25                   # taux de rafraichisement du jeu en ms
nomfen1='anonyme'            # nom du joueur
ok= [0]* nombre_de_balle     # tableau 1 si balle touchee 0 sinon

# afficher menu
def afficher_fenetre_1():
    global nomfen1
    def jouer1fen1():
        # affichage de la seconde partie du menu et selection du nom du joueur
        def afficherfen1(event):
            global nomfen1
            nomfen1 = entreefen1.get()
            if nomfen1=='':
                nomfen1= 'anonymous'
            fen1.destroy()
            afficher_fenetre_2()
        textefen1  = Label(fen1,text='\n ENTRE TON NOM ')
        textefen1.grid(row=14,padx=5,pady=5) 
        entreefen1 = Entry(fen1)    
        entreefen1.bind('<Return>',afficherfen1)
        entreefen1.grid(row=15,padx=10,pady=10)
        Can3fen1    = Canvas(fen1,width=dimension_et_couleur_fen1[0],height=dimension_et_couleur_fen1[1],bg=dimension_et_couleur_fen1[2])
        Can3fen1.grid(row=16)


    def options1fen1():
        print('f')

    # variables de la fenetre 1

    dimension_et_couleur_fen1= [300,40,'dark blue']
    global nomfen1, dimension_et_couleur_fen1
    fen1=Tk()
    Can1fen1    = Canvas(fen1,width=dimension_et_couleur_fen1[0],height=dimension_et_couleur_fen1[1],bg=dimension_et_couleur_fen1[2])
    Can2fen1    = Canvas(fen1,width=dimension_et_couleur_fen1[0],height=dimension_et_couleur_fen1[1],bg=dimension_et_couleur_fen1[2])
    bou1fen1    = Button(fen1,text='J O U E R',command=jouer1fen1)
    bou2fen1    = Button(fen1,text='O P T I O N S',command=options1fen1)
    bou3fen1    = Button(fen1,text='Q U I T T E R',command=fen1.destroy)
        
    Can1fen1.grid(row=0)
    bou1fen1.grid(row=3,padx=5,pady=5)
    bou2fen1.grid(row=4,padx=5,pady=5)
    bou3fen1.grid(row=5,padx=5,pady=5)
    Can2fen1.grid(row=6)
    fen1.mainloop()





# afficher fenetre de jeu
def afficher_fenetre_2():
    global ok,cibles_x,cibles_y ,rayon,score,nombre_de_balle,compteur,niveau_suivant,chance

       
    # fonction verifiant si on a touche une des balles
    def verification(i):
        global ok,cibles_x,cibles_y ,rayon,score,nombre_de_balle,compteur,niveau_suivant,chance
        distance = sqrt((abs(x-cibles_x[i],))**2+(abs(y-cibles_y[i]))**2)
        if distance <= rayon and ok[i]==0:
            score += 1
            Can1fen2.delete(boule[i])
            compteur = compteur-1
            ok[i]=1
            okfen2.configure(text= ' SCORE = '+str(score))
        # si on aa touche toutes les balles alors niveau suivant
        if compteur == 0:
            niveau_suivant+=1            
            niveau(niveau_suivant)

 
        
            
    def pointeur(event):
        global x,y,cibles_x,cibles_y,nombre_de_balle 
        x,y=event.x,event.y
        for i in range(nombre_de_balle):
            verification(i)
        
    def bouger():
        global x,y,nombre_de_balle,dx,dy,rayon,taille_ecran,cibles_x,cibles_y,temps
    
        for i in range(nombre_de_balle):

            if cibles_x[i]+rayon >=taille_ecran[0]:
                dx[i]   = -dx[i]
            if cibles_x[i]-rayon<=0:
                dx[i]   = -dx[i]
            if cibles_y[i]+rayon>=taille_ecran[1]:
                dy[i]   = -dy[i]
            if cibles_y[i]-rayon<=0:
                dy[i]   = -dy[i]
            cibles_x[i] = cibles_x[i]+dx[i]
            cibles_y[i] = cibles_y[i]+dy[i]
            Can1fen2.coords(boule[i],cibles_x[i]-rayon,cibles_y[i]-rayon,cibles_x[i]+rayon,cibles_y[i]+rayon)
        Can1fen2.bind('<Button-1>',pointeur)
        Can1fen2.after(temps,bouger)

    # definition du niveau 
    def niveau(niveau=0):
        global ok,vitesse_balle,cibles_x,cibles_y,rayon,taille_ecran,dx,boule,dy,nombre_de_balle,compteur,nombre_de_balle_0,temps
        try:
            for i in range(0,nombre_de_balle):
                    if boule[i]:
                        Can1fen2.delete(boule[i])
        except NameError:
            pass
        nombre_de_balle = nombre_de_balle_0 + niveau
        compteur        = nombre_de_balle
        boule           = [0] * nombre_de_balle
        ok              = [0] * nombre_de_balle
        cibles_x        = [0]*nombre_de_balle
        cibles_y        = [0]*nombre_de_balle
        dx,dy=[0]*nombre_de_balle, [0]*nombre_de_balle 
        # reduction du temps de rafraichissement (acceleration des balles)
        temps=temps -1
        # diminution du rayon des balles
        rayon=rayon-1
        for i in range(nombre_de_balle):
            cibles_x[i] = randrange(rayon,int(taille_ecran[0]-rayon))
            cibles_y[i] = randrange(rayon,int(taille_ecran[1]-rayon))
            dx[i]       = randrange(2,vitesse_balle)
            dy[i]       = sqrt(vitesse_balle**2-dx[i]**2)    
        for i in range(nombre_de_balle):
            boule[i]    = Can1fen2.create_oval(cibles_x[i]-rayon,cibles_y[i]-rayon,cibles_x[i]+rayon,cibles_y[i]+rayon,fill='blue',width=1,outline='red')    
        Can1fen2.after(50,bouger)

    # compte a rebours avant debut de partie
    def comptearebours():
        global c
        
        texte_depart.configure(text = str(c))
        if c>0:
            fenetre2.after(1000,comptearebours)  
        elif c==0:
            texte_depart.configure(text=' S T A R T !')
            niveau()
        c=c-1
    
    nomfen2= ''
    for i in range(len(nomfen1)):
        nomfen2=nomfen2+ nomfen1[i]+ ' '


    fenetre2=Tk()

    texte_depart = Label(fenetre2,text=' A T T E N T I O N    '+str(nomfen2.upper())+ '    L A  P A R T I E   V A   C O M M E N C E R  ! ', fg='blue')
    texte_depart.grid(row=0)
    Can1fen2  = Canvas (fenetre2,width=taille_ecran[0],height=taille_ecran[1],bg='white')
    Can1fen2.grid(row=1,padx=5,pady=5)
    Can1fen2.create_rectangle(1,1,taille_ecran[0]+2,taille_ecran[1]+2,outline='black',width=3)
    fenetre2.after(1000,comptearebours)
    Can1fen2.bind('<Button-1>',pointeur)
    okfen2 = Label(fenetre2,text='SCORE = 0 ')
    okfen2.grid(row=15)
    Can1fen2.grid(row=1,padx=5,pady=5)

    fenetre2.mainloop()
afficher_fenetre_1()

 





"""
# ajouter un compteur de temps pour les records

# probleme avec le compteur de chance restantes


variables globales pour le menu options:
resoltion => faire menu deroulant 
"""