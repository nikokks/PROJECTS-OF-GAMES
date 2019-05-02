# -*- coding: utf-8 -*-
"""
engine.py

contient la classe Ia intelligence artificielle
"""
from random import random
class Ia:
    def __init__(self):
    	self.resultat_gain=[0,0,0,0,0,0,0,0,0]
	self.resultat_perdre=[0,0,0,0,0,0,0,0,0]
	self.resultat_egalite=[0,0,0,0,0,0,0,0,0]
	self.gagne=[]
	self.case=[]
    def fin_de_partie(self,tableau):
    	liste=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    	for i in liste:
    	    res=0
    	    for j in i:
    	        res+=tableau[j]
    	    if res==30:
    	        return True
    	    elif res==3:
    	        return True
    	for i in range(9):
    	    if 0 in tableau:
    	        return False
    	return True
      

    def gagner(self,tableau):
    	liste=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    	for i in liste:
    	    res=0
    	    for j in i:
    	        res+=tableau[j]
    	    if res==30:
    	        return 1
    	    elif res==3:
    	        return -1
    	return 0



    def recurrence(self,tableau,dico,typ):

    	if self.fin_de_partie(tableau):
         return self.gagner(tableau)
     
    	for i in range(9):
    	    if tableau[i]==0:
    	        tab=list(tableau)
	       
    	        if typ=='o':
                 tab[i]=10
                 dico[i]=self.recurrence(tab,{},'x')
    	        else:
    	            tab[i]=1
    	            dico[i]=self.recurrence(tab,{},'o')
    	return dico
    def choix(self,tableau,tour):
        self.dico=self.recurrence(tableau,{},tour)
        self.dico=self.suite(0,self.dico,0)
        self.reponse=self.maximum_dico(self.dico)
        self.choix=[i for i in self.dico if self.dico[i]==self.reponse]
        choix=int(random()*len(self.choix))
        tableau[self.choix[choix]]=10
        
    def suite(self,k,dico,r):
        for i in dico:
            if type(dico[i])==dict:
                dico[i]=self.suite(k+1,dico[i],r+1)
        if r==0:
            return dico
        if k%2==0:
            return self.maximum_dico(dico)
        else:
            return self.minimum_dico(dico)

        
        
        
        
    def maximum_dico(self,dico):
        maximum=-1
        for i in dico:
            if dico[i]>maximum:
                maximum=dico[i]
        return maximum
        
    def minimum_dico(self,dico):
        minimum=1
        for i in dico:
            if dico[i]<minimum:
                minimum=dico[i]
        return minimum
        

        
	"""
        resultat=0
        resultat_indice=0
        for indice,i in enumerate(self.resultat_gain):
            if resultat<i:
                resultat_indice=indice
                resultat=i
        if resultat==0:
            for indice,i in enumerate(self.resultat_egalite):
                if resultat<i:
                    resultat_indice=indice
                    resultat=i
        tableau[resultat_indice]=10
	"""
if __name__=='__main__':
	ok=Ia()
	print ok.choix([1,1,1,1,1,0,10,0,0],'o')
"""
XXO
X..
O.. 
 """
 
