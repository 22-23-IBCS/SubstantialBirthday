class Zoo():
    
    def __init__(self):
        self.name="Point Defiance Zoo"
        self.animals = ["Elephant","Penguin","Python","Orangutan","Fish"]
        self.employees = ["Steve","Harold","Bart","Dembele"]
        self.enclosures = {1 : "Savannah" , 2:"Ice", 3:"Jungle", 4:"Pond"}
        self.habitats = {"Elephant":1,
                         "Penguin":2,
                         "Python":3,
                         "Orangutan":3,
                         "Fish":4}

    def getName(self):
        return self.name

    def getAnimals(self):
        return self.animals

    def getEmployees(self):
        return self.emplyees

    def updateAnimals(self,animal, habitat):
        self.animals.append(animal)

        for i in self.enclosures.keys():
            if habitat == self.enclosures.get(i):
                self.habitats.update({animal:i})

    def getHabitat(self, animal):
        h = self.habitats.get(animal)
        enclosure=self.enclosures.get(h)
        return ("The "+animal+" lives in the "+enclosure)
        
    
def main():
    Z=Zoo()
    print(Z.getName())
    Z.updateAnimals("Zebra","Savannah")
    print(Z.getAnimals())
    print(Z.getHabitat("Zebra"))

if __name__=="__main__":
    main()
