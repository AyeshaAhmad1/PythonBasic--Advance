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
