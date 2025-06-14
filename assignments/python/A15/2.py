# Create a class Product with members as pid,pname,price and quantity.
# Add following methods:  
# d. Constructor (Support both parameterized and parameterless)  
# e. Destructor   
# f. ShowProduct 

class Product():
    def __init__(self, pid=0, pn="not given", p=0, q="0 kg"):
        self.product_id = pid
        self.pname = pn
        self.price = p
        self.quantity = q

    def showproduct(self):
        print("Product ID =", self.product_id)
        print("Product Name =", self.pname)
        print("Product Price =", self.price)
        print("Product Quantity =", self.quantity)

    def __del__(self):
        print("Destruction completed!!")

p1 = Product()
p1.showproduct()


p2 = Product(12, "Tata salt", 30, "1 kg")
p2.showproduct()