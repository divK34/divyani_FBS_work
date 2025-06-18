# Create a class Shirt with members as sid, sname, type(formal etc), price and size(small,large etc). 
# Add following methods:  
# a. Constructor (Support both parameterized and parameterless)  
# b. Destructor   
# c. ShowShirt
# d. For each size of shirt price should change by 10%. 
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept. 

class Shirt():
    shirt_size = ""

    def __init__(self, sid=0, sn="not given", t="not given", p=0, shirt_size="not given"):
        self.shirt_id = sid
        self.sname = sn
        self.shirt_type = t
        self.price = p
        Shirt.shirt_size = shirt_size

    @staticmethod
    def get_size(s):
        Shirt.shirt_size = s
    
    @staticmethod
    def set_size():
        return Shirt.shirt_size
    
    def cal_price(self):
        s = Shirt.shirt_size
        if s in ["S", "small", "s", "SMALL"]:
            self.price 
        elif s in ["M", "medium", "m", "MEDIUM"]:
            self.price = self.price + (self.price * 0.10)
        elif s in ["L", "large", "l", "LARGE"]:
            self.price = self.price + (self.price * 0.20)
        elif s in ["XL", "xlarge", "xl", "XLARGE"]:
            self.price = self.price + (self.price * 0.30)

        return self.price

    def showshirt(self):
        print("Shirt ID =", self.shirt_id)
        print("Shirt Name =", self.sname)
        print("Shirt Type =", self.shirt_type)
        print("Shirt Price =", self.price)
        print("Shirt Size =", Shirt.shirt_size)
        print("Total price =", self.cal_price())

    def __del__(self):
        print("Destruction completed!!")

s1 = Shirt()
s1.showshirt()

s2 = Shirt(101, "nike round neck", "sportswear", 1000, "M")
s2.showshirt()

s3 = Shirt(101, "adidas t-shirt", "casual", 1000, "L")
s3.showshirt()

s4 = Shirt(101, "dior t-shirt", "casual", 1000)
s4.get_size("XL")
s4.showshirt()