# -*- coding: utf-8 -*-
""" The Hardest Game """
from Tkinter import *
from numpy   import *

deaths= 0
numero_niveau = 1

sol = array([[0],
            
[[30,100,120,280 ,'light green'   ,"coordonnées du rectangle de départ"],
 [480,100,570,280 ,'light green'   ,"coordonnées du rectangle d'arrivée"],
 [range(12),range(6)               ,"boucle avec j puis i"],
 [ ['(j+i)%2==0'   ,'light grey'],
   ['(j+i)%2==1'     ,'white'   ],
   ['j==0 and i<5' ,'dark grey' ],
   ['i==5 and j>1' ,'dark grey' ],
   ['i==0 and j<10','dark grey' ],
   ['i>0 and j==11','dark grey' ],'conditions dans les deux boucles']]]
 
)

bords = array([[0],
              
[[28.5,97  ,28.5 ,281.5,'left'],[30  ,97.5,120 ,97.5 ,'up'   ],
 [30  ,280 ,181.5,280  ,'down'],[179 ,250 ,179 ,280  ,'right'],
 [180 ,251 ,450  ,251  ,'down'],[451 ,130 ,451 ,253  ,'right'],
 [450 ,130 ,480  ,130  ,'down'],[480 ,130 ,480 ,281.5,'left' ],
 [480,280.5,571.5,280.5,'down'],[571 ,100 ,571 ,282  ,'right'],
 [420,100 ,571     ,100,'up'  ],[421 ,100 ,421 ,130  ,'left' ],
 [148,130,422,130      ,'up'  ],[148 ,130 ,148 ,250  ,'left' ],
 [120,248,148,248      ,'up'  ],[119 ,97  ,119 ,248  ,'right']]])
# important de ne pas oublier le classement croissant de l'ordre des x et y  x1<x2 et y1<y2

    
carre_coord_init = [abs(sol[numero_niveau][0][2]-sol[numero_niveau][0][0])/2.+min(sol[numero_niveau][0][2],sol[numero_niveau][0][0]),
                    abs(sol[numero_niveau][0][3]-sol[numero_niveau][0][1])/2.+min(sol[numero_niveau][0][3],sol[numero_niveau][0][1])]

def partie():
    global numero_niveau,sol,bords,deaths,carre_coord_init
    x,y=carre_coord_init[0],carre_coord_init[1]
    limites = [0]*len(bords[numero_niveau])
    partie_termine=0
    
    def construction_sol(element_fenetre):
        global numero_niveau,sol
        sol_niveau = sol[numero_niveau]

        for i in range(2):
            element_fenetre[3].create_rectangle(sol_niveau[i][0],sol_niveau[i][1],sol_niveau[i][2],sol_niveau[i][3],fill=sol_niveau[i][4],width=0)
        for j in sol_niveau[2][0]:
            for i in sol_niveau[2][1]:
                for k in range(len(sol_niveau[3])-1):
                    if eval(sol_niveau[3][k][0]):
                        coul=sol_niveau[3][k][1]
                        element_fenetre[3].create_rectangle(30*(4+j), 100+30*(i), 30*(5+j),100+30*(i+1),width=0,fill=coul)

    def construction_bords(element_fenetre):
        global bords,numero_niveau
        bords_niveau=bords[numero_niveau]
        for i in range(len(bords_niveau)):
            limites[i] = element_fenetre[3].create_line(bords_niveau[i][0],bords_niveau[i][1],bords_niveau[i][2],bords_niveau[i][3],width=3)
            
        """
        element_fenetre[3].create_rectangle(150+30*3, 100+30*5, 150+30*3+30,100+30*5+30,width=0,fill='white')
        element_fenetre[3].create_rectangle(150+30*3+30, 100+30*5, 150+30*3+30+30,100+30*5+30,width=0,fill='grey')
        element_fenetre[3].create_rectangle(150+30*3+30, 100+30*1, 150+30*3+30+30,100+30*1+30,width=0,fill='white')
        """
        

    def retour_menu():
        for i in range(4):
            element_fenetre[i].destroy()
        menu()  
    activekey = {}
    for k in ['left', 'up', 'right', 'down']:
        activekey[k] = False
        
    def pressed(event):
        key = event.keysym.lower()
        if key in activekey:
            activekey[key] = True
 
    def released(event):
        key = event.keysym.lower()
        if key in activekey:
            activekey[key] = False  
    def calcul_collisions_bords(coords_sommets_carre,bords_niveau):
        """"for i in range(len(bords_niveau)):"""
        deplacement =  [2,2,2,2]
        for i in range(len(bords_niveau)):
            if bords_niveau[i][4] == 'up':
                if bords_niveau[i][0]<=coords_sommets_carre[0]<=bords_niveau[i][2] or bords_niveau[i][0]<=coords_sommets_carre[2]<=bords_niveau[i][2]:
                    if coords_sommets_carre[1]-2<=bords_niveau[i][1] and coords_sommets_carre[3]>=bords_niveau[i][1]:
                        deplacement[0]=0
            if bords_niveau[i][4] == 'left':
                if bords_niveau[i][1]<=coords_sommets_carre[1]<=bords_niveau[i][3] or bords_niveau[i][1]<=coords_sommets_carre[3]<=bords_niveau[i][3]:
                    if coords_sommets_carre[0]-2<=bords_niveau[i][0] and coords_sommets_carre[2]>=bords_niveau[i][0]:
                        deplacement[1]=0
            if bords_niveau[i][4] == 'right':
                if bords_niveau[i][1]<=coords_sommets_carre[1]<=bords_niveau[i][3] or bords_niveau[i][1]<=coords_sommets_carre[3]<=bords_niveau[i][3]:
                    if coords_sommets_carre[2]-2<=bords_niveau[i][0] and coords_sommets_carre[2]>=bords_niveau[i][0]:
                        deplacement[2]=0  
            if bords_niveau[i][4] == 'down':
                if bords_niveau[i][0]<=coords_sommets_carre[0]<=bords_niveau[i][2] or bords_niveau[i][0]<=coords_sommets_carre[2]<=bords_niveau[i][2]:
                    if coords_sommets_carre[1]-2<=bords_niveau[i][1] and coords_sommets_carre[3]>=bords_niveau[i][1]:
                        deplacement[3]=0

        return deplacement

        


    def animation(k=0):
        global bords,numero_niveau,partie_termine,sol
        def conditions_changement_de_niveau():
            global numero_niveau
            if partie_termine ==1:
                for i in range(4):
                    element_fenetre[i].destroy()
                numero_niveau += 1               
                menu()
        
        if k==0:
            partie_termine=0
            arrivee = sol[numero_niveau][1]
            c2 = element_fenetre[3].coords(carre)
            bords_niveau= bords[numero_niveau]
            coords_sommets_carre = [c2[0]-1.5,c2[1]-1.5,c2[2]+1.5,c2[3]+1.5]
            sommets_carre = array([[coords_sommets_carre[0],coords_sommets_carre[1]],
                                   [coords_sommets_carre[0],coords_sommets_carre[3]],
                                   [coords_sommets_carre[2],coords_sommets_carre[1]],
                                   [coords_sommets_carre[2],coords_sommets_carre[3]]])
        
            for i in range(4):        
                if arrivee[0]<=sommets_carre[i][0]<=arrivee[2] and arrivee[1]<=sommets_carre[i][1]<=arrivee[3]:
                    partie_termine = 1
                    k+=1
                    if k==1:
                        conditions_changement_de_niveau()
                
            depl = calcul_collisions_bords(coords_sommets_carre,bords_niveau)

            if activekey['up'] and activekey['left']:
                element_fenetre[3].coords(carre, (c2[0]-depl[1], c2[1]-depl[0], c2[2]-depl[1], c2[3]-depl[0]))
            elif activekey['up'] and activekey['right']:
                element_fenetre[3].coords(carre, (c2[0]+depl[2], c2[1]-depl[0], c2[2]+depl[2], c2[3]-depl[0])) 
            elif activekey['down'] and activekey['left']:
                element_fenetre[3].coords(carre, (c2[0]-depl[1], c2[1]+depl[3], c2[2]-depl[1], c2[3]+depl[3]))
            elif activekey['down'] and activekey['right']:
                element_fenetre[3].coords(carre, (c2[0]+depl[2], c2[1]+depl[3], c2[2]+depl[2], c2[3]+depl[3])) 
            elif activekey['up']:
                element_fenetre[3].coords(carre, (c2[0], c2[1]-depl[0], c2[2], c2[3]-depl[0]))
            elif activekey['left']:
                element_fenetre[3].coords(carre, (c2[0]-depl[1], c2[1], c2[2]-depl[1], c2[3]))
            elif activekey['right']:
                element_fenetre[3].coords(carre, (c2[0]+depl[2], c2[1], c2[2]+depl[2], c2[3]))
            elif activekey['down']:
                element_fenetre[3].coords(carre, (c2[0], c2[1]+depl[3], c2[2], c2[3]+depl[3]))

            if partie_termine ==0:
                element_fenetre[3].after(10, animation)
    element_fenetre    = [0]*4
    element_fenetre[0] = Button(fenetre,text='  M E N U   ',command=retour_menu)
    element_fenetre[1] = Label(fenetre,text='                 '+ str(numero_niveau)+'  / 30'+'                 ',fg='green' )
    element_fenetre[2] = Label(fenetre,text='D E A T H S  =  '+str(deaths))    
    element_fenetre[3] = Canvas(fenetre,width=600,height=375)
    element_fenetre[3] . create_rectangle(4,4,600,375,outline='black',fill='dark grey',width=4)
    element_fenetre[3].focus_set()
    construction_sol  (element_fenetre)
    construction_bords(element_fenetre)
    
    element_fenetre[3] . bind("<KeyPress>", pressed)
    element_fenetre[3] . bind("<KeyRelease>", released)
    element_fenetre[0] . grid(row=0,column=0,sticky=W)
    element_fenetre[1] . grid(row=0,column=1)    
    element_fenetre[2] . grid(row=0,column=2,sticky=E)
    element_fenetre[3] . grid(row=1,column=0,columnspan=3)
    carre_coord_init = [abs(sol[numero_niveau][0][2]-sol[numero_niveau][0][0])/2.+min(sol[numero_niveau][0][2],sol[numero_niveau][0][0]),
                        abs(sol[numero_niveau][0][3]-sol[numero_niveau][0][1])/2.+min(sol[numero_niveau][0][3],sol[numero_niveau][0][1])]
    carre = element_fenetre[3].create_rectangle(carre_coord_init[0]-18/2.,carre_coord_init[1]-18/2.,carre_coord_init[0]+18/2.,carre_coord_init[1]+18/2.,width=3,outline='black',fill='red')
    animation(0)



fenetre=Tk()
def menu():
    element_fenetre = [0]*5
    def destruction():
        for i in range(5):
            element_fenetre[i].destroy()
        partie()

    global fenetre
    fenetre.title('                                                              T H E   H A R D E S T   G A M E   ')
    element_fenetre[0] = Canvas ( width=600,height=180,bg='white')
    element_fenetre[0].grid(row=0,column=0,columnspan=3)
    element_fenetre[1] = Canvas ( width=230,height=30,bg='white')
    element_fenetre[1].grid(row=1,column=0)
    element_fenetre[2] = Canvas ( width=230,height=30,bg='white')
    element_fenetre[2].grid(row=1,column=2)
    element_fenetre[3] = Canvas ( width=600,height=180,bg='white')
    element_fenetre[3].grid(row=2,column=0,columnspan=3)
    element_fenetre[4]= Button(text='R E A D Y   T O   P L A Y',fg='green',command=destruction)
    element_fenetre[4].grid(pady=5,row=1,column=1)
    rectangle = element_fenetre[0].create_rectangle(4,4,186,184,fill='blue',width=4,outline='black')
    element_fenetre[1].create_rectangle(4,0,186,182,fill='blue',width=4,outline='black')
    element_fenetre[3].create_rectangle(4,0,186,180,fill='blue',width=4,outline='black')
    element_fenetre[0].create_rectangle(400,4,600,184,fill='red',width=4,outline='black')
    element_fenetre[2].create_rectangle(30,0,231,176,fill='red',width=4,outline='black')
    element_fenetre[3].create_rectangle(400,0,600,180,fill='red',width=4,outline='black')    
    element_fenetre[0].create_line(186,4,400,4,fill='black',width=4)
    element_fenetre[3].create_line(186,180,400,180,fill='black',width=4)  
menu()

fenetre.mainloop()

"""
dimensions de fenetre_menu = width=600,height=400
propotions 
carré du sol =                     240/240 = 1.00 240=2*2*2*3*5*2 => 30
largeur exterieur du carré 170/237 168/240 = 0.70 168=2*2*2*3*7   => 21
largeur interieur du carré 116/237 120/240 = 0.50 120=2*2*2*3*5   => 15
bordure = 29/217*240                32/240 = 0.13  32=2*2*2*2*2   =>  3
diametre exterieur cercle  125/240 120/240 = 0.50 120=2*2*2*3*5   => 15
diametre interieur cercle  66 /240 72/240  = 0.30  72=2*2*2*3*3   =>  9



soucis avec la focntion animation elle tourne une fois de trop et appelle donc de elements supprimées 
verifier la vitesse de depalcement du carré
faire un module creation de niveau a faire depuis le menu

"""
