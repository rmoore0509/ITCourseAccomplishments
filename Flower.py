#Name: Rachel Moore
#Date: 6/15/2024
#Description of the purpose of the code: Using OOP to define an attribute of flowers, name three types of flowers, and display information about the behavior of those types of flowers.  

#create a class named Flower
class Flower:
#pass the variable for Flower using the __init__() function to assign a value for name and create an attibute
    def __init__(self, name):
        self.name = name
#create methods for the object
    def grow(self):
        print("The " +self.name + " is growing.")

    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
#instantiate object from the Flower class
    flower1 = Flower("Rose")
#methods are called by using the object_name.method
    flower1.grow()
    flower1.bloom()
#instantiate object from the Flower class
    flower2 = Flower("Daisy")
#methods are called by using the object_name.method
    flower2.grow()
    flower2.bloom()
#instantiate object from the Flower class
    flower3 = Flower("Tulip")
#methods are called by using the object_name.method
    flower3.grow()
    flower3.bloom()

#use if statement to call class Flower attribute and main() methods to run function 
if __name__ == "__main__":
  main()
