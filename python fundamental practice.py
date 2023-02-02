import random
import math

def CentralTendencies(x,y,z):

    mean=(x+y+z)/3

    if (x<y and x>z):
        mid=x
    if (x>y and z>x):
        mid = x
    if (y>x and y<z):
        mid=y
    if (y<x and y>z):
        mid=y
    if (z>x and z<y):
        mid=z
    if (z<x and z>y):
        mid=z

    return(mean, mid)

def randomPrime(n):

    print (n)
    
    if(n%2==0):
        return True
    if(n%3==0):
        return True
    if(n%5==0):
        return True
    else:
        return False 

def maxMinRange(l):
    mini=l[0]
    maxi=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
        if(l[i]>maxi):
            maxi=l[i]  
    print(l)
    range1=maxi-mini
    return ("Maximum: ",maxi," Minimum: ",mini,"range: ",range1)

def polarCoord(l):
    
    distance=math.sqrt((l[0]**2)+(l[1]**2))
    angle=math.atan2(l[0],l[1])*(180/math.pi)
    L=[distance,angle]
    return L

def scrabbleScore(n,bonus):
    one=["L","S","U","N","R","T","O","A","I","E"]
    two=["G","D"]
    three=["B","C","M","P"]
    four=["F","H","V","W","Y"]
    five=["K"]
    eight=["J","X"]

    score=0
    n=n.upper()
    
    for i in n:
        
        if i in one:
            score=score+1

        if i in two:
            score=score+2

        if i in three:
            score=score+3

        if i in four:
            score=score+4

        if i in five:
            score=score+5

        if i in eight:
            score=score+8

    bonus=bonus.lower()

    if bonus=="double":
        score=score*2

    if bonus=="triple":
        score=score*3

    return score
        
def main():
    
    l=[]
    for i in range(10):
        l.append(random.randint(1,50))
        
    print(CentralTendencies(1,3,5))
    print(randomPrime(random.randint(1,100)))
    print(maxMinRange(l))
    print(polarCoord([-5,4]))
    print(scrabbleScore("junha","double"))
    
if __name__=="__main__":
    main()
    
    
    
