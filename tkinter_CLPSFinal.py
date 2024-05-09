from tkinter import *
import numpy as np

restaurants = [{'name': "Poke Works", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': True, 'servers': False, 'price': True, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "In The Pink", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': False, 'new': True, 'servers': False, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Ben and Jerry's", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Mala Noodles", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': True, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "La Creperie", 'Thayer': False, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Starbucks", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': False, 'outside': True, 'pizza': False},
    {"name": "Ten One Tea House", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Al Shami", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Kabob and Curry", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Bajas Taqueria", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Bajas Tex Mex Grill", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "East Side Pockets", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Shake Shack", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Chipotle", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': False, 'outside': True, 'pizza': False},
    {"name": "Calientes", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': False, 'outside': True, 'pizza': False},
    {"name": "Chinatown", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': False, 'outside': False, 'pizza': False},
    {"name": "Yas Chicken", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': True, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Antonio's Pizza",'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Shaking Crab", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': True, 'servers': True, 'price': True, 'snackpass': False, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Mikes Calzones and Deli", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': False, 'pizza': True},
    {"name": "Sydney", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': False, 'new': True, 'servers': False, 'price': False, 'snackpass': False, 'words': False, 'outside': False, 'pizza': False},
    {"name": "Aroma Joes", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Andreas", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': False, 'words': False, 'outside': False, 'pizza': False},
    {"name": "Kung Fu Tea", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Vivi's", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': False, 'outside': True, 'pizza': False},
    {"name": "Insomnia", 'Thayer': True, 'latenight': True, 'coffee': False, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Tiger Sugar", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': True, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
    {"name": "Flatbread", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': False, 'words': False, 'outside': True, 'pizza': True},
    {"name": "Heng Thai", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Den Den", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': False, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Peri Peri", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': True,'pizza': False},
    {"name": "Ceremony", 'Thayer': False, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': False, 'words': False, 'outside': False, 'pizza': False},
    {"name": "Dadadurki", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': False, 'outside': False, 'pizza': False},
    {"name": "Bagel Gourmet Ole", 'Thayer': True, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Meeting Street Cafe",  'Thayer': False, 'latenight': False, 'coffee': True, 'dessert': False, 'new': False, 'servers': True, 'price': True, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Wongs Kitchen", 'Thayer': False, 'latenight': False, 'coffee': False, 'dessert': False, 'new': False, 'servers': False, 'price': False, 'snackpass': True, 'words': True, 'outside': False, 'pizza': False},
    {"name": "Zinnekens", 'Thayer': False, 'latenight': False, 'coffee': True, 'dessert': True, 'new': True, 'servers': True, 'price': False, 'snackpass': True, 'words': False, 'outside': True, 'pizza': False},
    {"name": "Feed the Cheeks",'Thayer': False, 'latenight': False, 'coffee': True, 'dessert': True, 'new': True, 'servers': False, 'price': False, 'snackpass': False, 'words': True, 'outside': False, 'pizza': False}
    ]

a = len(restaurants[0])
LA = np.zeros((len(restaurants), (a-1)))

x = []
q = []

for i,d in enumerate(restaurants):
    x.append(d["name"])
    for j,k in enumerate(d.items()):
        if k[0] == "name":
            continue
        else:
            if k[0] not in q:
                q.append(k[0])
            LA[i,j-1] = k[1] 
#creating a graphical user interface(GUI) for our game to exist in
open = Tk()
open.title("The Restaurantators")

myLabel = Label(open, text = 'This is our CLPS0950 Final Project')
myLabel1 = Label(open, text = 'Are you ready to get started?')
myLabel.grid(row = 0, column = 0, padx = 5)
myLabel1.grid(row = 0, column = 1)

def myClick():
    myButton2 = Button(open, text = 'Start',command=answer_questions, fg = 'black', bg = 'green')
    myButton2.grid(row = 6, columnspan =2)
    
    startLabel = Label(open, text = 'Hello and welcome to this new game called the Restaurantators!')
    startLabel1 = Label(open, text = 'Think of your favorite restaurant on campus.')
    startLabel2 = Label(open, text = 'When you got it, click the start button')
    startLabel.grid(row = 3, columnspan = 2)
    startLabel1.grid(row = 4, columnspan = 2)
    startLabel2.grid(row = 5, columnspan = 2)

def answer_question(x, q, LA):
    answer_book =[]
    for ii in range(0,len(q)):
        x = np.array(x)
        Label(open, text = 'Is your restaurant' + q[ii] + '?').grid(row = 8+ii, pady = 5)
        Button(open, text = 'Yes').grid(row = 8+ii, column =1, padx = 5, pady = 5)
        Button(open, text = 'No').grid(row = 8+ii, column =2, padx = 150, pady = 5)
        Button(open, text = "Don't Know").grid(row = 8+ ii, column =3, pady = 5)
    
        def boolean():
            qans = Button.cget('text')
            if qans == 'Yes':
                ans = '1'
            elif qans == 'No':
                ans = '0'
            else:
                ans = 'idk' 
            Label(open, text = 'Cool').grid()
            return ans 
    
        s = boolean
        if s not in ['0', '1']:
            continue
        
    #these are the inputs of each colums put into a row
        row = LA[:,ii]

        for jj in range(0, len(row)):
            if jj> len(row)-1:
                continue 
            if float(s) != row[jj]:
                #indexes of where the row equals the floats
                answer_book= np.where(row!=float(s))
                LA = np.delete(LA, answer_book, 0)
                x = np.delete(x, answer_book)
                row = LA[:,ii]

            if len(LA) == 1:
                Label(open, text = 'Your restaurant is:' + x[0]).grid()
            return          
        return print("Could not identify your restaurant")
    
def answer_questions():
     answer_question(x,q,LA)

#calling the function in the button, so don't put the ()
myButton = Button(open, text="Yeah!", width = 40, command=myClick, fg = 'black', bg = 'yellow')
myButton.grid(row = 2, columnspan = 2)

    #entry widgets are used intead of inputs on tkinter
    #e = Entry(open)
    #e.pack()
    #e.get() to retrieve entry

open.mainloop()

