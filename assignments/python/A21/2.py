# Create class television that has members to hold the model number ,screen size and price. Take a member function to take input from user, If more than 4 digits are entered for model number, if screen size is smaller than 12 inches or greater than 70 inches or if the price is negative or greater than 5000 Rs, then throw an exception. Write a main() that  instantiates an object and allows the user to enter and display data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_details(self):
        try:
            self.model_number = int(input("Enter model number (up to 4 digits) ="))
            if self.model_number > 9999:
                raise ValueError("Model number should not be more than 4 digits.")

            self.screen_size = int(input("Enter screen size in inches (12–70) = "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size should be between 12 and 70 inches.")

            self.price = float(input("Enter price in Rs (0–5000) = "))
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price should be between 0 and 5000 Rs.")

        except ValueError as ve:
            print("Exception =", ve)
            print("Resetting all values to zero.")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\nTelevision Details =")
        print("Model Number =", self.model_number)
        print("Screen Size =", self.screen_size, "inches")
        print("Price = Rs", self.price)

def main():
    tv = Television()
    tv.input_details()
    tv.display()

if __name__ == "__main__":
    main()
