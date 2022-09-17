#one class for Library
#one class for customer
#Library - show list of books, lend a book, add a book
#customer - request for a book, return a book
class Library:
    def __init__(self,data):
        self.booklist=data
    def showbooks(self):
        for i in self.booklist:
            print(i)
    def lendABook(self,bookname):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            print("your request is fulfilled! Thankyou!!")
        else:
            print("book is not available")
    def addABook(self,returnedbook):
        self.booklist.append(returnedbook)
        print("Book sucessfully added! Thank you!!")
    def welcome(gre):
        print("{}, Welcome to our library".format(gre))

class customer():
    def requestABook(self):
        print("Enter the book you like to borrow :")
        self.book=input()
        return self.book
    def returnABook(self):
        print("Enter the book you like to return :")
        self.book=input()
        return self.book
    

lib=Library(["Book1","Book2","Book3","Book4"])

cus=customer()

lib.welcome("Hi")
while True:
    print("select options from below")
    print("\n 1-show list of books \n 2-lend a book \n 3-return a book")
    option = int(input())

    if option ==1:
        lib.showbooks()
    elif option ==2:
        requestedBook=cus.requestABook()
        lib.lendABook(requestedBook)
    elif option==3:
        returnedBook=cus.returnABook()
        lib.addABook(returnedBook)

