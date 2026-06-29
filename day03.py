'''
Scenario: You are building a basic cash register.
 A user inputs the price of an item and the quantity they want to buy.
However, Python saves all user inputs (input()) as strings.

Task: Write a script that takes a string price and a string quantity, 
converts them to the correct data types, calculates the total price,
 and prints it out.

price = "19.99"

quantity = "3"

Expected Output: The total cost is 59.97
'''

                             #Task 1
print("\n Task 1")
price = input("Enter the price of an item\n")
quantity = input("Enter the quantity of an item\n")

c = (float(price) * int(quantity)) 

print("Your total bill is: ")

print (c)

#Task 2

'''Scenario: You are building a system that processes ratings,
 but your database only accepts whole numbers (integers).
   Your current data stream is giving you numbers as text strings containing decimals.

Task: Take the string value given below, 
convert it so that it can be chopped down to a clean integer, 
and print the final result. 
(Hint: Remember what happens if you try to turn a decimal string straight into an int).34

raw_rating = "4.7"

Expected Output: 4'''

print("\n Task 2")

rating = input("Enter the rating of the product\n")

final_rating = float(rating)
final_rating = int(final_rating)

print("The rating of the product is: ")

print(final_rating)


                                   #Task 3

'''
Scenario: A user tells you their current age as an integer, 
and you want to output a message telling them how old they will be in 5 years. 
You must combine text and the new age together in one print statement without using commas 
or f-strings—meaning you have to concatenate strings using the + operator.

Task: Take the integer age, calculate the age in 5 years,
and convert the result back into a string so it can be cleanly added to the final message.'''

print("\n Task 3")

current_age = input("Enter your age\n")

age2 = int(current_age)

age2 += 5

string_age = str(age2)

print("After 5 years, you will be " + string_age + " years old ")