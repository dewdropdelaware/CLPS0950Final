print('This is CLPS0950 Final Project')
print('Did this work?')
print ('yes')

def answer_question(ans, prop, database):
    if ans == "y":
        ans = True
    elif ans == "n":
        ans = False
    else:
        ans = True or False

    filtered_database = []
    #import pdb;pdb.set_trace()
    for d in database:
      if d[prop] == ans:
            filtered_database.append(d)

    print(len(filtered_database))
    return filtered_database
database = [{'name': "Poke Works", 'Thayer': True, 'latenight': False, 'coffee': False, 'dessert': False, 'new': True, 'servers': False, 'price': True, 'snackpass': True, 'words': True, 'outside': True, 'pizza': False},
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

ans = input("Is your restaurant actually on Thayer (y/n/idk): ")
database = answer_question(ans, 'Thayer', database)
print(len(database))
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])

ans = input("Is your restaurant open past midnight (y/n/idk): ")
database = answer_question(ans, 'latenight', database)
print(len(database))
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Does your restaurant serve coffee (y/n/idk): ")
database = answer_question(ans, 'coffee', database)
print(len(database))
if len(database) == 1:
 print("Your restaurant is " + database[0]["name"])
ans = input("Does your restaurant primarily serve dessert (y/n/idk): ")
database = answer_question(ans, 'dessert', database)
print(len(database))
if len(database) == 1:
 print("Your restaurant is " + database[0]["name"]) 

ans = input("Is your restaurant newer (y/n/idk): ")
database = answer_question(ans, 'new', database)
print(len(database))
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Does your restaurant have servers (y/n/idk): ")
database = answer_question(ans, 'servers', database)
print(len(database))
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Do you expect to spend over $15 when you come (y/n/idk): ")
database = answer_question(ans, 'price', database)
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Is your restaurant on snackpass (y/n/idk): ")
database = answer_question(ans, 'snackpass', database)
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Is your restaurant more than one word (y/n/idk): ")
database = answer_question(ans, 'words', database)
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Can you find this restaurant outside of Providence (y/n/idk): ")
database = answer_question(ans, 'outside', database)
if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
ans = input("Does your restaurant serve pizza (y/n/idk): ")
database = answer_question(ans, 'pizza', database)

if len(database) == 1:
    print("Your restaurant is " + database[0]["name"])
else:
    print("Could not identify a restaurant based on the provided criteria.")