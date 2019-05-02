# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 18:36:14 2016

@author: Nikok
"""
from Tkinter import *
from numpy import *
from random import randrange
x,y=150,150
taille = 5
position = array([[0,0]]*taille)
dx,dy=0,-10
collision = 0
dt=200
position_manger =[randrange(10,295,10),randrange(10,295,10)]
k=0
h=0
position_manger_2 = [0,0]
nourriture = [0]
def manger():
    global dt,position_manger,taille,k,rectangle,position,h,position_manger_2,nourriture
    
    if k== 0:
        k=1        
        
        nourriture[0] = can.create_rectangle(position_manger[0]-5,position_manger[1]-5,position_manger[0]+5,position_manger[1]+5,fill='red')
    if position_manger[0]==position[0][0] and position_manger[1]==position[0][1] : 
        taille+=1
        dt-=5
        position_3 = array([[0,0]]*(taille))
        for i in range(taille-1):
            position_3[i] = position[i]
        position = position_3
        position_manger_2 = position_manger
        h=0
        position_manger =[randrange(10,295,10),randrange(10,295,10)]
        k=0
        can.delete(nourriture[0])

def calcul_collision():
    global collision,position
    if not(5<=position[0][0]<=295):
        collision = 1        
    if not(5<=position[0][1]<=295):
        dy=0
        collision = 1 
def bouger(): 
    global position,variable,dx,dy,collision,h,position_manger_2,dt
    h+=1
    if h==1: 
        position[taille-1],position[taille-1]= [position_manger_2[0],position_manger_2[1]]
        rectangle[taille]= can.create_rectangle(position[taille-1][0]-5,position[taille-1][1]-5,position[taille-1][0]+5,position[taille-1][1]+5,width=2,fill='yellow')
    manger()
    print taille
    position_2 = array([[0,0]]*(taille+1))
    for i in range(taille):
        position_2[i+1] = position[i]
    position = position_2
        
    position[0][0]= position[1][0]+dx
    position[0][1]= position[1][1]+dy
    print position    
    calcul_collision()    
    print collision
    if collision ==0:
        for i in range(taille):
            can.coords(rectangle[i],position[i][0]-5,position[i][1]-5,position[i][0]+5,position[i][1]+5)
        can.after(dt,bouger)
def move(event):
    global dx,dy
    depl = event.keysym
    if depl == 'Left':
        dx,dy=-10,0
    if depl == 'Right':
        dx,dy=10,0
    if depl == 'Up':
        dx,dy=0,-10
    if depl == 'Down':
        dx,dy=0,10

fen= Tk()
can = Canvas(width=295,height=295)
can.pack()
can.create_rectangle(3,3,296,296,width=3,fill='white',outline='black')
rectangle = [0]*50
for i in range(taille):    
    position[i][0],position[i][1]= x , y+i*10
    rectangle[i]= can.create_rectangle(position[i][0]-5,position[i][1]-5,position[i][0]+5,position[i][1]+5,width=2,fill='yellow')
can.focus_set()
bouger()
can.bind('<KeyPress>',move)    
fen.mainloop()

"""arriver a supprimer e cube jaune"""