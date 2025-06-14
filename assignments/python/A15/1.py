# Create a class Book with members as bid, bname, price and author.
# Add following methods:  
# a.  Constructor (Support both parameterized and parameterless)  
# b.  Destructor   
# c.  ShowBook 

class Book():
    def __init__(self, bid=0, bn="not given", p=0, a="not given"):
        print("Constructor is called!!")
        self.book_id = bid
        self.bname = bn
        self.price = p
        self.author = a

    def showbook(self):
        print("Book ID =", self.book_id)
        print("Book Name =", self.bname)
        print("Book Price =", self.price)
        print("Book Author =", self.author)

    def __del__(self):
        print("Destructor is called!!")

b1 = Book()
b1.showbook()

b2 = Book(101, "Emma", 500, "Jane Austen")
b2.showbook()