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

admin_user = 'admin'
admin_password = 'adminpass'

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
        break
      else:
        print ("Invalid")
        menu()
    except ValueError as e:
      print(e)
      menu()

def menu_b(username):
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
        user_menu(username)
        break
      else:
        print ("Invalid")
        menu_b(username)
    except ValueError as e:
      print(e)
      menu_b(username)


def register():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n---------------------------------------------------------- REGISTER ------------------------------------------------------------ ")
  username = input("Enter Username: ")

  if username in user_acc:
    print ("Username already existing")
    choice = int(input("Enter [1] to continue, [2] to return."))
    while True: 
      try:
        if choice == 1: 
          register()
          break
        elif choice == 2:
          main_menu()
          break
        else:
          print ("Invalid Input. Please try again.")
          register()
      except ValueError as e:
        print(e)
        register()
  else:
    password = input("Enter Password: ")
    password1 = input("Re-Enter Password: ")
    balance = 0
    points = 0

    if password == password1:
      user_acc[username] = {
      'password' : password,
      'balance' : balance,
      'points' : points
    }
      print("\nRegister Complete! Return to Main Menu and chooce [3] to Log-in.")
      print ("________________________________________________________________________________________________________________________________")
      choice = int(input("Enter 1 to return: "))
      while True:
        try:
          if choice == 1: 
            main_menu()
            break
          else:
            print ("Invalid")
            register()
        except ValueError as e:
          print(e)
          register()
    else:
      print ("Invalid Input")
      register()

def customer_login():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n-------------------------------------------------------- CUSTOMER LOG-IN ------------------------------------------------------- ")
  username = input("Username: ")
  password = input("Password: ")

  if username in user_acc:
    if user_acc[username]['password'] == password:
      print(f"Welcome {username}")
      user_menu(username)
    else:
      print("Wrong Credentials\n")
      customer_login()
  else:
    choice = int(input(f"Username {username} does not exist. Enter [1] to return and [2] to Try Again: "))
    while True:  
      try: 
        if choice == 1:
          main_menu()
          break
        elif choice == 2:
          customer_login()
          break
        else: 
          print("Invalid Input. Please Try again.")
          customer_login()
      except ValueError as e:
        print(e)
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
        menu_b(username)
        break
      elif choice == 2: 
        order_food(username)
        break
      elif choice == 3:
        wallet(username)
        break
      elif choice == 4: 
        check_bag(username)
        break
      elif choice == 5:
        check_points(username)
        break
      elif choice == 6: 
        print ("Thank you")
        main_menu()
        break
      else:
        print ("Invalid Input")
        user_menu(username)
    except ValueError as e:
      print (e)
      user_menu(username)

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
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in drinks_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * drinks_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{drinks_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
      elif choice == 2:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n--------------------------------------------------------- RICE BOWLS ----------------------------------------------------------- ")
        for ricebowl in ricebowl_lib:
          print(f"\n\t{ricebowl:50}Cost: P {ricebowl_lib[ricebowl]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in ricebowl_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * ricebowl_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{ricebowl_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
      elif choice == 3:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PASTA ------------------------------------------------------------- ")
        for pasta in pasta_lib:
          print(f"\n\t{pasta:50}Cost: P {pasta_lib[pasta]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in pasta_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pasta_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{pasta_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
      elif choice == 4:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PIZZA ------------------------------------------------------------- ")
        for pizza in pizza_lib:
          print(f"\n\t{pizza:50}Cost: P {pizza_lib[pizza]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in pizza_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pizza_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{pizza_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
      elif choice == 5:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n------------------------------------------------------------ PASTRIES ------------------------------------------------------------- ")
        for pastries in pastries_lib:
          print(f"\n\t{pastries:50}Cost: P {pastries_lib[pastries]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in pastries_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * pastries_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{pastries_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print ("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
      elif choice == 6:
        print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
        print ("\n---------------------------------------------------------- ADD-ONS ------------------------------------------------------------- ")
        for addons in addons_lib:
          print(f"\n\t{addons:50}Cost: P {addons_lib[addons]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        order = input("Enter your Choice of order (Enter 1 to return): ")
        if order in addons_lib:
          quantity = int(input("How many do you want to order?: "))
          total = quantity * addons_lib[order]['cost']
          if user_acc[username]['balance'] >= total:
            if username not in user_bag:
              user_bag[username] = [order]
            else:
              user_bag[username].append(order)
            print (f"\nSuccessfully ordered {order}. ")
            print ("\n----------------------------------------------------------- RECEIPT ------------------------------------------------------------- ")
            print (f"\n\t\t\t\t{order:20}\t\t\t(P{addons_lib[order]['cost']}\tx\t{quantity})")
            print ("\n                                  -------------------------------------------------------\n")
            print (f"\t\t\t\t\tTotal: \t\t\t\t\t{total}")
            print (f"\t\t\t\t\tBalance:\t\t\t\t{user_acc[username]['balance']}")
            user_acc[username]['balance'] -= total
            print (f"\t\t\t\t\tNew Balance: \t\t\t\t{user_acc[username]['balance']}")
            print (f"\t\t\t\t\tPoints Earned:\t\t\t\t{quantity}")
            user_acc[username]['points'] += quantity
            print (f"\t\t\t\t\tTotal Points: \t\t\t\t{user_acc[username]['points']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Order Again\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  order_food(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
          else: 
            print(f"Insufficient Balance. Your current balance is {user_acc[username]['balance']}")
            print("\n\t\t\t[1] Return\t\t\t[2] Wallet\t\t\t[3] Exit")
            print ("________________________________________________________________________________________________________________________________")                
            choice = int(input("Enter your choice: "))
            while True:
              try:
                if choice == 1:
                  user_menu(username)
                  break
                elif choice == 2:
                  wallet(username)
                  break
                elif choice == 3:
                   print("Thank you!")
                   quit()
                else:                      
                  print("Invalid Input")
                  order_food(username)
              except ValueError as e:
                print(e)
                order_food(username)
        elif order == 1:
          user_menu(username)
          break
        else:
          print("Invalid Input")
          order_food(username)
    except ValueError as e:
      print (e)
      order_food(username)

def wallet(username):
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n----------------------------------------------------------- WALLET ------------------------------------------------------------- ")
  print(f"\tUsername:  {username}")
  print(f"\tWallet:    P {user_acc[username]['balance']}")
  print(f"\tPoints:    {user_acc[username]['points']} points")
  print("\n\t\t\t[1] Return\t\t\t[2] Deposit\t\t\t[3] Exit")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your choice: "))
  while True:
    try:
      if choice == 1:
        user_menu(username)
        break
      elif choice == 2: 
        while True:
          try:
            amount = int(input('\nEnter Amount to deposit: '))
            user_acc[username]['balance'] += amount
            print(f"You have deposited {amount}, your new balance is {user_acc[username]['balance']}.")
            print ("________________________________________________________________________________________________________________________________")
            choice = int(input("Enter 1 to return: "))
            while True:
              try:
                if choice == 1: 
                  user_menu(username)
                  break
                else:
                  print ("Invalid")
                  wallet(username)
              except ValueError as e:
                print(e)
                wallet(username)
          except ValueError as e:
            print(e)
            wallet(username)
      elif choice == 3: 
        print("Thank you! ")
        quit()
      else:
        print("Invalid Input")
        wallet(username)
    except ValueError as e:
      print(e)
      wallet(username)
            
  
def check_bag(username): #shows recent orders
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n------------------------------------------------------------- BAG -------------------------------------------------------------- ")
  while True:
    try:
      if username in user_bag:
        print (f"Your recent orders:\n{user_bag[username]}")
        print ("________________________________________________________________________________________________________________________________")
        choice = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice == 1: 
              user_menu(username)
            else:
              print ("Invalid")
              check_bag(username)
          except ValueError as e:
            print(e)
            check_bag(username)
      else:
        print("You haven't ordered anything yet.")
        print ("________________________________________________________________________________________________________________________________")
        choice = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice == 1: 
              user_menu(username)
            else:
              print ("Invalid")
              check_bag(username)
          except ValueError as e:
            print(e)
            check_bag(username)
    except ValueError as e:
      print(e)
      check_bag(username)
      
def check_points(username):
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n----------------------------------------------------------- POINTS ------------------------------------------------------------- ")
  print(f"\tUsername:  {username}")
  print(f"\tWallet:    P {user_acc[username]['balance']}")
  print(f"\tPoints:    {user_acc[username]['points']} points")
  print("\n\t\t\t[1] Return\t\t\t[2] Redeem\t\t\t[3] Exit")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your choice: "))
  while True:
    try:
      if choice == 1:
        user_menu(username)
        break
      elif choice == 2:
        print ("\n\t\t\t\tPlease note that 1 order = 1 point. In every 5 points, you can convert them to 1 peso\n")
        print (f"You currently have {user_acc[username]['points']} points.")
        choice = int(input("Enter [1] to continue and [2] to return: "))
        while True:
          try: 
            if choice == 1:
              if user_acc[username]['points'] >= 5:
                points = int(input("Enter How many points you want to redeem: "))
                redeem = points / 5
                user_acc[username]['balance'] += redeem
                print (f"Congratulations! You redeemed P{redeem}.00. Your new balance is P{user_acc[username]['balance']}.00")
                print ("________________________________________________________________________________________________________________________________")
                choice = int(input("Enter 1 to return: "))
                while True:
                  try:
                    if choice == 1: 
                      user_menu(username)
                    else:
                      print ("Invalid")
                      check_points(username)
                  except ValueError as e:
                    print(e)
                    check_points(username)
              elif choice == 2:
                check_points(username)
              else:
                print ("Invalid")
                check_points(username)
          except ValueError as e:
                    print(e)
                    check_points(username)
      elif choice == 3:
        print("Thank you!")
        quit()
      else: 
        print("Invalid")
        check_points(username)
    except ValueError as e:
      print(e)
      check_points(username)
              
                

def admin_login():
  while True: 
    username = input("Enter Admin Username: ")
    if username == admin_user:
      password = input("Enter Admin Password: ")
      if password == admin_password:
        admin_menu(username)
        break
      else: 
        print("Invalid Password! ")
        admin_login()
    else:
      print("Invalid Username! ")
      admin_login()

def admin_menu():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n---------------------------------------------------------- ADMIN MENU ---------------------------------------------------------- ")
  print("\n[1] Update Menu")
  print("[2] Exit")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your Choice: "))
  while True:
    try:
      if choice == 1:
        admin_edit()
        break
      elif choice == 2:
        main_menu()
        break
      else:
        print("Invalid Input")
        return
    except ValueError as e:
      print(e)


def admin_edit():
  print ("\n***************************************************** WELCOME TO AICKA'S CAFE ************************************************** ")
  print ("\n--------------------------------------------------------- UPDATE MENU ---------------------------------------------------------- ")
  print("\n [1] Edit Price")
  print("\n [2] Add New Product")
  print("\n [3] Log Out")
  print ("________________________________________________________________________________________________________________________________")
  choice = int(input("Enter your Choice: "))
  while True:
    try:
      if choice == 1:
        update_price()
        break
      elif choice == 2:
        add_new()
        break
      elif choice == 3:
        main_menu()
        break
      else:
        print("Invalid Input")
        return
    except ValueError as e:
      print(e)
  
def update_price():
  print ("\n--------------------------------------------------------- UPDATE PRICE -------------------------------------------------------- ")
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
        for drinks in drinks_lib:
          print(f"\t{drinks:50}Size: {drinks_lib[drinks]['size']} oz\t\t\tCost: P {drinks_lib[drinks]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        drink_name = input("Enter Drink name: ")
        if drink_name in drinks_lib:
          new_price = int(input("Enter new price: "))
          drinks_lib[drink_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Drink not found or Invalid Drink name")
          return
      elif choice == 2:
        for ricebowl in ricebowl_lib:
          print(f"\t{ricebowl:50}Cost: P {ricebowl_lib[ricebowl]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        ricebowl_name = input("Enter Rice Bowl name: ")
        if ricebowl_name in ricebowl_lib:
          new_price = int(input("Enter new price: "))
          ricebowl_lib[ricebowl_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Rice Bowl not found or Invalid Rice Bowl name")
          return
      elif choice == 3:
        for pasta in pasta_lib:
          print(f"\t{pasta:50}Cost: P {pasta_lib[pasta]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        pasta_name = input("Enter Pasta name: ")
        if pasta_name in pasta_lib:
          new_price = int(input("Enter new price: "))
          pasta_lib[pasta_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Pasta not found or Invalid Pasta name")
          return
      elif choice == 4:
        for pasta in pasta_lib:
          print(f"\t{pasta:50}Cost: P {pasta_lib[pasta]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        pizza_name = input("Enter Pizza name: ")
        if pizza_name in pizza_lib:
          new_price = int(input("Enter new price: "))
          pizza_lib[pizza_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Pizza not found or Invalid Pizza name")
          return 
      elif choice == 5:
        for pastries in pastries_lib:
          print(f"\t{pastries:50}Cost: P {pastries_lib[pastries]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        pastry_name = input("Enter Pastry name: ")
        if pastry_name in pastries_lib:
          new_price = int(input("Enter new price: "))
          pastries_lib[pastry_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Pastry not found or Invalid Pastry name")
          return  
      elif choice == 6:
        for addons in addons_lib:
          print(f"\t{addons:50}Cost: P {addons_lib[addons]['cost']}.00")
        print ("________________________________________________________________________________________________________________________________")
        addon_name = input("Enter Add-on: ")
        if addon_name in addons_lib:
          new_price = int(input("Enter new price: "))
          addons_lib[addon_name]['cost'] = new_price
          print("Price updated successfully!")
          admin_edit()
        else:
          print("Add-on not found or Invalid Add-on name")
          return  
      elif choice == 7:
        admin_edit()
      else:
        print("Invalid Input")
        update_price()
    except ValueError as e:
      print(e)
      update_price()

def add_new():
  print ("\n--------------------------------------------------------- UPDATE MENU -------------------------------------------------------- ")
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
        new_product = input("Enter the new product's name: ")
        size = int(input("Enter size: "))
        cost = int(input("Enter price: "))
        drinks_lib[new_product] = {'size' : size, 'cost' : cost}
        print(f"Successfully added {new_product} to drinks menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 2:
        new_product = input("Enter the new product's name: ")
        cost = int(input("Enter price: "))
        ricebowl_lib[new_product] = {'cost' : cost}
        print(f"Successfully added {new_product} to ricebowl menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 3:
        new_product = input("Enter the new product's name: ")
        cost = int(input("Enter price: "))
        pasta_lib[new_product] = {'cost' : cost}
        print(f"Successfully added {new_product} to pasta menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 4:
        new_product = input("Enter the new product's name: ")
        cost = int(input("Enter price: "))
        pizza_lib[new_product] = {'cost' : cost}
        print(f"Successfully added {new_product} to pizza menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 5:
        new_product = input("Enter the new product's name: ")
        cost = int(input("Enter price: "))
        pastries_lib[new_product] = {'cost' : cost}
        print(f"Successfully added {new_product} to pastry menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 6:
        new_product = input("Enter the new product's name: ")
        cost = int(input("Enter price: "))
        addons_lib[new_product] = {'cost' : cost}
        print(f"Successfully added {new_product} to add-on menu. ")
        print ("________________________________________________________________________________________________________________________________")
        choice1 = int(input("Enter 1 to return: "))
        while True:
          try:
            if choice1 == 1: 
              admin_menu()
            else:
              print ("Invalid")
              add_new()
          except ValueError as e:
            print(e)
            add_new()
      elif choice == 7:
        admin_edit()
      else:
        print("Invalid")
        add_new()
    except ValueError as e:
      print(e)
      add_new()



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
        break
      elif choice == 2:
        register()
        break
      elif choice == 3:
        customer_login()
        break
      elif choice == 4:
        admin_login()
        break
      elif choice == 5:
        print ("Thank you!")
        quit()
      else:
        print("Invalid. Please try again")
        main_menu()
    except ValueError as e:
      print(e)
      main_menu()

main_menu()