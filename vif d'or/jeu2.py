# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 12:32:44 2016

@author: Nikok
"""

from Tkinter import *
from math import sqrt
from random import randrange
  
r_0=80
r=r_0
nombre_de_boule_0= 1
nombre_de_boule=nombre_de_boule_0
x        = [0]* nombre_de_boule
y        = [0]* nombre_de_boule
dx       = [0]* nombre_de_boule
dy       = [0]* nombre_de_boule
taille_can=[700,500]
niveau = 0
niveau_0=0
coul= ['gold','red','blue','green','grey','purple', 'white','cyan','pink','brown','dark blue','light blue','pale blue']

boule = [0]*nombre_de_boule
a= [0]* nombre_de_boule
dx_ancien = dx
dy_ancien = dx
clique = [0]*2
vitesse_0  = 1
vitesse=vitesse_0
h=0
score = 0
resistance_vitesse=0

def bug():
    initialiser()
    
def creation_coordonnees_initiales():
    global x,y,nombre_de_boule,r,taille_can,r
    x        = [0]* nombre_de_boule
    y        = [0]* nombre_de_boule

    x[0]     = randrange(r+1,taille_can[0]-r-1)
    y[0]     = randrange(r+1,taille_can[1]-r-1)   
    
    compteur = 1
    while compteur < nombre_de_boule:
        d = randrange(r+1,taille_can[0]-r-1)
        b = randrange(r+1,taille_can[1]-r-1)
        c = 0
        for i in range(compteur):
            distance = sqrt( (x[i]-d)**2+(y[i]-b)**2 )
            if distance <= 2*r+2 and (d-r>0 and d+r<taille_can[0] and b-r>0 and b+r<taille_can[1] ):
                c=1
        if c==0 :
            x[compteur]= d
            y[compteur]= b
            compteur += 1

def creation_vitesses_initiales():
    global dx,dy,vitesse,nombre_de_balle
    dx       = [0]* nombre_de_boule
    dy       = [0]* nombre_de_boule
    for i in range(nombre_de_boule):
        dx[i]= randrange(-vitesse,vitesse+1)
        dy[i]= sqrt(vitesse**2 - dx[i]**2)
    

def rebonds_parois(i):
    global x,y,r,dx,dy,taille_can
    if x[i]+r     >= taille_can[0]:
        dx[i]=-abs(dx[i])
    if x[i]-r     <= 0 :
        dx[i]=abs(dx[i])
    if y[i]+r     >= taille_can[1]:
        dy[i]=-abs(dy[i])
    if y[i]-r     <= 0:
        dy[i]=abs(dy[i])



def rebonds_boules(i):
    global x,y,r,dx,dy,nombre_de_boule,a,dx_ancien,dy_ancien
    for j in range(nombre_de_boule):
        if j!=i and a[j]!=1 :
            distance = sqrt( (x[j]-x[i])**2+(y[j]-y[i])**2 )
            if distance <= 2*r+2 and dx_ancien[i] != dx[j] and dy_ancien[i] != dy[j] :
                a[i],a[j]=1,1
                dx[i],dx[j]=dx[j],dx[i]
                dy[i],dy[j]=dy[j],dy[i]
                p[i]+=1
                p[j]+=1

        
def move():
    global x,y,r,dx,dy,taille_can,nombre_de_boule,a,dx_ancien,dy_ancien,h,p
    a=[0]*nombre_de_boule
    e=0
    dx_ancien,dy_ancien=dx,dy
    for i in range(nombre_de_boule):
        rebonds_boules(i)
    for i in range(nombre_de_boule):
        if a[i]==0:
            rebonds_parois(i)
    for i in range(nombre_de_boule):
        x[i],y[i]=x[i]+dx[i],y[i]+dy[i]
        can.coords(boule[i],x[i]-r,y[i]-r,x[i]+r,y[i]+r)
    if h>0:
        can.after(3,move)

def initialiser(k=0):
    global x,y,r,coul,nombre_de_boule,h,boule,p
    p = [0]*nombre_de_boule
    creation_coordonnees_initiales()
    creation_vitesses_initiales()
    for i in range(nombre_de_boule-k*1):
        can.delete(boule[i])
    for i in range(nombre_de_boule):
        boule = [0]*nombre_de_boule
    for i in range(nombre_de_boule):        
        boule[i] = can.create_oval(x[i]-r,y[i]-r,x[i]+r,y[i]+r,outline='red',fill=coul[i],width=1)
    arreter()
    can.after(1000,demarrer)

def demarrer():
    global h
    if h==0:
        h=1
        move()

def pointeur(event):
    global x,y,r,h
    if h>0:
        distance_1 = sqrt((event.x-x[0])**2 + (event.y-y[0])**2)
        if distance_1 <= r+3:
            comptage_score(1)
        else : 
            comptage_score(-1)
            
def comptage_score(i):
    global score
    score+=i
    texte_score.configure(text='S C O R E = ' + str(score))
    if score % 3 ==0 and score>0 and i==1:        
        niveau_superieur()
    elif score % 3 ==2 and score>0 and i==-1:
        niveau_inferieur()
    

def arreter():
    global h
    h=0

def niveau_superieur():

    global vitesse,nombre_de_boule,r,vitesse_0,resistance_vitesse,niveau_0,niveau
    niveau = score/3
    nombre_de_boule +=1
    resistance_vitesse = (niveau/2)    
    vitesse = vitesse + int(resistance_vitesse)
    r = r - 1
    texte_information.configure(text='Vitesse = '+ str(vitesse)+  '   et   Rayon = ' + str(r))   
    initialiser(1)
        
def niveau_inferieur():

    global vitesse,nombre_de_boule,r,vitesse_0,resistance_vitesse,niveau_0,niveau
    niveau = score/5
    nombre_de_boule -=1   
    vitesse = vitesse - 2
    r = r + 1
    texte_information.configure(text='Vitesse = '+ str(vitesse)+  '   et   Rayon = ' + str(r))   
    initialiser(-1)


fenetre=Tk()
Label(fenetre,text=" A T T R A P P E   L E   V I F   D' O R",fg='red').grid(row=0,column=0, columnspan=4)
can=Canvas(fenetre,width=taille_can[0],height=taille_can[1],bg='black')
can.grid(row=1,column=0,columnspan=4)
can2=Canvas(fenetre,width=10,height=10)
can.bind('<Button-1>',pointeur)
can2.grid(row=2,column=0,sticky=W)
Button(can2,text='Commencer',command=initialiser,bg='gold').pack(side=LEFT,padx=2)
can3=Canvas(fenetre,width=10,height=10)
can3.grid(row=2,column=3,sticky=E)
Button(can3,text="en cas de bug",bg='red',command=bug).pack(side=RIGHT,padx=2)
texte_score = Label(fenetre,text='S C O R E = '+ str(score))
texte_score.grid(row=2,column=1,columnspan=2)
texte_information=Label(fenetre,text='Vitesse = '+ str(vitesse)+  '   et   Rayon = ' + str(r))
texte_information.grid(row=4,column=1,columnspan=2)
fenetre.mainloop()

"""
-probleme de synchronistaiotn entre rebons parois et rebonds boules 
=> si deux boules se touchent et qu une des deux touvhe une parois ca bug
-probleme de separation des boules si elles n'en sortent pas en une fois
-revoir la technique du if flag == 0 sur le pdf du portable 
-soucis avec les mauvais rebonds entre boules (ce nest pas parfait)
"""