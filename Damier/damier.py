from Tkinter import *
from random import randrange

def damier():
    global x,y,liste
    can.delete(ALL)
    liste=[-1,-1]
    can.create_rectangle(0,0,x,y,fill='white')
    a,b=x/10.,y/10.
    k=0
    while k<10:    
        i=0
        while i<5:
            if k%2==0:
                x1,y1=2*i*a,k*b
                x2,y2=x1+a,y1+b
            elif k%2==1:
                x1,y1=2*i*a+a,k*b
                x2,y2=x1+a,y1+b
            can.create_rectangle(x1,y1,x2,y2,fill='blue')
            i+=1
        k+=1

def pions():
    global x,y,liste
    a,b=x/10.,y/10.
    i=randrange(10)
    j=randrange(10)
    c=0
    while c<len(liste):
        if i==liste[c] and j==liste[c+1]:
            i = randrange(10)
            j = randrange(10)
            c=0
        elif len(liste)>=202:
            c=len(liste)
        else:
            c=c+2
    liste.append(i)
    liste.append(j)
    x1,y1=a*i,b*j
    x2,y2=x1+a,y1+b    
    can.create_oval(x1,y1,x2,y2,fill='red') 
            
x,y,liste=200,200,[-1,-1]
fen=Tk()
can=Canvas(fen,width=x,height=y,bg='white')
can.pack(side=TOP,pady=5,padx=5)
bu1=Button(fen,text='Damier',command=damier)
bu1.pack(side=LEFT,padx=5,pady=5)
bu2=Button(fen,text='Pions',command=pions)
bu2.pack(side=RIGHT,padx=5,pady=5)
fen.mainloop()
