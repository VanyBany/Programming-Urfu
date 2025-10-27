from abc import ABC, abstractclassmethod

class Printable(ABC):
    
    @abstractclassmethod
    def print_info():
        pass
    
class Book(Printable):

    def __init__(self,author:str,year:int,title:int):
        self.title = title
        self.author = author 
        self.year = year 



    def print_info(self):
        return f"Title: {self.title}, author: {self.author}, year: {self.year}"
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, year: {self.year}"


    def __eq__(self,other):
        return isinstance(other,Book) and self.title == other.title

    @classmethod
    def create_book(cls,data):
        author, year, title = data.split(";")
        return cls(author,year,title)
    
book = Book("Харуки Муроками",1987,"Норвежский лес")
print(book)
