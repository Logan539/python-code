from tkinter import *
import parser

root = Tk()
root.title("Calculator")

#getting user input
i=0
def get_inp(num):
    global i
    display.insert(i,num)
    i+=1

#for equal to or result
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,"Error")

#clear all function
def clearall():
    display.delete(0,END)

#deleting single element
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clearall()
        display.insert(0,new_string)
    else:
        clearall()
        display.insert(0,"Error")

#for permoring operation
def oper(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length



#adding input feild
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#adding various buttons
Button(root, text="1",command = lambda :get_inp(1)).grid(row=2, column=0)
Button(root, text="2",command = lambda :get_inp(2)).grid(row=2, column=1)
Button(root, text="3",command = lambda :get_inp(3)).grid(row=2, column=2)

Button(root, text="4",command = lambda :get_inp(4)).grid(row=3, column=0)
Button(root, text="5",command = lambda :get_inp(5)).grid(row=3, column=1)
Button(root, text="6",command = lambda :get_inp(6)).grid(row=3, column=2)

Button(root, text="7",command = lambda :get_inp(7)).grid(row=4, column=0)
Button(root, text="8",command = lambda :get_inp(8)).grid(row=4, column=1)
Button(root, text="9",command = lambda :get_inp(9)).grid(row=4, column=2)

Button(root, text="AC",command = lambda :clearall()).grid(row=5, column=0)
Button(root, text="0",command = lambda :get_inp(0)).grid(row=5, column=1)
Button(root, text="=",command = lambda :calculate()).grid(row=5, column=2)

Button(root, text="+",command = lambda :oper("+")).grid(row=2, column=3)
Button(root, text="-",command = lambda :oper("-")).grid(row=3, column=3)
Button(root, text="*",command = lambda :oper("*")).grid(row=4, column=3)
Button(root, text="/",command = lambda :oper("/")).grid(row=5, column=3)

#adding new operations
Button(root, text="pi",command = lambda :oper("*3.14")).grid(row=2, column=4)
Button(root, text="%",command = lambda :oper("%")).grid(row=3, column=4)
Button(root, text="(",command = lambda :oper("(")).grid(row=4, column=4)
Button(root, text="exp",command = lambda :oper("**")).grid(row=5, column=4)

Button(root, text="<-",command = lambda :undo()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")",command = lambda :oper(")")).grid(row=4, column=5)
Button(root, text="^2",command = lambda :oper("**2")).grid(row=5, column=5)

root.mainloop()