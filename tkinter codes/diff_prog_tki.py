#tkinter hello world program--------------------------------------

"""from tkinter import *

root = Tk()    #will create a window and Tk() is call
label1 = Label(root, text="Hello World") #label
label1.pack() #to add a label to window
root.mainloop()  #for putting up a loop for window"""

#frames-----------------------------------------------------------
"""from tkinter import *

root = Tk()

newframe = Frame(root) #for creating fram
newframe.pack()

secframe = Frame(root)
secframe.pack(side=BOTTOM) #() for specifying the position

button1 = Button(newframe, text = "Click here", fg="Red")
button2 = Button(secframe, text = "Click here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()"""

#Grid layout------------------------------------------------------
"""from tkinter import *

root = Tk()

label1 = Label(root, text="First name")
label2 = Label(root, text="Last name")

entry1 = Entry(root)#accepting user input
entry2 = Entry(root)

label1.grid(row = 0, column = 0)  #for specifying placement in grid
label2.grid(row = 1, column = 0)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

root.mainloop()"""

#self adjusting widgets------------------------------------------------
"""from tkinter import *

root = Tk()

label1 = Label(root, text = "First", bg="Red",fg="Black")
label1.pack(fill=X)  #x width of the window

label2 = Label(root, text = "Second", bg="Black",fg="White")
label2.pack(side = LEFT, fill = Y) #for adjusting column wise

root.mainloop()"""

#handling Button click-----------------------------------------------------
"""from tkinter import *

root = Tk()

def add():
    a = 10
    b = 20
    print(a+b)

button1 = Button(root, text = "DO THE ADDITION", command=add)    
button1.pack()

root.mainloop()"""

#using classes for tkinter---------------------------------------------------

"""from tkinter import *

class Mybuttons:

    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.button1 = Button(frame, text = "Click me", command = self.printmsg)
        self.button1.pack()

        self.button2 = Button(frame, text = "Quit", command =frame.quit) #frame.quit for quitting the frame
        self.button2.pack(side=LEFT)

    def printmsg(self):
        print("Something changed")

        
root = Tk()
b = Mybuttons(root)
root.mainloop()"""

#tkinter using drop down-----------------------------------------------------
"""from tkinter import *

def function1():
    print("click done")
def function2():
    print("2nd click")

def fun3():
    print("Cut done")
def fun4():
    print("Copy done")

root = Tk()

mymenu = Menu(root)    #object of menu
root.config(menu=mymenu)

submenu = Menu(mymenu)  

mymenu.add_cascade(label="File", menu=submenu)  #creating submenu1

submenu.add_command(label="Project", command=function1)  #adding drop down values
submenu.add_command(label="Save", command=function2)
submenu.add_separator()   #for adding separator in drop down values
submenu.add_command(label="Settings", command=function2)

submenu2 = Menu(mymenu) #submenu2

mymenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Cut", command=fun3)
submenu2.add_command(label="Copy", command=fun4)

root.mainloop()"""

#tkinter toolbaar----------------------------------------------------
"""from tkinter import *

def function1():
    print("click done")
def function2():
    print("2nd click")

def fun3():
    print("Cut done")
def fun4():
    print("Copy done")

root = Tk()

mymenu = Menu(root)    #object of menu
root.config(menu=mymenu)

submenu = Menu(mymenu)  

mymenu.add_cascade(label="File", menu=submenu)  #creating submenu1

submenu.add_command(label="Project", command=function1)  #adding drop down values
submenu.add_command(label="Save", command=function2)
submenu.add_separator()   #for adding separator in drop down values
submenu.add_command(label="Settings", command=function2)

submenu2 = Menu(mymenu) #submenu2

mymenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Cut", command=fun3)
submenu2.add_command(label="Copy", command=fun4)


toolbar = Frame(root, bg="Red")     #for creating toolbar
button1 = Button(toolbar, text="Insert", command=function1)
button1.pack(side=LEFT, padx=2, pady=3) #padx and pady for padding

button2 = Button(toolbar, text="Print", command=function1)
button2.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)   #for adding it to menu

root.mainloop()"""


#making status bar------------------------------------------------------
"""from tkinter import *

def function1():
    print("click done")
def function2():
    print("2nd click")

def fun3():
    print("Cut done")
def fun4():
    print("Copy done")

root = Tk()

mymenu = Menu(root)    #object of menu
root.config(menu=mymenu)

submenu = Menu(mymenu)  

mymenu.add_cascade(label="File", menu=submenu)  #creating submenu1

submenu.add_command(label="Project", command=function1)  #adding drop down values
submenu.add_command(label="Save", command=function2)
submenu.add_separator()   #for adding separator in drop down values
submenu.add_command(label="Settings", command=function2)

submenu2 = Menu(mymenu) #submenu2

mymenu.add_cascade(label="Edit", menu=submenu2)
submenu2.add_command(label="Cut", command=fun3)
submenu2.add_command(label="Copy", command=fun4)


toolbar = Frame(root, bg="Red")     #for creating toolbar
button1 = Button(toolbar, text="Insert", command=function1)
button1.pack(side=LEFT, padx=2, pady=3) #padx and pady for padding

button2 = Button(toolbar, text="Print", command=function1)
button2.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)   #for adding it to menu

statusbar = Label(root, text="This is the status bar", bd=1, relief=SUNKEN, anchor=W)
#for creating statusbar

statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()  """

#message box-------------------------------------------------------
"""from tkinter import *
import tkinter.messagebox

root = Tk()
#info showing message box syntax
tkinter.messagebox.showinfo("Warning", "You are not allowed to perform this operation")

#question type message box syntax
respone = tkinter.messagebox.askquestion("Warning", "Do you want to Continue?")
if respone == "yes":
    print("Operation started")
else:
    print("Operation cancelled")
                
root.mainloop()"""

#creating graphics in tkinter-----------------------------------------

from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height=200)  #creates a canvas for drawing
canvas.pack()

newline = canvas.create_line(15, 25, 200, 25)
#creates newline, it requires two co-ordinates set, 1st two are co-ordinates of 1st point and next two are co-ordingates of 2nd point
seconf = canvas.create_line(10,10,50,100, fill="red")
thri = canvas.create_line(300, 35, 300, 200, dash=(4, 2))
#dash represets 4x and 2y space
fou = canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

root.mainloop()
