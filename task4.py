class Book:
    def __init__(self,title,author,year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print("~" * 20)

book1 = Book("The NoteBook", "Nicholas Sparks", 1996)
book2 = Book("The Purpose Driven Life", "Rick Warren", 2002)
book3 = Book("The Great Man", "Kate Christensen", 2007)

book1.describe()
book2.describe()
book3.describe()