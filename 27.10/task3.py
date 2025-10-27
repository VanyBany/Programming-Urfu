#Объявление класса
class Book:
    # Конструктор класса
    def __init__(self,author:str,year:int,title:int):
        self.title = title
        self.author = author 
        self.year = year 


    # Метод
    def info(self):
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
book2 = Book.create_book("Пушкин;очень давно; Золотая рыбка")
print(book)
print(book2)





# Создали экземпляр 
# book = Book("Харуки Муроками",1987,"Норвежский лес")
# book2 = Book("Кто-то",1232,"Что-то")


# print(book)
# print(book.info())
# print(book2)
# print(book2.info())

# class Ebook(Book):

#     def __init__(self,author,year,title,format):
#         self.format = format
#         super().__init__(title,author,year)



#     def info(self):
#         return f"Title: {self.title}, author: {self.author}, year: {self.year},format: {self.format}"

    
# ebook = Ebook("Харуки Муроками",1987,"Норвежский лес","electro")
# print(ebook.info())

