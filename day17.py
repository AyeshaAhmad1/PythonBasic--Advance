class Animal:
    def __init__(self , name , specie):
        self.name = name 
        self.specie = specie
    
    def is_pet(self):
        return True
    
class Cat(Animal):
    def __init__(self, name, specie , breed ):
        super().__init__(name, specie)
        self.breed = breed
    
    def __str__(self):
        return(f"The name is {self.name} , specie is {self.specie} , breed is {self.breed} ")
    
    def is_pet(self):
        if(super().is_pet()):
            print("This can be keep at home")
        else:
            print("This is not a domestic animal")
    
    def food(self):
        print(f"It only takes {self.specie} food")

cat1 = Cat("Mano" , "Cat" , "Germen",)
print(cat1)
cat1.is_pet()
cat1.food()




    
        