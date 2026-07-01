
'''
Task: Ask a user for their first name and last name using input().
 Clean up any accidental extra spaces they might have typed at the beginning or end
 . Then, generate a username that is the first 3 letters of their first name (in lowercase)
 joined with the last 3 letters of their last name (in uppercase)
'''

                       #Task 1
username = input("Enter your first  name\n")
username1 = input("Enter your last name\n")


first_clean = username.strip()
last_clean = username1.strip()


print(first_clean , last_clean)

print(len(first_clean))
print(len(last_clean))

clean_1 = first_clean[0:3].lower()
clean2 = last_clean[-3:].upper()
final_name = clean_1 + clean2
print(final_name)

              #Task 2
'''
Task: Given the sentence: "Python is amazing. I love Python because Python is versatile."

Count how many times the word "Python" appears.

Replace the word "versatile" with "awesome".

Check if the sentence starts with "Python" and ends with "!". (Print True or False for these checks).
'''
str1 = "Python is amazing. I love Python because Python is versatile."


count_python = str1.count("python")
Replace = str1.replace("versatile" , "Awsome")

start = str1.startswith("Python")
end = str1.endswith("!")

print(count_python)
print(Replace)
print(start)
print(end)


    #Task 3
'''
Task: Write a script that takes a 16-digit credit card number as a string (e.g., "1234567812345678").

Verify that the input consists only of digits and is exactly 16 characters long.

If valid, mask the first 12 digits with asterisks (*) and display only the last 4 digits (e.g., ************5678).
'''

credit_card_num = input("Enter the credit card number")

for_digit = credit_card_num.isdigit()

print(for_digit)
print(len(credit_card_num) == 16)

masked_card = ("*" * 12) + credit_card_num[-4:]
print(masked_card)


