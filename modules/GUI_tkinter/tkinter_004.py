# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:14:40 2023

@author: kpras
"""
# Demo of a simple calculator
# Notice how the columnspan parameter works, it resizes the widget to span across columns

import tkinter

def add_function():
    x = int(in1.get())
    y = int(in2.get())
    z = x + y
    label.configure(text=z,font=("verdana",14))
    
window = tkinter.Tk()
window.title("Calculator Sample")
window.configure(background="white")

button_sum = tkinter.Button(window,text="Add",font=("verdana",14),padx=60,pady=5,bg="green",fg="white",command=add_function)
button_sum.grid(row=1,column=0,columnspan=2)

in1 = tkinter.Entry(window,width=5,borderwidth=1,font=("verdana",14))
in1.grid(row=0,column=0,padx=20,pady=10)

in2 = tkinter.Entry(window,width=5,borderwidth=1,font=("verdana",14))
in2.grid(row=0,column=1,padx=20,pady=10)

label = tkinter.Label(window, text="0", font= ('Verdana',16), bg="lightgreen")
label.grid(row=0, column=2, rowspan=2)

window.mainloop()