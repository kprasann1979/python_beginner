# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 09:31:24 2023

@author: kpras
"""

import tkinter
import tk_tools
def add():
    x = int(in1.get()) #get value from entry box
    y = int(in2.get()) #get value from entry box
    z = x + y
    #Convert the integer value to string to display in Seven segment widget
    ss_int.set_value(str(z)) # Update the value of seven segment display widget

window = tkinter.Tk() #create tkinter window
window.title("Addition") #give title
window.configure(background="white") #change background color
window.geometry("400x110")
button_on = tkinter.Button(window, text="Add",
font= ('Verdana',16), padx=60, pady =5,
bg="green",fg="white",
command = add)
button_on.grid(row=1,column=0, columnspan=2)
button_on.grid(row=1,column=0, columnspan=2)
in1 = tkinter.Entry(window, width = 5, borderwidth=1, font= ('Verdana',16))
in1.grid(row = 0, column =0, padx=20, pady =10)
in2 = tkinter.Entry(window, width = 5, borderwidth=1, font= ('Verdana',16))
in2.grid(row = 0, column =1, padx=20, pady =10)
ss_int = tk_tools.SevenSegmentDigits(window, digits=4, background='white', digit_color='black')
ss_int.grid(row=0, column=6, rowspan=2)
ss_int.set_value(str(0))

window.mainloop()