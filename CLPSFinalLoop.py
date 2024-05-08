print('This is CLPS0950 Final Project')


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


## REDEFINING OUR DATABASE AS AN ARRAY OF 1, 0
import numpy as np
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
print(LA)  

#DEFINING OUR FUNCTION so we only have to run it once
def answer_question(x, q, LA):
  answer_book =[]
  for ii in range(0,len(q)):
    x = np.array(x)
    s = input("Is your restaurant " + q[ii] + "?")
    #these are the inputs of each colums put into a row
    row = LA[:,ii]

    #this will not go through the indices of the row
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
          print("Your restaurant is:" + x[0])
          return          
                
""" def answer_question(qans, prop, database):
    if qans == "y":
        boolean = True
    elif qans == "n":
        boolean = False
    else:
        return database


    filtered_database = []
    for d in database:
        if d[prop] == boolean:
            filtered_database.append(d)


    if len(filtered_database) == 1:
        print("Your restaurant is " + filtered_database[0]["name"])
        exit()

    return filtered_database


ans = input("Is your restaurant actually on Thayer (y/n/idk): ")
restaurants1 = answer_question(ans, 'Thayer', restaurants)

ans = input("Is your restaurant open past midnight (y/n/idk): ")
restaurants2 = answer_question(ans, 'latenight', restaurants1)

ans = input("Does your restaurant serve coffee (y/n/idk): ")
restaurants3 = answer_question(ans, 'coffee', restaurants2)

ans = input("Does your restaurant primarily serve dessert (y/n/idk): ")
restaurants4 = answer_question(ans, 'dessert', restaurants3)

ans = input("Is your restaurant newer (y/n/idk): ")
restaurants5 = answer_question(ans, 'new', restaurants4)

ans = input("Does your restaurant have servers (y/n/idk): ")
restaurants6 = answer_question(ans, 'servers', restaurants5)

ans = input("Do you expect to spend over $15 when you come (y/n/idk): ")
restaurants7 = answer_question(ans, 'price', restaurants6)

ans = input("Is your restaurant on snackpass (y/n/idk): ")
restaurants8 = answer_question(ans, 'snackpass', restaurants7)

ans = input("Is your restaurant more than one word (y/n/idk): ")
restaurants9 = answer_question(ans, 'words', restaurants8)

ans = input("Can you find this restaurant outside of Providence (y/n/idk): ")
restaurants10 = answer_question(ans, 'outside', restaurants9)

ans = input("Does your restaurant serve pizza (y/n/idk): ")
restaurants11 = answer_question(ans, 'pizza', restaurants10) """

#if len(restaurants) == 1:
    #print("Your restaurant is " + restaurants[0]["name"])
#else:
    #print("Could not identify a restaurant based on the provided criteria.")
answer_question(x, q, LA)