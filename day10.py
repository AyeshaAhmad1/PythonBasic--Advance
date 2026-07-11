#Program 1

try:
    a = 10
    b = 5
    c = (a/b)
    print(c)
except ZeroDivisionError :
    print("Cannot divided by zero")
finally:
    print("program continuouse")

#Quick quize

num = input("Enter the values between 5 and 9")



print("hello")

if(num == quit):
    print("Progrm exited")
else:
    num_1 = int(num)

    if( num_1 < 5 or num_1 > 9 ):
      raise ValueError("value should be between 5 and 9 or should be word quite")


#TAsk 1
print("Enter 5 numbers")


for i in range(1 , 6):
    try:
        num = int(input("Enter the numbers"))
        if(num < 0):
            raise ValueError("Number cannot be negative")
        print(num)

    except ValueError as e:
        print(e)
    finally: 
        print("Itration completed")
else:
    print("All number processed successfully ")



    



