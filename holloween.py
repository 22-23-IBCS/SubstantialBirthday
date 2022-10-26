
import random
class Houses:

    def __init__(self):
        self.matrix=[[],[],[],[],[]]
        for l in self.matrix:
           for i in range(5):
               l.append(random.randint(1,10))
        
        
    def get_houses(self):
        return self.matrix

    def get_house(self, x, y):
        return self.get_houses()[x][y]
    
    def calc_adjacent_houses_value(self,x,y):
        adjacent_houses = []
        if (x+1<5):
            adjacent_houses.append(self.matrix[x+1][y])
        if (x-1>-1):
            adjacent_houses.append(self.matrix[x-1][y])
        if(y+1<5):
            adjacent_houses.append(self.matrix[x][y+1])
        if(y-1>-1):
            adjacent_houses.append(self.matrix[x][y-1])

        return adjacent_houses
    
    def calc_adjacent_houses_xy(self,x,y):
        adjacent_houses = []
        if (x+1<5):
            adjacent_houses.append((x+1, y))
        if (x-1>-1):
            adjacent_houses.append((x-1,y))
        if(y+1<5):
            adjacent_houses.append((x,y+1))
        if(y-1>-1):
            adjacent_houses.append((x,y-1))

        return adjacent_houses
            
            

def main():
    houses = Houses()
    print(houses.get_house(0, 0))#there's no object called "House". Instance should be an individual house
    print(houses.get_house(4, 4))
    print(houses.get_houses())

    sumMatrix=0
    for i in range(0,4):
        sumMatrix=sumMatrix+ houses.get_house(i,0)+houses.get_house(i,1)+houses.get_house(i,2)+houses.get_house(i,3)+houses.get_house(i,4)

    aveGenerosity=sumMatrix/25
    print(aveGenerosity)

    l=[]

 
    for i in range(5):
        l.append(houses.get_house(i,0))
        l.append(houses.get_house(i,1))
        l.append(houses.get_house(i,2))
        l.append(houses.get_house(i,3))
        l.append(houses.get_house(i,4))
    maximum=max(l)
    print(l)
    print(maximum)
    for i in range (0,len(l)):
        if (l[i]==maximum):
            break
    if(i<=4):
        x=0
        y=i
    if(4<i<=9):
        x=1
        y=i-5
    if(9<i<=14):
        x=2
        y=i-10
    if(14<i<=19):
        x=3
        y=i-15
    if(19<i<=24):
        x=4
        y=i-20

    
        
    print(i)
    print(x,y)
    print(houses.get_house(x,y))

    
    print("adjacent houses:", houses.calc_adjacent_houses_xy(0,0))

    

    #houses.get_adjacent_houses(rand,4)
    

    
'''
    nVisit=5 #user input between 1 and 25
    positionX=x
    positionY=y
    counter=0
    while(counter<=nVisit):
        l2=[houses.get_house(positionX+1,positionY),houses.get_house(positionX-1,positionY),houses.get_house(positionX,positionY-1),houses.get_house(positionX,positionY+1)
        ]
        max(l2)

        for i in range (0,len(l)):
            if (l2[i]==maximum):
                if (i==0):
                    return positionX=positionX+1
                if(i==1):
                    return positionX=positionX-1
                if(i==2):
                    return positionY=positoinY-1
                if(i==3):
                    return positionY=positoinY+1

            

        counter=counter+1
'''      

        

    

    

    
    

    

    


if __name__=="__main__":
    main()
    
            
    
 
