print('This is CLPS0950 Final Project')


restaurants = [{'name': "Poke Works", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': True, 'with servers': False, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "In The Pink", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': True, 'with servers': False, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Ben and Jerry's", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Mala Noodles", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': True, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "La Creperie", 'on Thayer': False, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Starbucks", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': False, 'outside': True, 'pizza serving': False},
    {"name": "Ten One Tea House", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Al Shami", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Kabob and Curry", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Bajas Taqueria", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Bajas Tex Mex Grill", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "East Side Pockets", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Shake Shack", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Chipotle", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': False, 'outside': True, 'pizza serving': False},
    {"name": "Calientes", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': False, 'outside': True, 'pizza serving': False},
    {"name": "Chinatown", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': False, 'outside': False, 'pizza serving': False},
    {"name": "Yas Chicken", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': True, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Antonio's Pizza",'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Shaking Crab", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': True, 'with servers': True, 'high price': True, 'on snackpass': False, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Mikes Calzones and Deli", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': True},
    {"name": "Sydney", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': True, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': False, 'outside': False, 'pizza serving': False},
    {"name": "Aroma Joes", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Andreas", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': False, 'multiple words': False, 'outside': False, 'pizza serving': False},
    {"name": "Kung Fu Tea", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Vivi's", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': False, 'outside': True, 'pizza serving': False},
    {"name": "Insomnia", 'on Thayer': True, 'latenight': True, 'coffee serving': False, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Tiger Sugar", 'on Thayer': True, 'latenight': False, 'coffee serving': False, 'primarily dessert': True, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': True, 'pizza serving': False},
    {"name": "Flatbread", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': False, 'multiple words': False, 'outside': True, 'pizza serving': True},
    {"name": "Heng Thai", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Den Den", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': False, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Peri Peri", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': True,'pizza serving': False},
    {"name": "Ceremony", 'on Thayer': False, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': False, 'outside': False, 'pizza serving': False},
    {"name": "Dadadurki", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': False, 'outside': False, 'pizza serving': False},
    {"name": "Bagel Gourmet Ole", 'on Thayer': True, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Meeting Street Cafe",  'on Thayer': False, 'latenight': False, 'coffee serving': True, 'primarily dessert': False, 'new': False, 'with servers': True, 'high price': True, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Wongs Kitchen", 'on Thayer': False, 'latenight': False, 'coffee serving': False, 'primarily dessert': False, 'new': False, 'with servers': False, 'high price': False, 'on snackpass': True, 'multiple words': True, 'outside': False, 'pizza serving': False},
    {"name": "Zinnekens", 'on Thayer': False, 'latenight': False, 'coffee serving': True, 'primarily dessert': True, 'new': True, 'with servers': True, 'high price': False, 'on snackpass': True, 'multiple words': False, 'outside': True, 'pizza serving': False},
    {"name": "Feed the Cheeks",'on Thayer': False, 'latenight': False, 'coffee serving': True, 'primarily dessert': True, 'new': True, 'with servers': False, 'high price': False, 'on snackpass': False, 'multiple words': True, 'outside': False, 'pizza serving': False}
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

#DEFINING OUR FUNCTION so we only have to run it once
def answer_question(x, q, LA):
  answer_book =[]
  for ii in range(0,len(q)):
    x = np.array(x)
    s = input("Is your restaurant " + q[ii] + "?" + "(yes = 1 / no = 0)")
    
    # if input is not 1 or 0, curtesy of chatGPT loop continues on to the next iteration
    if s not in ['0', '1']:
        print("Hmm? ...Making things tricky")
        continue
        
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
  return print("Could not identify your restaurant")

#if len(restaurants) == 1:
    #print("Your restaurant is " + restaurants[0]["name"])
#else:
    #print("Could not identify a restaurant based on the provided criteria.")
answer_question(x, q, LA)
