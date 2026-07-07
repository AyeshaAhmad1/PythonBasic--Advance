# Create a function named greet() that takes a person's name as a parameter and prints
#Task 1

def greet(name):
    print("Hello ", name,"!" ,"\nWlcome to Python" )

greet("Ayesha")
print("\n")

#Task 2
# Write a function that accepts three numbers and prints the largest

def largest(a , b , c):
    if(a > b and a>c):
        print(a , "is gretest")
    elif(b>a and b>c):
        print(b,"is greatest")
    else:
        print(c,"is greatest")

largest(23,65, 789)
print("\n")
#Task 3
#Even or Odd

def is_even(num):
    if(num % 2 ==0):
        print("the number is evne")
    else:
        print("The number is odd")

is_even(5)
print("\n")

#Task 4

def table(num):
    for i in range(0 , 10):
        print(num, "X" , i+1 , "=" , num*(i+1))

num = int(input("Enter the value for table"))
table(num)
print("\n")

#Task 5
even = 0

def is_even(num1):
   global even
   if(num1 % 2 ==0):
     even +=1

num = int(input("Enter how many numbers you want to enter:"))

for i in range(0, num):
    num1 = int(input("Now enter your numbers"))
    is_even(num1)

print("Even numbers are: " , even)
print("\n")

#Task 6

def fec(num):
    result = 1
    for i in range (1 , num +1):
        result *= i
    print(result)
fec(8)
print("\n")
#Task 7 

def prime(num):
    if(num %1 == 0 and num % num == 0):
        print("The number is prime")
    else:
        ("The number is not prime")

prime(17)
print("\n")

#Task 8
def add(num , num1):
    print("Addition of two numbers are", (num+num1))
def subs(num , num1):
    print("Difference of two numbers are" , (num-num1))
def multi(num,num1):
    print("Multiplication of two numbwers are ", (num * num1))
def divi(num,num1):
    print("dividion of two numbwers are ", (num/num1))



while True:
    print("Press 1 for addition\n")
    print("Press 2 for substraction\n")
    print("Press 3 for multiplication\n")
    print("Press 4 for division\n")
    print("Press 5 for exit\n")
    choice = int(input("Enter your choice"))
    if(choice == 5):
     break
    
    num = int(input("Enter your first number"))
    num1 = int(input("Enter your second number"))

    match choice:

        case 1:
            add(num , num1)
        case 2:
            subs(num , num1)
        case 3:
            multi(num , num1)
        case 4:
            divi(num , num1)
print("\n")
    
#task 9

def rev(num):
    orignal_num = num
    reversed_num = 0
    while(num>0):
       last_digit = num % 10 
       reversed_num = (reversed_num *10) + last_digit
       num //= 10

    print(reversed_num)

rev(12345)    

#Task 10

def find():
    secrete_num = 27
    attempt = 0
    num = int(input("Guess the secrete number"))
    while(num != 27):
        print("You didnot guess right")
        num = int(input("Guess the secrete number"))
        attempt =+ 1
        if(num == 27):
            print("You guessed the right number in" , attempt , "attempt")
            break

find()
print("\n")

#Task 11

initial_balance = 5000

def check():
    global initial_balance
    print("Your initial balance is ", initial_balance)

def deposit():
    global initial_balance
    deposit_balance = int(input("Enter the money you want to deposit"))
    initial_balance = initial_balance + deposit_balance
    print(initial_balance)

def wtd():
     global initial_balance
     withdraw_balance = int(input("Enter the money you want to withdraw"))

     if(withdraw_balance > initial_balance):
         print("Your donot have enough money")
     else:
         initial_balance = initial_balance - withdraw_balance 
         print("New balance:", initial_balance)


while True:
    print("press 1 to check balance")
    print("press 2 to deposit money")
    print("press 3 to withdraw money")
    print("press 4 to exit")

    choice = int(input("ENter your choice"))

    if(choice == 4):
        print("Thanks for trusting us")
        break
    match choice:
        case 1:
            check()
        case 2:
            deposit()
        case 3:
            wtd()
        case _:
            print("Thanks for comming")
print("\n")
#Task 12

def check(num):
    if(num == 0):
        print("The numberis zero")
    elif(num > 0):
        print("The number is positive")
    else:
        print("The number is negative")
    if(num % 2 == 0 ):
        print("The number is even")
    else:
        print("The number is odd")
    is_prime = True
    if(num <= 1):
        is_prime = False
    else:
        i = 2
    while(i < num):
        if(num % i == 0):
            is_prime = False
            break
        i = i+1
    if(is_prime == True):
        print("The number is prime")
    else:
        print("The number is not prime")

    if(num % 5 == 0):
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")

num = int(input("Enter the number for verification"))
check(num)
print("\n")









    


    
