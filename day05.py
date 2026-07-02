import time

timer = int(time.strftime("%H"))
print(timer)

minutes = int(time.strftime("%M"))
print(minutes)

if(timer >= 5 and timer <=11):
    print("Good Morning sir")

elif(timer >= 12 and timer <=15):
     print("Good noon sir")
    
elif 16 <= timer <= 18:
     print("Good afternoon sir")
   
else:
     print('Good night')


