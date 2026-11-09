#Aggregation

class Book:
    def __init__(self,title: str):
        self.title = title

    def __del__(sefl):
        print(f"Book has been claimed by the Guest. '{self.title}' is no longer in your hands.")

class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books else []

    def __del__(self):
        print ("The Library has been destroyed by the Arbiters.")