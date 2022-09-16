class favDog:

    def __init__(self,breed,nickname,color,gender):
        self.mamal=True
        self.nickname= nickname
        self.breed=breed
        self.color=color
        self.gender=gender
        self.cuteness="very cute"

    
    def setNickname(self,nickname):
        self.nickname=nickname
        
    def getNickname(self):
        return self.nickname

    def neutering(self):
        self.gender="neutral"

    def getGender(self):
        return self.gender

    def hairDying(self,color):
        self.color=color

    def getColor(self):
        return self.color

    def getBreed(self):
        return self.breed

    

def main():
    dog1= favDog("Austrailian Sheperd","Pancake","grey","female")
    dog1.setNickname("Max")
    dog1.neutering()
    
    print(dog1.getBreed(),dog1.getNickname(),dog1.getColor(),dog1.getGender())

    dog2= favDog("Bull dog", "Sunny","White","Male")
    dog2.setNickname("Daisy")
    dog2.hairDying("black")
    print(dog2.getBreed(), dog2.getNickname(),dog2.getColor(),dog2.getGender())
        




dogIsCute=True

if(dogIsCute==True):
    print(main())
