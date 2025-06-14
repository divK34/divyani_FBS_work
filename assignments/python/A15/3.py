# Create a class Shirt with members as sid, sname, type(formal etc), price and size(small,large etc). 
# Add following methods:  
# g. Constructor (Support both parameterized and parameterless)  
# h. Destructor   
# i. ShowShirt

class Shirt():
    def __init__(self, sid=0, sn="not given", t="not given", p=0, s="not given"):
        self.shirt_id = sid
        self.sname = sn
        self.shirt_type = t
        self.price = p
        self.shirt_size = s

    def showshirt(self):
        print("Shirt ID =", self.shirt_id)
        print("Shirt Name =", self.sname)
        print("Shirt Type =", self.shirt_type)
        print("Shirt Price =", self.price)
        print("Shirt Size =", self.shirt_size)

    def __del__(self):
        print("Destruction completed!!")

s1 = Shirt()
s1.showshirt()

s2 = Shirt(101, "nike round neck", "sportswear", 700, "M")
s2.showshirt()