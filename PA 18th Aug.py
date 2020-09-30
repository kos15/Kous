class Book:
    def __init__(self,bookId,bookName,bookTechnology,bookPrice,authorname):
        self.bookId = bookId
        self.bookName = bookName
        self.bookTechnology = bookTechnology
        self.bookPrice = bookPrice
        self.authorname = authorname

class BookStore:
    def __init__(self,bookdb,bookStoreName):
        self.bookdb = bookdb
        self.bookStoreName = bookStoreName

    def searchByName(self,x_name):
        a1 = []
        for a,b in self.bookdb.items():
            if b.bookName == x_name:
                a1.append(b)
        if len(a1) != 0:
            return a1
        else:
            return None

    def calculatePriceByTechnology(self,x_technology):
        a2 = 0
        for a,b in self.bookdb.items():
            if b.bookTechnology == x_technology:
                a2 += b.bookPrice
        if a2 != 0:
            return 0.9*a2
        else:
            return 0.0


if __name__=="__main__":
    n = int(input())
    books = {}
    for i in range (n):
        bookId = int(input())
        bookName = input()
        bookTechnology = input()
        bookPrice = int(input())
        authorname = input()
        temp = Book(bookId,bookName,bookTechnology,bookPrice,authorname)
        books[i] = temp
    x_name = input()
    x_technology = input()
    
    demo1 = BookStore(books,"TCSL")
    a1 = BookStore.searchByName(demo1,x_name)
    if a1 != None:
        for i in a1:
            print(i.bookId)
            print(i.bookName)
            print(i.bookTechnology)
            print(i.bookPrice)
            print(i.authorname)
    else:
        print("No Book Exists with the BookName")

    demo2 = BookStore(books,"TCSL")
    a2 = BookStore.calculatePriceByTechnology(demo2,x_technology)
    print(a2)
