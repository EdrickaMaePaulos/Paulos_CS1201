#Edricka Mae H. Paulos
#CS1201


drinks_lib = {
  'Barako Brew' : {'size' : 12, 'cost' : 109},
  'Hot Americano' : {'size' : 12, 'cost' : 129},
  'Hot Cappuccino' : {'size' : 12, 'cost' : 140},
  'Hot Cafe Latte' : {'size' : 12, 'cost' : 149},
  'Hot Caramel Macchiato' : {'size' : 12, 'cost' : 159},
  'Pure Chamomile' : {'size' : 12, 'cost' : 99},
  'Hot Choco' : {'size' : 12, 'cost' : 159},
  'Caramel Macchiato' : {'size' : 16, 'cost' : 169},
  'Americano' : {'size' : 16, 'cost' : 129},
  'Salted Caramel Latte' : {'size' : 16, 'cost' : 169},
  'Mocha Latte' : {'size' : 16, 'cost' : 179},
  'Green Apple Italian Soda' : {'size' : 16, 'cost' : 139},
  'Super Berries Italian Soda' : {'size' : 16, 'cost' : 139},
  'Caramel Creamy Frappe' : {'size' : 16, 'cost' : 189},
  'Chocolate Creamy Frappe' : {'size' : 16, 'cost' : 189},
  'Crushed Oreo Creamy Frappe' : {'size' : 16, 'cost' : 189},
  'Strawberry Creamy Frappe' : {'size' : 16, 'cost' : 189},
  'Matcha Creamy Frappe' : {'size' : 16, 'cost' : 189},
  'Mango Creamy Shake' : {'size' : 16, 'cost' : 169},
  'Avocado Creamy Shake' : {'size' : 16, 'cost' : 169}
}

ricebowl_lib = {
  'Sisig Bowl' : {'cost' : 209},
  'Spamsilog' : {'cost' : 209},
  'Bangsilog' : {'cost' : 209},
  'Dimsum Rice Meals' : {'cost' : 209},
  'Solo Baby Back Ribs' : {'cost' : 309}
}

pasta_lib = {
  'Asian Noodles' : {'cost' : 189},
  'Carbonara' : {'cost' : 189},
  'Italian Spaghetti' : {'cost' : 189},
  'Tuna Pasta' : {'cost' : 189},
  'Lasagna' : {'cost' : 189}
}

pizza_lib = {
  'Hawaiian' : {'cost' : 399},
  'Pepperoni' : {'cost' : 399},
  'Overload' : {'cost' : 399}
}

pastries_lib = {
  'Cinnamon Bun' : {'cost' : 69},
  'Korean Bun' : {'cost' : 69},
  'Blue Berry Cheesecake' : {'cost' : 69},
  'Burnt Basque Cheesecake' : {'cost' : 69}
}

addons_lib = {
  'Rice' : {'cost' : 25},
  'Garlic Rice' : {'cost' : 35},
  'Egg' : {'cost' : 18},
  'Shanghai' : {'cost' : 55}
}

user_acc = {}
user_bag = {}

def menu():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n------------------------------------------------------------- MENU ----------------------------------------------------------------- ")
  print ("\nDRINKS:")
  for drinks in drinks_lib:
    print(f"\t{drinks:50}Size: {drinks_lib[drinks]['size']} oz\t\t\tCost: P {drinks_lib[drinks]['cost']}.00")
  print ("\nRICE BOWLS:")
  for ricebowl in ricebowl_lib:
    print(f"\t{ricebowl:50}Cost: P {ricebowl_lib[ricebowl]['cost']}.00")
  print ("\nPASTA:")
  for pasta in pasta_lib:
    print(f"\t{pasta:50}Cost: P {pasta_lib[pasta]['cost']}.00")
  print ("\nPIZZA:")
  for pizza in pizza_lib:
    print(f"\t{pizza:50}Cost: P {pizza_lib[pizza]['cost']}.00")
  print ("\nPASTRIES:")
  for pastries in pastries_lib:
    print(f"\t{pastries:50}Cost: P {pastries_lib[pastries]['cost']}.00")
  print ("\nADD-ONS:")
  for addons in addons_lib:
    print(f"\t{addons:50}Cost: P {addons_lib[addons]['cost']}.00")

  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter 1 to return: "))
  while True:
    try:
      if choice == 1: 
        main_menu()
      else:
        print ("Invalid")
        menu()
        break
    except ValueError as e:
          print(e)



def register():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n---------------------------------------------------------- REGISTER ------------------------------------------------------------ ")
  username = input("Enter Username: ")

  if username in user_acc:
    print ("Username already existing")
    register()
  else:
    password = input("Enter Password: ")
    password1 = input("Re-Enter Password: ")
    balance = 0
    points = 0

    user_acc[username] = {
      'password' : password,
      'balance' : balance,
      'points' : points
    }

    if password == password1: 
      print("\nRegister Complete!")
      print ("________________________________________________________________________________________________________________________________")
      choice = int(input("Enter 1 to return: "))
      while True:
        try:
          if choice == 1: 
            main_menu()
          else:
            print ("Invalid")
            register()
            break
        except ValueError as e:
          print(e)
    else:
      print ("Invalid Input")
      register()

def customer_login():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n-------------------------------------------------------- CUSTOMER LOG-IN ------------------------------------------------------- ")
  username = input("Username: ")
  password = input("Password: ")

  if username in user_acc and user_acc[username]['password'] == password:
    print(f"Welcome {username}")
    user_menu(username)
  else:
    print("Wrong Username or Password\n")
    customer_login()


def user_menu(username):
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n------------------------------------------------------- CUSTOMER MAIN MENU ----------------------------------------------------- ")
  print ("\t [1] Menu")
  print ("\t [2] Order Food")
  print ("\t [3] Wallet")
  print ("\t [4] Check Bag")
  print ("\t [5] Check Points")
  print ("\t [6] Exit")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your Choice: "))
  while True:
    try: 
      if choice == 1:
        menu()
      elif choice == 2: 
        order_food(username)
      elif choice == 3:
        wallet(username)
      elif choice == 4: 
        check_bag(username)
      elif choice == 5:
        check_points(username)
      elif choice == 6: 
        print ("Thank you")
        main_menu()
      else:
        print ("Invalid Input")
        user_menu()
        break
    except ValueError as e:
      print (e)

def order_food(username):
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n----------------------------------------------------------- ORDER FOOD --------------------------------------------------------- ")
  print ("\t [1] Drinks")
  print ("\t [2] Rice Bowl")
  print ("\t [3] Pasta")
  print ("\t [4] Pizza")
  print ("\t [5] Pastries")
  print ("\t [6] Add-ons")
  print ("\t [7] Return")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your Choice: "))

  while True:
    try:
      if choice == 1:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n----------------------------------------------------------- DRINKS ------------------------------------------------------------- ")
        for drinks in drinks_lib:
          print(f"\n\t{drinks:50}Size: {drinks_lib[drinks]['size']} oz\t\t\tCost: P {drinks_lib[drinks]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        drinks = input("Enter your Choice of drinks (Enter 1 to return): ")
        if drinks in drinks_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * drinks_lib[drinks]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = {'order' : {'drinks name' : drinks, 'quantity' : quantity, 'cost' : total} }
            else:
              user_bag[username].append(drinks)
              print(f"\nSuccessfully ordered {drinks}")
          else: 
            print("\nInsufficient Balance")
        elif drinks == 1:
          return
        else:
          print("Invalid Input")
          break
      elif choice == 2:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n--------------------------------------------------------- RICE BOWLS ----------------------------------------------------------- ")
        for ricebowl in ricebowl_lib:
          print(f"\n\t{ricebowl:50}Cost: P {ricebowl_lib[ricebowl]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        ricebowl = input("Enter your Choice of rice bowl (Enter 1 to return): ")
        if ricebowl in ricebowl_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * ricebowl_lib[ricebowl]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = ricebowl
            else:
              user_bag[username].append(ricebowl)
              print(f"\nSuccessfully ordered {ricebowl}")
          else: 
            print("\nInsufficient Balance")
        elif ricebowl == 1:
          return
        else:
          print("Invalid Input")
          break
      elif choice == 3:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PASTA ------------------------------------------------------------- ")
        print([pasta_lib])
        print ("________________________________________________________________________________________________________________________________")
        pasta = input("Enter your Choice of pasta (Enter 1 to return): ")
        if pasta in pasta_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pasta_lib[pasta]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = {pasta : quantity}
            else:
              user_bag[username].append(pasta[quantity])
              print(f"\nSuccessfully ordered {pasta}")
          else: 
            print("\nInsufficient Balance")
        elif pasta == 1:
          return
        else:
          print("Invalid Input")
          break
      elif choice == 4:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PIZZA ------------------------------------------------------------- ")
        print([pizza_lib])
        print ("________________________________________________________________________________________________________________________________")
        pizza = input("Enter your Choice of pasta (Enter 1 to return): ")
        if pizza in pizza_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pizza_lib[pizza]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = {pizza : quantity}
            else:
              user_bag[username].append(pizza)
              print(f"\nSuccessfully ordered {pizza}")
          else: 
            print("\nInsufficient Balance")
        elif pizza == 1:
          return
        else:
          print("Invalid Input")
          break
      elif choice == 5:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PASTRIES ------------------------------------------------------------- ")
        print([pastries_lib])
        print ("________________________________________________________________________________________________________________________________")
        pastries = input("Enter your Choice of pasta (Enter 1 to return): ")
        if pastries in pastries_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pastries_lib[pastries]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = {pastries : quantity}
            else:
              user_bag[username].append(pastries)
              print(f"\nSuccessfully ordered {pastries}")
          else: 
            print("\nInsufficient Balance")
        elif pastries == 1:
          return
        else:
          print("Invalid Input")
          break
      elif choice == 6:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n---------------------------------------------------------- ADD-ONS ------------------------------------------------------------- ")
        print([addons_lib])
        print ("________________________________________________________________________________________________________________________________")
        addons = input("Enter your Choice of pasta (Enter 1 to return): ")
        if addons in addons_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * addons_lib[addons]['cost']
          if user_acc[username]['balance'] >= total:
            user_acc[username]['balance'] -= total
            user_acc[username]['points'] += quantity
            if username not in user_bag:
              user_bag[username] = {addons : quantity}
            else:
              user_bag[username][addons][quantity]+= quantity
              print(f"\nSuccessfully ordered {pastries}")
          else: 
            print("\nInsufficient Balance")
        elif pastries == 1:
          return
        else:
          print("Invalid Input")
          break
    except ValueError as e:
      print(e)

def wallet(username):
  while True:
    try:
      amount = int(input('Enter Amount to deposit: '))
      user_acc[username]['balance'] += amount
      print(f"You have deposited {amount}, your new balance is {user_acc[username]['balance']}\n")
      print ("________________________________________________________________________________________________________________________________")
      choice = int(input("Enter 1 to return: "))
      while True:
        try:
          if choice == 1: 
            user_menu()
          else:
            print ("Invalid")
            wallet()
            break
        except ValueError as e:
          print(e)
    except ValueError as e:
      print(e)
  
def check_bag(username):
  pass

def check_points(username):
  pass

def admin_login():
  pass


def main_menu():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\t[1] Menu")
  print ("\t[2] Register")
  print ("\t[3] Customer Log-in")
  print ("\t[4] Admin Log-in")
  print ("\t[5] Exit")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your Choice: "))
  
  while True:
    try:
      if choice == 1:
        menu()
      elif choice == 2:
        register()
      elif choice == 3:
        customer_login()
      elif choice == 4:
        admin_login()
      elif choice == 5:
        print ("Thank you!")
        quit()
      else:
        print("Invalid. Please try again")
        main_menu()
        break
    except ValueError as e:
      print(e)

main_menu()