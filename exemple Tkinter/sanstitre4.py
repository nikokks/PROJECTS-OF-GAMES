# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 01:53:29 2016

@author: Nikok
"""

from Tkinter import *
from random import randrange

def drawline():
    global coul,x1,y1,x2,y2
    can1.create_line(x1,y1,x2,y2,width=n,fill=coul)
    y2,y1=y2+10,y1-10
    
def changecolor():
    global coul
    pal=['purple','cyan']
    c=randrange(2)
    coul=pal[c]
    
def drawline2():
    can1.create_line(0,325,500,325,width=2,fill='black')
    can1.create_line(250,0,250,650,width=2,fill='red')
x1,y1,x2,y2=0,650,500,00
coul = 'dark green'
n=1
fen1=Tk()
can1= Canvas(fen1,bg='dark grey',height=650,width=500)
can1.pack(side=LEFT)
bou1=Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2=Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3=Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4=Button(fen1,text='Tracer croix',command=drawline2)
bou4.pack()

fen1.mainloop()
fen1.destroy()