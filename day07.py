# #Task 1
for i in range(0, 20):
    print(i+1)
print("\n")

# #Task 2
for i in range(0 , 100 , 2 ):
    print(i)
print("\n")

# #Task 3
for i in range(0 , 100 , 3 ):
    print(i)
print("\n")

#Task 4

num = int(input("Enter the number for multiplication :"))

for i in range(0 , 10):
    print(num , "X" , i+1 , "=" , (i+1)*num)
# print("\n")

# #Task 5
num = int(input("Enter the number for square :"))

for i in range(0, num):
    print((i+1)*(i+1))
print("\n")


# #Task 6
num = int(input("Enter the number for sum :"))
sum = 0
for i in range(0 , num):
    sum += i+1
    i+1

print (sum)

#Task 7

num = int(input("Enter the number for fectorial :"))

for i in range( 0 , num):
    multi = i*(i+1)
print(multi)

#task 8
num = int(input("Enter the number count :"))

count = 0
while num > 0:
    count += 1
    num //= 10  

print("Total digits:", count) 

#Task 9

num = int(input("Enter the number for reverse :"))

for i in range(num , 0 , -1):
    print(i)

while(num > 0):
    print(num)
    num -= 1
    
#Task 10

num = int(input("Enter the number for sum :"))
sum = 0

while(num>0):
   digit_num = num % 10
   sum  += digit_num

   num //= 10
print(sum)

#Task 11


orignal_num= int(input("Enter the num: "))
num = orignal_num
reversed_num = 0

while(num > 0):
    last_digit = num % 10
    reversed_num =(reversed_num * 10) + last_digit
    num //= 10

if orignal_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")














  

