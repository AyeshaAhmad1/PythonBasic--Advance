
              # Task 1

print(       "-----------ATM------------"        )

choice = int(input("Enter the choice from (1 to 5) :"))

match choice:

    case 1:
        print("Checking balance")
    case 2:
        print("Deposit money")
    case 3:
        print("Withdraw money")
    case 4:
        print("Change pin")
    case 5:
        print("Exiting the system")

print("\n")
print("..........Task 2 ........")
print("\n")

            #Task 2

print( "   =========REstraunt ordering system============   ")
print("\n")
print("---------MANUE-----------")
print("\n")
print("PIZZA, BURGER , FRIES , DRINKS ", end=(","))
print("\n")
manue = input("Enter the item you want to buy :")
print("\n")

match manue:
    case "Pizza":
        print("You ordered a pizza")
    case "Fries":
        print("You ordered a Fries")
    case "Burger":
        print("You ordered a Burger")
    case "Drink":
        print("You ordered a Drink")    
    case _:
        print("You did not order anything")
    
   

       
    
    
   





