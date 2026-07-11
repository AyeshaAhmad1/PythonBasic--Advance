try:
    for i in range(1 , 6):
        num = int(input("Enter the numbers"))
        if(num < 0):
            raise ValueError("Number cannot be negative")
        print(num)
    else:
        print("All number processed successfully ")
except ValueError as e:
   print(e)
finally: 
   print("Itration completed")
