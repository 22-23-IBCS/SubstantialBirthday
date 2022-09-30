
class Vehicle:
    
    #constructor method. Needed to define how.
    #the class instances are created
    def __init__(self, brand, color): #the name should be __init__
        self.numWheels = 4 
        self.brand = brand
        self.color = color

    def getBrand(self):
        return self.brand

    def setBrand(self,brand):
        self.brand=brand
        
class Truck(Vehicle):

    def __init__(self, brand, color):
        super().__init__(brand,color)
    
        
def main():

    #return("Hello World")
        
    veh1 = Vehicle("Toyota","Blue")
    print(veh1.getBrand())

    #veh1.setBrand("Bugatti")
    #print(veh1.getBrand())

    t=Truck("Ford","Red")
    print(t.getbrand())

if (__name__ == "__main__"):

    print(main())

__name__=="__main__"
