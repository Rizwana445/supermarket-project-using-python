import products
import datetime
def supermarket():
   try:
      print("press 1-> fresh products 1")
      print("press 2-> fresh product 2")
      print("Press 3-> dairy and eggs items")
      print("Press 4-> snacks items")
      print("Press 5-> plastic items")
      print("press 6-> school items")
      fruit_items = ["apple", "orange", "grapes", "kiwi", "pomegranate","guava", "strawberry"]
      vegetable_items=["onion","tomato","carrot","potato","beetroot","cauliflower","cabbage"]
      dairyandeggs_items=["milk","butter","chees","chiken eggs"]
      snacks_items=["potato chips","nuts","chocolate","cookies","candy"]
      plastic_items = ["bottles", "bags", "containers", "utensils", "wraps", "toys", "packaging"]
      school_items = ["notebooks", "pencils", "pens", "backpack", "lunchbox", "folders", "ruler", "scissors", "glue", "calculator"]
      apple_1kg=100
      orange_1kg=100
      pomegranate_1kg=150
      kiwi=100
      strawberry=120
      onion_1kg=100
      tomato_1kg=50
      carrot_1kg=40
      potato_1kg=30
      cabbage=40
      one_milk=34
      one_butter=40
      one_chees=50
      chicken_eggs=20
      potato_chips=20
      nuts=100
      chocolate=50
      cookies=40
      candy=20
      bottles=40
      bags=1500
      containers=500
      wraps=300
      toys=500
      notebooks=40
      pencils=5
      pens=5
      backpack=1400
      lunchbox=200
      folders=100
      user = int(input("Enter your choice:"))
      if user == 1:
            products.fresh_products1()
            fruit_item_name = input("Enter your fruit item:")
            if fruit_item_name in fruit_items:
                print(f"Yes, {fruit_item_name} is available.")
                try:
                    how_many = int(input(f"How many {fruit_item_name} do you want:"))
                    if fruit_item_name == "apple":
                        total =apple_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()
                        f.write(f"Your total bill for {how_many} {fruit_item_name} is {total}\n {x}") 
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif fruit_item_name == "orange":
                        total =orange_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {fruit_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif fruit_item_name == "kiwi":
                        total =kiwi* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {fruit_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif fruit_item_name == "pomegranate":
                        total =pomegranate_1kg* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {fruit_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif fruit_item_name == "strawberry":
                        total =strawberry* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {fruit_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                            print("thank you for visiting  our supermarket")

                except:
                     print(f"Sorry, {fruit_item_name} is not available.")
            
      elif user == 2:
            products.fresh_products2()
            vegetable_item_name = input("Enter your vegetable item:")
            if vegetable_item_name in vegetable_items:
                print(f"Yes, {vegetable_item_name} is available.")
                try:
                    how_many = int(input(f"How many {vegetable_item_name} do you want:"))
                    if vegetable_item_name == "onion":
                        total =onion_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {vegetable_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                            supermarket()
                        else:
                            print("thank you for visiting  our supermarket")
                    elif vegetable_item_name == "tomato":
                        total =tomato_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {vegetable_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif vegetable_item_name == "carrot":
                        total =carrot_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {vegetable_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif vegetable_item_name == "potato":
                        total =potato_1kg * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "w")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {vegetable_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                            print("thank you for visiting  our supermarket")
                    elif vegetable_item_name == "cabbage":
                        total =cabbage * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {vegetable_item_name} is {total}\n {x}  ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")                    
                except:
                    print(f"Sorry, {vegetable_item_name} is not available.")

      elif user == 3:
            products.dairy_and_eggs()
            dairyandeggs_item_name = input("Enter your dairyandeggs item:")
            if dairyandeggs_item_name in dairyandeggs_items:
                print(f"Yes, {dairyandeggs_item_name} is available.")
                try:
                    how_many = int(input(f"How many {dairyandeggs_item_name} do you want:"))
                    if dairyandeggs_item_name == "milk":
                        total =one_milk * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {dairyandeggs_item_name} is {total}\n {x}") 
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting our supermarket")
                    elif dairyandeggs_item_name == "butter":
                        total =one_butter * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a") 
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {dairyandeggs_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif dairyandeggs_item_name == "chees":
                        total =one_chees * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {dairyandeggs_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif dairyandeggs_item_name == "chickeneggs":
                        total =chicken_eggs * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {dairyandeggs_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                except:
                    print(f"Sorry, {dairyandeggs_item_name} is not available.")           
                             
      elif user == 4:
            products.snacks_items()
            snacks_item_name = input("Enter your snacks item:")
            if snacks_item_name in snacks_items:
                print(f"Yes,{snacks_item_name} is available.")
                try:
                    how_many = int(input(f"How many {snacks_item_name} do you want:"))
                    if snacks_item_name == "potato chips":
                        total =potato_chips * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {snacks_item_name} is {total}\n {x}") 
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif snacks_item_name == "nuts":
                        total =nuts * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a") 
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {snacks_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting for our supermarket")
                    elif snacks_item_name == "chocolate":
                        total =chocolate * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {snacks_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting for our supermarket")
                    elif snacks_item_name == "cookies":
                        total =cookies * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {snacks_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif snacks_item_name == "candy":
                        total =candy* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {snacks_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                except:
                    print(f"Sorry, {snacks_item_name} is not available.")    
                           
      elif user == 5:
            products.plastic_items()
            plastic_item_name = input("Enter your plastic item:")
            if plastic_item_name in plastic_items:
                print(f"Yes, {plastic_item_name} is available.")
                try:
                    how_many = int(input(f"How many {plastic_item_name} do you want:"))
                    if plastic_item_name == "bottles":
                        total =bottles * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {plastic_item_name} is {total}\n {x}") 
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif plastic_item_name == "bags":
                        total =bags * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {plastic_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif plastic_item_name == "containers":
                        total =containers* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {plastic_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif plastic_item_name == "toys":
                        total =toys * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {plastic_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif plastic_item_name == "wraps":
                        total =wraps* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a") 
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {plastic_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                except:
                    print(f"Sorry, {plastic_item_name} is not available.")           
                      
      elif user == 6:
            products.school_items()
            school_item_name = input("Enter your school item:")
            if school_item_name in school_items:
                print(f"Yes, {school_item_name} is available.")
                try:
                    how_many = int(input(f"How many {school_item_name} do you want:"))
                    if school_item_name == "notebooks":
                        total = notebooks * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x}") 
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif school_item_name == "pencils":
                        total =pencils * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a") 
                        x=datetime.datetime.now() 
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif school_item_name == "pens":
                        total =pens * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif school_item_name == "backpack":
                        total =backpack * how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif school_item_name == "lunchbox":
                        total =lunchbox* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x} ")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                    elif school_item_name == "foldres":
                        total =folders* how_many
                        print(f"Your total bill is {total}")
                        # Write bill to a text file
                        f=open("bill.txt", "a")
                        x=datetime.datetime.now()  
                        f.write(f"Your total bill for {how_many} {school_item_name} is {total}\n {x}")
                        print("Bill generated successfully.")
                        var = input("Do you want to continue? Press 'yes' to continue:")
                        if var == 'yes':
                           supermarket()
                        else:
                           print("thank you for visiting  our supermarket")
                except:
                    print(f"Sorry, {school_item_name} is not available.")    
                                              
      else:
            print("Invalid choice. Please enter 1 or 2.")
   except ValueError:
        print("Please enter a valid number.")
      
supermarket()
