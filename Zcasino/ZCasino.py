# -*- coding: utf-8 -*-
import os
from random import randrange
from math   import ceil


argent=-1

while (argent <=0) :
    argent = input(u"Entrez la somme d'argent (nombre entier) à laquelle vous venez à la table en $ : " )
    try:
        argent=int(argent)
    except ValueError:
        print "Vous n'avez pas saisi un nombre !"
        continue
    if argent <0:
        print u"La somme d'argent que vous avez entré n'est pas positive"
    elif argent==0:
        print u"La somme d'argent que vous avez entré est nulle il est donc impossible pour vous de pouvoir jouer"

print "Vous vous installez à la table avec ",argent," $"


continuer_partie=True

while continuer_partie :
    
    nombre_mise=-1
    
    while nombre_mise >49 or nombre_mise<0:
        nombre_mise=input(u"Entrez Le nombre à miser entre 0 et 49 : ")
        try :
            nombre_mise = int(nombre_mise)
        except ValueError:
            print "Erreur de Saisie du nombre à miser"
            continue
        if nombre_mise<0:
            print "Vous avez entré un nombre négatif "
        if nombre_mise>49:
            print "Vous avez entré un nombre supérieur à 49"
        

    mise=-1
    
    while mise<=0 or mise>argent :
        mise = input ("Entrez la mise (nombre entier) : ")
        try :
            mise=int(mise)
        except ValueError:
            print "erreur de saisie , entrez un nombre"
            continue
        if mise<0:
            print "Vous avez entré un nombre négatif"
        elif mise==0:
            print "Vous avez saisi une mise nulle"
        if mise>argent:
            print "Votre mise ", mise,"$ est supérieure à votre argent ",argent," $"
        
    numero_gagnant=randrange(50)
    

    if nombre_mise == numero_gagnant :
        argent = argent + 3*mise        
        print "Vous avez gagné", 3*mise,"$ !"
        print "vous possedez ",argent," $"
    elif nombre_mise%2==numero_gagnant%2:
        argent += ceil(0.5*mise)
        print u"vous avez misé sur la bonne couleur : gain de ",ceil(mise*0.5)," $"
        print "Vous possedez", argent, " $"
    else : 
        argent -= mise
        print "PERDU !"
        print "Vous possedez desormais ", argent," $"

    if argent <= 0:
        print "Vous etes ruiné revenez quand vous pourrez !"
        continuer_partie=False
    else :
        reponse = raw_input("Une autre partie ? (o/n) : ")
        if reponse == "n" or reponse == "N":
            continuer_partie=False
        
    
    

"""os.system("pause")"""