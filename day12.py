print("            Library menagement system             ")



class library:
    def __init__(self):
        self.books = ["A", "B" , "C" , "D"]
        self.no_of_books = len(self.books)
    
    def show_books(self):
        for index , book in enumerate(self.books , start = 1):
            print(f"Index {index}: {book}")
    
    def show_no_of_books(self):
        print(f"The number of books are: {self.no_of_books}")

    
        
    def add(self , book):
        print(f"The book {book} is added")
        self.books.append(book)
        self.no_of_books += 1

         

p1 = library()
p1.show_books()
p1.show_no_of_books()
print()
p1.add("Python")
print()
p1.show_books()
p1.show_no_of_books()






    