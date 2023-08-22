class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showInfo(self):
        print(f"The Library has{self.noBooks} books.\nThe books are:")
        for book in self.books:
            print(book)
l1=Library()
l1.addBook("Electromagnetic theory")
l1.addBook("basic c programming")
l1.addBook("basic c++ programming")
l1.addBook("basic python programming")
l1.showInfo()    

        