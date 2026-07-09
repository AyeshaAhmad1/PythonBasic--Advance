#TASK 1
def febonicci(num):
    '''A recursive function that call itself to calculate 
    the febonnicci sequence of nu 7
    it will goes like
    #0,1,1,2,3,5,8,13
    '''
    if num == 0:
        return 0
    if num == 1:
        return 1
    return febonicci(num - 1) + febonicci(num - 2)
    
print( febonicci.__doc__)
print(febonicci(7))


#TASK 2

name = "Ayesha Ahmad"
age = 18
Course = "BS software engineering"

Student_info = f"my name is:  {name} \nmy age is:  {age} \ncourse is:  {Course}"

print(Student_info)

print(f"The lenght of username is {len(name)}")



