from tkinter import *

root=Tk()
equa=""

eq=StringVar()
eq.set("Enter An Expression")

en=Label(root,textvariable=eq)
en.grid(columnspan=3)

def btnpress(num):
    global equa
    equa=equa+str(num)
    eq.set(equa)

def equalpress():
    global equa
    total=str(eval(equa))
    eq.set(total)
    equa=""

def clearpress():
    global equa
    equa=" "
    eq.set(" ")

but1=Button(root,text="1",command=lambda:btnpress(1))
but1.grid(row=1,column=0)

but2=Button(root,text="2",command=lambda:btnpress(2))
but2.grid(row=1,column=1)

but3=Button(root,text="3",command=lambda:btnpress(3))
but3.grid(row=1,column=2)

but4=Button(root,text="4",command=lambda:btnpress(4))
but4.grid(row=2,column=0)

but5=Button(root,text="5",command=lambda:btnpress(5))
but5.grid(row=2,column=1)

but6=Button(root,text="6",command=lambda:btnpress(6))
but6.grid(row=2,column=2)

but7=Button(root,text="7",command=lambda:btnpress(7))
but7.grid(row=3,column=0)

but8=Button(root,text="8",command=lambda:btnpress(8))
but8.grid(row=3,column=1)

but9=Button(root,text="9",command=lambda:btnpress(9))
but9.grid(row=3,column=2)

but0=Button(root,text="0",command=lambda:btnpress(0))
but0.grid(row=4,column=1)

plus=Button(root,text="+",command=lambda:btnpress("+"))
plus.grid(row=1,column=3)

minus=Button(root,text="-",command=lambda:btnpress("-"))
minus.grid(row=2,column=3)

mul=Button(root,text="*",command=lambda:btnpress("*"))
mul.grid(row=3,column=3)

div=Button(root,text="/",command=lambda:btnpress("/"))
div.grid(row=4,column=2)

equal=Button(root,text="=",command=equalpress)
equal.grid(row=4,column=3)

clear=Button(root,text="C",command=clearpress)
clear.grid(row=4,column=0)

root.mainloop()
    
