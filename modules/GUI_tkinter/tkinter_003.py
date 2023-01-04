# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 08:54:33 2023

@author: kpras
"""

# Demo of event handling using GUI elements/widgets

import tkinter
def lights_on():
    label.configure(text="Light is ON",font=("verdana",16))
    button_on.configure(bg="light grey",state=tkinter.DISABLED)
    button_off.configure(bg="red",state=tkinter.NORMAL)
    
def lights_off():
    label.configure(text="Light is OFF",font=("verdana",16))
    button_off.configure(bg="light grey",state=tkinter.DISABLED)
    button_on.configure(bg="green",state=tkinter.NORMAL)

window = tkinter.Tk()
window.title("Event handling example GUI")
window.configure(bg="white")

label = tkinter.Label(window,text="Light is OFF",font=("verdana",16))
label.grid(row=0,column=1,columnspan=3)

button_on = tkinter.Button(window, text="ON",font=("verdana",14),padx=50,pady=20,bg="green",fg="yellow",command=lights_on)
button_on.grid(row=1,column=1)

button_off = tkinter.Button(window, text="OFF",font=("verdana",14),padx=50,pady=20,bg="red",fg="white",command=lights_off)
button_off.grid(row=1,column=2)

window.mainloop()
    
    