class Employee:
    companyName = "Apple"

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.companyName}")
        print(f"Raise: {self.raise_amount}")
        print("-" * 30)
    @staticmethod
    def change_companyname():
        print(f"Welcome to :{Employee.companyName}")



emp1 = Employee("Harry")
emp2 = Employee("Rohan")

print("Initially:")
emp1.showDetails()
emp2.showDetails()

# Create an instance variable only for emp1
emp1.companyName = "Apple India"
Employee.change_companyname()
emp1.change_companyname()

print("After changing emp1.companyName:")
emp1.showDetails()
emp2.showDetails()



# Change the class variable
Employee.companyName = "Google"

print("After changing Employee.companyName:")
emp1.showDetails()
emp2.showDetails()