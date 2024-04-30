from tkinter import *

#creating a graphical user interface(GUI) for our game to exist in
open = Tk()

myLabel = Label(open, text = 'This is our CLPS0950 Final Project')
myLabel.pack()

#defining a function to the click
def myClick():
    startLabel = Label(open, text = 'Try thinking of your favorite a restaurant near campus!')
    startLabel.pack()
    #entry widgets are used intead of inputs on tkinter
    e = Entry(open)
    e.pack()

#calling the function in the button, so don't put the ()
myButton = Button(open, text="Start!", command=myClick, fg = 'black', bg = 'green')
myButton.pack()

open.mainloop()

