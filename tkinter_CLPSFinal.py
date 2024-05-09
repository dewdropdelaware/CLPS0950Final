# restaurants = [{"Name": 'Hi',"Pink": True, "Blue":False, "Green":False}, {"Name": 'Bye', "Pink": True, "Blue":True, "Green":True},
#                {"Name": 'Adios' , "Pink": False, "Blue": False, "Green": False}, {"Name": 'Hola', "Pink": True, "Blue": False, "Green": True}]

# #creating a graphical user interface(GUI) for our game to exist in
# open = Tk()
# open.title("The Restaurantators")
# current_row = 0

# myLabel = Label(open, text = 'This is our CLPS0950 Final Project')
# myLabel1 = Label(open, text = 'Are you ready to get started?')
# myLabel.grid(row = 0, column = 0, padx = 5)
# myLabel1.grid(row = 0, column = 1)

# def myClick():
#     myButton2 = Button(open, text = 'Start',command=myClicks, fg = 'black', bg = 'green')
#     myButton2.grid(row = 6, columnspan =2)
    
#     startLabel = Label(open, text = 'Hello and welcome to this new game called the Restaurantators!')
#     startLabel1 = Label(open, text = 'Think of your favorite restaurant on campus.')
#     startLabel2 = Label(open, text = 'When you got it, click the start button')
#     startLabel.grid(row = 3, columnspan = 2)
#     startLabel1.grid(row = 4, columnspan = 2)
#     startLabel2.grid(row = 5, columnspan = 2)
    
# def myClicks():  
#     ask_next_question(0)
    
# def ask_question(question_text,current_row):

#     Label(open, text=question_text).grid(row=current_row, pady=5)
#     e = Entry(open)
#     e.grid(row=current_row, column=1, padx=5, pady=5)
#     # Waiting for user input
#     def on_button_click():
#         s = e.get()
#         if s in ['0', '1']:
#             return s
#         else:
#             # Handle invalid input
#             Label(open, text = "Error, Please enter either '0' or '1'").grid(row = current_row + 1)
    
#     myButton = Button(open, text="Enter", command=on_button_click)
#     myButton.grid(row=current_row, column=2)
#     return e.get(), current_row + 1

# #creating a loop by using function recursion where a function is called within itself
# #(Acessed ChatGPT on 5/9/23)
# def ask_next_question(question_index):
#     global current_row
#     while question_index < len(q):
#         s = ask_question('Is your restaurant' + q[question_index] + '?' + 'yes = 1, no = 0', current_row)
#         #current_row = current_row + 1
        
#         if s in ['0', '1']:
#             process_entry(s)
#             ask_next_question(question_index + 1)

#     your_restaurant_is()
        
# def process_entry(s):
#     global x, LA
#     for ii in range(len(q)):
#         x = np.array(x)
#         row = LA[:,ii]
#         if ii> len(row)-1:
#             continue 
#         if float(s) != row[ii]:
#                 #indexes of where the row equals the floats
#                 answer_book= np.where(row!=float(s))
#                 LA = np.delete(LA, answer_book, 0)
#                 x = np.delete(x, answer_book)
                

# #method one using entries like in the other code to run the loop
# def your_restaurant_is():
#     if len(LA) == 1:
#         return Label(open, text = 'Your restaurant is:' + x[0]).grid(row = current_row)         
#     else:        
#         return Label(open, text = "Could not identify your restaurant").grid(row = current_row)

# #calling the function in the button, so don't put the ()
# myButton = Button(open, text="Yeah!", width = 40, command=myClick, fg = 'black', bg = 'yellow')
# myButton.grid(row = 2, columnspan = 2)

# question_index = 0
# x = []
# q = []
# LA = np.zeros((4,3))

# for i,d in enumerate(restaurants):
#  x.append(d["Name"]) #i is each dictionary

#  for j,k in enumerate(d.items()):
#   if k[0] == "Name":
#     continue
#   else:
#       if k[0] not in q:
#         q.append(k[0])
#       LA[i,j-1] = k[1]

# open.mainloop()




# import numpy as np
# from tkinter import *

# # Define restaurants data
# restaurants = [
#     {"Name": 'Hi', "Pink": True, "Blue": False, "Green": False},
#     {"Name": 'Bye', "Pink": True, "Blue": True, "Green": True},
#     {"Name": 'Adios', "Pink": False, "Blue": False, "Green": False},
#     {"Name": 'Hola', "Pink": True, "Blue": False, "Green": True}
# ]

# class RestaurantatorApp:
#     def __init__(self, master):
#         self.master = master
#         master.title("The Restaurantators")
#         self.current_row = 0
#         self.x = []
#         self.q = []
#         self.LA = np.zeros((4, 3))

#         # Create initial labels and button
#         self.create_initial_widgets()

#     def create_initial_widgets(self):
#         self.label = Label(self.master, text='This is our CLPS0950 Final Project')
#         self.label.grid(row=0, column=0, padx=5)

#         self.label1 = Label(self.master, text='Are you ready to get started?')
#         self.label1.grid(row=0, column=1)

#         self.button = Button(self.master, text="Yeah!", width=40, command=self.start_game, fg='black', bg='yellow')
#         self.button.grid(row=2, columnspan=2)

#     def start_game(self):
#         self.button.destroy()
#         self.label.destroy()
#         self.label1.destroy()

#         self.start_label = Label(self.master, text='Hello and welcome to this new game called the Restaurantators!')
#         self.start_label.grid(row=3, columnspan=2)

#         self.start_label1 = Label(self.master, text='Think of your favorite restaurant on campus.')
#         self.start_label1.grid(row=4, columnspan=2)

#         self.start_label2 = Label(self.master, text='When you got it, click the start button')
#         self.start_label2.grid(row=5, columnspan=2)

#         self.start_button = Button(self.master, text='Start', command=self.ask_first_question, fg='black', bg='green')
#         self.start_button.grid(row=6, columnspan=2)

#     def ask_first_question(self):
#         self.start_button.destroy()
#         self.ask_next_question(0)

#     def ask_next_question(self, question_index):
#         if question_index < len(self.q):
#             self.ask_question('Is your restaurant ' + self.q[question_index] + '? (yes = 1, no = 0)', question_index)
#         else:
#             self.your_restaurant_is()

#     def ask_question(self, question_text, question_index):
#         Label(self.master, text=question_text).grid(row=self.current_row, column=0, columnspan=2, pady=5)
#         self.entry = Entry(self.master)
#         self.entry.grid(row=self.current_row + 1, column=0, padx=5, pady=5)

#         def on_button_click():
#             user_input = self.entry.get()
#             if user_input in ['0', '1']:
#                 self.process_entry(user_input, question_index)
#                 self.ask_next_question(question_index + 1)
#             else:
#                 self.error_label = Label(self.master, text="Error: Please enter either '0' or '1'")
#                 self.error_label.grid(row=self.current_row + 2, column=0, columnspan=2)
    
#         button = Button(self.master, text="Enter", command=on_button_click)
#         button.grid(row=self.current_row + 2, column=0, columnspan=2)
#         self.current_row += 3

#     def process_entry(self, user_input, question_index):
#         for ii in range(len(self.q)):
#             self.x = np.array(self.x)
#             row = self.LA[:, ii]
#             if ii > len(row) - 1:
#                 continue
#             if float(user_input) != row[ii]:
#                 answer_book = np.where(row != float(user_input))
#                 self.LA = np.delete(self.LA, answer_book, 0)
#                 self.x = np.delete(self.x, answer_book)

#     def your_restaurant_is(self):
#         if len(self.LA) == 1:
#             Label(self.master, text='Your restaurant is: ' + self.x[0]).grid(row=self.current_row, columnspan = 2)
#         else:
#             Label(self.master, text="Could not identify your restaurant").grid(row=self.current_row, columnspan =2)


# def main():
#     root = Tk()
#     app = RestaurantatorApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import numpy as np
from tkinter import *

open = Tk()
open.title("Items mini")

myLabel = Label(open, text = 'This is our CLPS0950 Final Project')
myLabel1 = Label(open, text = 'Are you ready to get started?')
myLabel.grid(row = 0)
myLabel1.grid(row = 1)

#When "Yeah" Button is clicked
def myClick():
    startLabel = Label(open, text = 'Hello and welcome to this new game called Items Mini!')
    startLabel1 = Label(open, text = 'Choose one of the following items:')
    startLabel2 = Label (open, text = '[Orange, Starburst, Watermelon, Candy]')
    startLabel3 = Label(open, text = 'When you got it, click the start button')
    startLabel.grid(row = 3)
    startLabel1.grid(row = 4)
    startLabel2.grid(row = 4, column = 1)
    startLabel3.grid(row = 5)

    myButton2 = Button(open, text = 'Start',command=answer_questions, fg = 'black', bg = 'green')
    myButton2.grid(row = 6)

#calling the function in the button, so don't put the ()
myButton = Button(open, text="Yeah!", command=myClick, fg = 'black', bg = 'yellow')
myButton.grid(row = 2)

#when the 'pink' button is clicked
def button_pushed(s):
    x = np.array(names)
    #these are the inputs of each colums put into a row
    row = array[:,0]

    for ii in range(0, len(row)):
        if ii > len(row) - 1:
            continue
        if s != '':
                
            if float(s) != row[ii]:
                #indexes of where the row equals the floats
                answer_book= np.where(row!=float(s))
                LA = np.delete(array, answer_book, 0)
                x = np.delete(x, answer_book)
                #changing the question, so looking at a new column
                row = LA[:,1]
                
                if len(LA) == 1:
                    Answer = Label(open, text = "Your item is:" + '' + x[0])
                    Answer.grid(row = 8)
                    return
                else:
                    def button_clicked():
                        k = Blue_Entry.get() 
                        button_down(k,x, LA)
                    Blue_label = Label(open, text = 'Is your item blue? (yes = 1 / no  = 0)')
                    Blue_label.grid(row = 8)
                    Blue_Entry = Entry(open, bg = 'skyblue')
                    Blue_Entry.grid(row = 8, column = 1, padx = 5)
                    Blue_Button = Button(open, text = 'Enter', command = button_clicked, bg = 'skyblue')
                    Blue_Button.grid(row = 8, column = 2)
                    
        else: print('oh no')
#when blue button is clicked                
def button_down(k,x, LA):
    row = LA[:,1]
    
    for ii in range(0, len(row)):
        if ii > len(row) - 1:
            continue
        if k != '':
            
            if float(k) != row[ii]:
                answer_book= np.where(row!=float(k))
                LA = np.delete(LA, answer_book, 0)
                x = np.delete(x, answer_book)
                row = LA[:,2]
                
                if len(LA) ==1:
                    Answer = Label(open, text = 'Your item is:' + '' + x[0])
                    Answer.grid(row =9)
                    return
                else:
                    def button_clicked():
                        y = Green_Entry.get() 
                        button_tap(y,x, LA)
                    
                    Green_Label = Label(open, text = 'Is your item green? (yes = 1 / no = 0)')
                    Green_Label.grid(row=9)
                    Green_Entry = Entry(open, bg ='pale green')
                    Green_Entry.grid(row =9 , column = 1, padx = 5)
                    Green_Button = Button(open, text = 'Enter', command = button_clicked, bg = 'pale green')
                    Green_Button.grid(row=9, column = 2)
        else: print('oh no')

#when green button is clicked and answer generated
def button_tap(y, x, LA):
    row = LA[:,2]
    for ii in range(0, len(row)):
        if ii > len(row) - 1:
            continue
        if y != '':
            
            if float(y) != row[ii]:
                answer_book= np.where(row!=float(y))
                LA = np.delete(LA, answer_book, 0)
                x = np.delete(x, answer_book)          

                Answer = Label(open, text = 'Your item is:' + '' + x[0])
                Answer.grid(row =10)
                return
                
        else: print('oh no')
    

#when start button is clicked creates the pink group   
def answer_questions():
#Also when pink button is pushed
    def button_clicked():
        s = Pink_Entry.get()
        button_pushed(s)
    labell = Label(open, text = 'Is your item pink? (yes = 1 / no = 0)')
    labell.grid(row = 7 )
    Pink_Entry = Entry(open, bg = 'pink')
    Pink_Entry.grid(row=7, column = 1, padx = 5)
    Pink_Button = Button(open, text = 'Enter', command = button_clicked, bg = 'pink')
    Pink_Button.grid(row = 7, column = 2)

restaurants = [{"Name": 'Starbursts',"Pink": True, "Blue":False, "Green":False}, {"Name": 'Candy', "Pink": True, "Blue":True, "Green":True},
               {"Name": 'Orange' , "Pink": False, "Blue": False, "Green": False}, {"Name": 'Watermelon', "Pink": True, "Blue": False, "Green": True}]
q = []
names = []
answer_book =[]
array = np.zeros((4,3))

for i,d in enumerate(restaurants):
    names.append(d["Name"]) #i is each dictionary
    for j,k in enumerate(d.items()):
        if k[0] == "Name":
            continue
        else:
            if k[0] not in q:
                q.append(k[0])
            array[i,j-1] = k[1]
open.mainloop()
