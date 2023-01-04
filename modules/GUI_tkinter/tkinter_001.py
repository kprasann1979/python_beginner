import tkinter
window = tkinter.Tk()
window.title = "My first GUI"
window.configure(background="aqua")


#Demo the usgae of button widget
'''
window.geometry("500x600")
button1 = tkinter.Button(window,text="Click Me",font=("verdana",14),bg="blue",state=tkinter.NORMAL)
button2 = tkinter.Button(window,text="Click Me",font=("verdana",14),bg="green",state=tkinter.DISABLED)
button1.grid(row=0,column=0)
button2.grid(row=0,column=0)
'''

#Demo the usage of label and entry widget
'''
window.geometry("500x600")
label = tkinter.Label(window, text = "Please enter some text below...",font = ('Verdana',9), bg ="orange",fg="blue")
label.grid(row=0, column=0)
entry = tkinter.Entry(fg="black", bg="white", width=50)
entry.grid(row=1, column=0)
#print(entry.get())
button = tkinter.Button(window,text="Click to get text",font=("verdana",9),bg="light grey",state=tkinter.NORMAL)
button.grid(row=1,column=2)
'''

#Demo the usage of check and radio button widget
'''
window.geometry("210x150")
label = tkinter.Label(window,text="please choose your food",font=("verdana",9),bg="white")
label.grid(row=0,column=0,pady=20) #pady is the spacing AFTER the label
cb1 = tkinter.Checkbutton(window,width=15,text="Dosa",font=("verdana",9)) #Default bg takes grey
cb1.grid(row=1,column=0,padx=10)
cb2 = tkinter.Checkbutton(window,width=15,text="Dosa",font=("verdana",9),bg="aqua")
cb2.grid(row=2,column=0,padx=10)
rb1 = tkinter.Radiobutton(window,width=15,text="Dosa",font=("verdana",9),value=0) #Value paramater enables or disables the radio button
rb1.grid(row=3,column=0,padx=10)
rb2 = tkinter.Radiobutton(window,width=15,text="Dosa",font=("verdana",9),bg="aqua",value=1)
rb2.grid(row=4,column=0,padx=10)
'''

#Demo list box widget
'''
window.geometry("210x150")
list_box = tkinter.Listbox(window,height=8) #height represents how elements in the list will be shown in the window
list_box.insert(1,"Dosa")
list_box.insert(2,"Idly")
list_box.insert(3,"Chappati")
list_box.insert(4,"Samosa")
list_box.grid(row=0,column=0)
'''

#Demo frame widget
'''
window.geometry("100x100")
top_frame = tkinter.Frame(window)
top_frame.grid(row=0,column=0)
bot_frame=tkinter.Frame(window)
bot_frame.grid(row=1,column=0)
redbutton = tkinter.Button(top_frame, text = 'Red', fg ='red')
redbutton.grid(row=0, column=0)
greenbutton = tkinter.Button(top_frame, text = 'Green', fg='green')
greenbutton.grid(row=0, column=1)
redbutton = tkinter.Button(top_frame, text = 'Yellow', fg ='yellow')
redbutton.grid(row=0, column=2)
bluebutton = tkinter.Button(bot_frame, text ='Blue', fg ='blue')
bluebutton.grid(row=0, column=0)
blackbutton = tkinter.Button(bot_frame, text ='Black', fg ='black')
blackbutton.grid(row=1, column=2)
'''

#Demo the canvas widget
'''
window.geometry("100x100")
canva = tkinter.Canvas(window, width=80, height=80)
canva.grid()
canva_height=20
canva_width=200
canva.create_line(0,10,canva_width,10) #Learn more about these parameters ???         
'''

#Demo the menu button widget - learn the syntax, not very clear
'''
window.geometry("100x100")
mb = tkinter.Menubutton(window, text= "Menu")
mb.grid()
mb.menu = tkinter.Menu(mb, tearoff = 0)
mb["menu"] = mb.menu
a = tkinter.IntVar()
b = tkinter.IntVar()
mb.menu.add_checkbutton(label ='Contact', variable = a)
mb.menu.add_checkbutton(label = 'About', variable = b)
mb.pack()
'''

#Demo the message box widget
#A Message Box is similar to label widget for showing texts/messages whenever needed.
'''
ourMessage ='This is our Message'
messageVar = tkinter.Message(window, text = "Hello:")
messageVar.config(bg='pink')
messageVar.grid(row =0, column=0 )
'''

#Demo the scale widget
'''
scale = tkinter.Scale(window, from_=0, to=50)
scale.grid()
scale2 = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL)
scale2.grid()
'''

#Demo the scrollbar widget - Learn more about this...
'''
scrollbar = tkinter.Scrollbar(window)
scrollbar.grid(row=0,column=1)
mylist = tkinter.Listbox(window, yscrollcommand = scrollbar.set )
for line in range(50):
    mylist.insert(tkinter.END, 'line number' + str(line))
mylist.grid(row=0,column=0)
scrollbar.config(command = mylist.yview)
'''

#There are other widgets like Text, Spin Box, Message Box - not covering them in detail here



window.mainloop()
