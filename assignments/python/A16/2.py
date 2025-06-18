# Create a class Product with members as pid,pname,price and quantity.
# Add following methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowProduct 
# d. Add static member discount.
# e. Provide methods for applying discount on price of product.

class Product():
    discount = 0 
    def __init__(self, pid=0, pn="not given", p=0, q="0 kg"):
        self.product_id = pid
        self.pname = pn
        self.price = p
        self.quantity = q

    # need static method for discount bc, discount is for single product and not all.
    @staticmethod
    def get_discount():
        return Product.discount

    @staticmethod
    def set_discount(d):
        Product.discount = d

    def tot_bill(self):
        return self.price - (self.price * (Product.discount / 100))

    def showproduct(self):
        print("Product ID =", self.product_id)
        print("Product Name =", self.pname)
        print("Product Price =", self.price)
        print("Product Quantity =", self.quantity)
        print("Total Bill =", self.tot_bill()) 

    def __del__(self):
        print("Destruction completed!!")

p1 = Product()
p1.showproduct()

p2 = Product(12, "Tata salt", 30, "1 kg")
p2.showproduct()

p3 = Product(13, "Nike shirt", 500, "1")
p3.set_discount(50)
p3.showproduct()
print(f"Discount = {p3.get_discount()}%")
