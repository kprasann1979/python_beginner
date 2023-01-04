# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:46:27 2023

@author: kpras

Pillow is a python imaging library (PIL) used for handling images. We can open, manipulate, save images using this module. 
We make use of Pillow package to add images to our tkinters widgets. 
You can import JPG or PNG images of your wish and display it in tkinter canvas or buttons or labels.
"""

from PIL import Image
import tkinter

'''
#Demo to just open and show the image
right = Image.open("right.png") #please change the file path to your directory
right.show()
'''

#Demo to bind the image to a button
window = tkinter.Tk()
window.title("My GUI")
right = Image.open("right.png") #please change the file path to your directory
button = tkinter.Button(window,image = right)
button.grid(row=0, column=0)
window.mainloop()
