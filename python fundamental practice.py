import random
import math

class Fundamentals:

    def centralTendencies(self,x,y,z):
        self.mean=(x+y+z)/3
        if (x<y and x>z):
            self.mid=x
        if (x>y and z>x):
            self.mid = x
        if (y>x and y<z):
            self.mid=y
        if (y<x and y>z):
            self.mid=self.y
        if (z>x and z<y):
            self.mid=z
        if (z<x and z>y):
            self.mid=z

        return(self.mean, self.mid)

    def randomPrime(self,n):

        print (n)
        
        if(n%2==0):
            return True
        if(n%3==0):
            return True
        if(n%5==0):
            return True
        else:
            return False 

    def maxMinRange(self,l):
        self.mini=l[0]
        self.maxi=l[0]
        for i in range(len(l)):
            if (l[i]<self.mini):
                self.mini=l[i]
            if(l[i]>self.maxi):
                self.maxi=l[i]  
        print(l)
        self.range1=self.maxi-self.mini
        return ("Maximum: ",self.maxi," Minimum: ",self.mini,"range: ",self.range1)

    def polarCoord(self,l):
        
        distance=math.sqrt((l[0]**2)+(l[1]**2))
        angle=math.atan2(l[0],l[1])*(180/math.pi)
        self.L=[distance,angle]
        return self.L

    def scrabbleScore(self,n,bonus):
        one=["L","S","U","N","R","T","O","A","I","E"]
        two=["G","D"]
        three=["B","C","M","P"]
        four=["F","H","V","W","Y"]
        five=["K"]
        eight=["J","X"]

        self.score=0
        n=n.upper()
        
        for i in n:
            
            if i in one:
                self.score=self.score+1

            if i in two:
                self.score=self.score+2

            if i in three:
                self.score=self.score+3

            if i in four:
                self.score=self.score+4

            if i in five:
                self.score=self.score+5

            if i in eight:
                self.score=self.score+8

        bonus=bonus.lower()

        if bonus=="double":
            self.score=self.score*2

        if bonus=="triple":
            self.score=self.score*3

        return self.score
            
def main():

    f=Fundamentals()

    l=[]
    for i in range(10):
        l.append(random.randint(1,50))
        
    print(f.centralTendencies(1,3,5))
    print(f.randomPrime(random.randint(1,100)))
    print(f.maxMinRange(l))
    print(f.polarCoord([-5,4]))
    print(f.scrabbleScore("adjlwkdjflw","triple"))
   
    

if __name__=="__main__":
    main()
    
    

    
    
