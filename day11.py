print("\n")
title = "KAUN BANE GA KARORPATI"
print(title.rjust(50))

#Global veriable to count money
final_amount = 0

Questions_list = [ 
    ["What is the largest ocean on Earth?" ," \nA) Atlantic Ocean" , "\nB) Indian Ocean","\nC) Pacific Ocean", "\nD) Arctic Ocean","C" ],
    
    ["Which planet is known as the Red Planet?" , "\nA) Venus" , "\nB) Mars" ,"\nC) Jupiter","\nD) Saturn", "B"],
    ["What is the capital of France?" , "\nA) London" , "\nB) Rome", "\nC) Berlin ","\nD) Paris" ,"D"],
    ["Who painted the Mona Lisa?","\nA) Vincent van Gogh","\nB) Pablo Picasso","\nC) Leonardo da Vinci","\nD) Claude Monet","C"],
    ["How many continents are there in the world,?","\nA) 5","\nB) 6","\nC) 7","\nD) 8","C"],
    ["What is the chemical symbol for water?","\nA) H₂O","\nB) CO₂","\nC) O₂","\nD) NaCl","A"],
    ["Which animal is known as the King of the Jungle?", "\n A) Tiger ","\nB) Lion", "\nC) Elephant","\nD) Gorilla" ,"B"],
    ["What is the tallest mammal on Earth?","\nA) Elephant","\nB) Blue Whale","\nC) Giraffe","\nD) Camel","C"],
    ["How many legs does a spider have?","\nA) 6","\nB) 8","\nC) 10","\nD) 12","B"],
    ["Which is the hardest natural substance on Earth?","\nA) Gold","\nB) Iron","\nC) Diamond","\nD) Quartz","C"],
    ["What is the primary language spoken in Brazil?","\nA) Spanish","\nB) Portuguese","\nC) French","\nD) English","B"]
]

for question in Questions_list:

    for i in range(5):
     print(question[i])

    print("\n")
    ans = input("Enter the correct answer option(A/B/C/D):  ").upper()

    if(ans == question[5].strip()):
       final_amount += 10000
       print()
       print("You won 10000 rupees")
    else:
        print("Wrong answer")

    
print()    
print(f"Your final amount is  {final_amount}")


