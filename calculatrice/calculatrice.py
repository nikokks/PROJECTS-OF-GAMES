
import numpy as np
from math import *
from tkinter import *
import matplotlib.pyplot as plt
from scipy import misc
import PIL.Image
import PIL.ImageTk

# affichage menu
def menu():
    # vers l'application graphique
    def vers_graphique():
        fenetre1.destroy()
        afficher_graphique()
    # vers l'application calculatrice
    def vers_calculatrice():
        fenetre1.destroy()
        afficher_calculatrice()
    fenetre1 = Tk() 
    fenetre1.title('M E N U ')
    
    bout1fen1    = Button(fenetre1,text='       GRAPHIQUE       ',command=vers_graphique)
    bout2fen1    = Button(fenetre1,text='CALCUL NUMERIQUE',command=vers_calculatrice)
    bout1fen1.pack(side='top')
    bout2fen1.pack(side='top')
    fenetre1.mainloop()

# affichage calculatrice
def afficher_calculatrice():
    # retour au menu
    def vers_menu():
        fenetre_calculatrice.destroy()
        menu()
    
    def saisie_expression(event):
        global nomfen1
        nomfen1 = entreefen1.get()
        try:
            champ_label2['text']="resultat = "+str(eval(nomfen1))       
        except:
            champ_label2['text']="Erreur de saisie"
    fenetre_calculatrice = Tk()
    fenetre_calculatrice.title("C A L C U L")
    bout1fen1    = Button(fenetre_calculatrice,text='RETOUR',command=vers_menu)
    bout1fen1.pack(side='top')
    champ_label1 = Label(fenetre_calculatrice, text="Entrez votre calcul : ")
    champ_label2 = Label(fenetre_calculatrice, text="resutlat = ")
    entreefen1 = Entry(fenetre_calculatrice)    
    entreefen1.bind('<Return>',saisie_expression)
    champ_label2.pack(side='bottom')
    entreefen1.pack(side='bottom')
    champ_label1.pack(side='top')
    fenetre_calculatrice.mainloop()


def afficher_graphique():
    def vers_menu():
        fenetre_graphique.destroy()
        menu()
    def fonction(n):
        global chaine       
        chaine2=chaine.replace("X",str(n))
        return eval(chaine2)
    def fonction_prime(f,a):
        h=1e-10
        return (f(a+h)-f(a-h))/(2*h)
    def saisie_expression(event):
        global chaine
        chaine = entreefen1.get()
        plot()

    def plot():
        global x_min,x_max,chaine,ok
        x=np.linspace(-10,10,10000)
        y=[]    
        z=[]
        index=0
        for indice,i in enumerate(x):
            try:
                y.append(fonction(i))
                z.append(fonction_prime(fonction,i))
            except ValueError:
                index=indice+1
                continue
        x=x[index:]
        plt.title(chaine.replace("X","x"))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axis([-10,10,-50,50])
        plt.plot(x,y, label='f')
        plt.plot(x,len(x)*[0],color='black')
        plt.plot([0]*len(x),[i*50 for i in x],color='black')
        plt.plot(x,z, label='f_prime' )
        plt.legend()
        plt.savefig('plot.png')
        plt.close()
        entreefen1.destroy()
        photo = PhotoImage(file='plot.png') 
        label = Label(fenetre_graphique, image=photo)
        label.grid(row=5) 
        label = tk.Label(fenetre_graphique, image=photo)
        label.grid(row=6)

        
            
    chaine="exp(X)*X+X"
    x_min=-10
    x_max=10
    fenetre_graphique = Tk()
    fenetre_graphique.title("REPRESENTATION GRAPHIQUE")    
    bout1fen1    = Button(fenetre_graphique,text='RETOUR',command=vers_menu)
    champ_label1 = Label(fenetre_graphique, text="Entrez votre expression en fonction de X : ")
    entreefen1 = Entry(fenetre_graphique)    
    entreefen1.bind('<Return>',saisie_expression)
    bout1fen1.grid(row=0)
    champ_label1.grid(row=1) 
    entreefen1.grid(row=2)
    


    fenetre_graphique.mainloop()   
    




afficher_graphique()