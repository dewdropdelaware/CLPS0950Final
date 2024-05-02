from tkinter import *

#creating a graphical user interface(GUI) for our game to exist in
open = Tk()

myLabel = Label(open, text = 'This is our CLPS0950 Final Project')
myLabel1 = Label(open, text = 'Are you ready to get started?')
myLabel.pack()
myLabel1.pack()

#defining a function to the click
def myClick():
    startLabel = Label(open, text = 'Hello and welcome to this new game called the Restaurantators!')
    startLabel1 = Label(open, text = 'Think of your favorite restaurant on campus.')
    startLabel2 = Label(open, text = 'When you got it, click the start button')
    startLabel.pack()
    startLabel1.pack()
    startLabel2.pack()
    #entry widgets are used intead of inputs on tkinter
    #e = Entry(open)
    #e.pack()
    #e.get() to retrieve entry

    myButton2 = Button(open, text = 'Start',command=answer_questions, fg = 'black', bg = 'green')
    myButton2.pack()

def answer_questions():
    labell = Label(open, text = 'jello')
    labell.pack()

#calling the function in the button, so don't put the ()
myButton = Button(open, text="Yeah!", command=myClick, fg = 'black', bg = 'yellow')
myButton.pack()


open.mainloop()

