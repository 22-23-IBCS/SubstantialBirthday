
import random
class House:
    def __init__(self):
        self.rating=random.randint(1,10)
    def getRating(self):
        return self.rating

    def calcPath(self,m,l):
        sumP=0
        for i in range(0,len(l)):
            x=l[i][0]
            y=l[i][1]
            sumP=m[x][y]+sumP
        return sumP

    def calcMatrix(self,m):
        sumM=0
        for i in range(0,5):
            sumM=sumM+m[i][0]+m[i][1]+m[i][2]+m[i][3]+m[i][4]

        return sumM

def greedyPath(m,num):
    bestHouses = []
    houses = []
    coords = []

    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])
            
    #pull out the best house from list of houses. Do this 25 times
    for i in range(25):
        curMax = 0
        maxCoord=[0,0]
        for pos in range(len(houses)):
            if (houses[pos] > curMax):
                curMax = houses[pos]
                maxCoord = coords[pos]
        bestHouses.append(maxCoord)
        houses.remove(curMax)
        coords.remove(maxCoord)

                
    #for i in range(len(bestHouses)):
    p=[]
    start = bestHouses[0]
    x = start[0]
    y = start[1]
    pVal= m[x][y]
    p.append(start)

    for i in range(num-1): #check neighbors and remove bad neighbors

        neighbors=[[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        bad=[]


        for n in neighbors:
            if(n[0]>4) or (n[0]<0):
                bad.append(n)
            elif(n[1]>4) or (n[1]<0):
                bad.append(n)
            elif n in p:
                bad.append(n)
        for b in bad:
            neighbors.remove(b)

        isbreak = False

        for h in bestHouses:
            #isbreak = False
            if isbreak:
                break
            for n in neighbors:    
                if n==h:
                    nextHouse = n
                    isbreak = True
                    break
            
        p.append(nextHouse)
        x = nextHouse[0]
        y = nextHouse[1]
        pVal=pVal+m[x][y]

    if (len(p)!=num):
        return "your trapped. please try again"

    return pVal,p
  
def main():

    m=[[],[],[],[],[]]
    for l in m:
        for i in range(5):
            h=House()
            l.append(h.getRating())
    for i in range(5):
        print(m[0][i],m[1][i],m[2][i],m[3][i],m[4][i])

    num=int(input ("How many houses? \n"))

    matrixAve=h.calcMatrix(m)/25

    path=greedyPath(m,num)

    print("path: ", path[1])
    print("path average: ",path[0]/num)
    print("total candies collected: ",path[0])
    print("Average generosity", matrixAve)

    if(path[0]>matrixAve):
        print("success")
    elif(path[0]<=matrixAve):
        print("fail")


    


if __name__=="__main__":
    main()


