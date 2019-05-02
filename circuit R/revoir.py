from Tkinter import *

    
def switch():
   global n
   if n==0:
       n=1
       can.coords(inter,130,90,160,90)
   elif n==1:
       n=0
       can.coords(inter,130,90,160,80)

def intensity1(event):
    global VarVolt,VarResist,n
    if n==1:
        VarVolt=str(eval(volt.get()))
        I= str(eval(VarVolt)/float(eval(VarResist)))
        ok.configure(text='Intensite de gfnxcfx' + I +' Amperes')
    elif n==0:
        ok.configure(text="Intensite nulle car l'interrupteur est ouvert")
        

def intensity2(event):
    global VarVolt,VarResist,n
    if n==1:
        VarResist=str(eval(resis.get()))
        I=str(eval(VarVolt)/float(eval(VarResist))) 
        ok.configure(text='Intensite de ' + I +' Amperes')
    elif n==0:
        ok.configure(text="Intensite nulle car l'interrupteur est ouvert")
        

fen=Tk()
n=1
VarVolt=StringVar()
VarVolt.set('1')
VarResist=StringVar()
VarResist.set('1')

can = Canvas(fen,width=250,height=200)
can.grid(row=2,columnspan=2)
can.create_rectangle(50,80,100,100,outline='black',fill='blue',width=2)
can.create_line(30,90,50,90,fill='black',width=2)
can.create_line(30,150,30,90,fill='black',width=2)
can.create_line(30,150,150,150,fill='black',width=2)
can.create_line(180,150,220,150,fill='black',width=2)
can.create_line(220,90,220,150,fill='black',width=2)
can.create_line(100,90,130,90,fill='black',width=2)
can.create_line(220,90,160,90,fill='black',width=2)
can.create_rectangle(150,160,180,140,outline='black',fill='yellow',width=2)

can0=Canvas(fen,width=1,height=1)
can0.grid(row=1)
Label(can0,text='G',fg='yellow').grid(row=0,column=0)
Label(can0,text='R',fg='blue').grid(row=0,column=1)
Label(can0,text='I',fg='red').grid(row=0,column=2)
inter= can.create_line(130,90,160,90,fill='red',width=2)
Butt=Button(fen,text='ON/OFF',command=switch).grid(row=5,columnspan=2)

can1=Canvas(fen,width=1,height=1)
can1.grid(row=15)
Label(can1,text=' Voltage : ').grid(row=0,column=0)
volt= Entry(can1,textvariable =VarVolt)
volt.bind("<Return>", intensity1)
volt.grid(row=0,column=1)
Label(can1,text='V').grid(row=0,column=2)


can2=Canvas(fen,width=1,height=1)
can2.grid(row=16)
Label(can2,text='  Resistance : ').grid(row=0,column=0)
resis=Entry(can2)
resis.bind("<Return>", intensity2)
resis.grid(row=0,column=1)
Label(can2,text='Ohm').grid(row=0,column=2)


can3=Canvas(fen,width=1,height=1)
can3.grid(row=17)
ok= Label(can3,text='Intensite nulle')
ok.grid(row=0,column=0)
fen.mainloop()