
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

    return pVal/num,p
  
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

    #pathAve= h.calcPath(m,path)/num

    print("path average, path",greedyPath(m,num))

    print("Average generosity", matrixAve)

    

'''
    if (len(path)==num and (pathAve > matrixAve)):
        print("path: ", path)
        print("Number of collected candies: ", h.calcPath(m,path))
        print("Your Average: ", h.calcPath(m,path)/num)
        print("Average generosity: ", matrixAve)
        print("successs")
        
    if(len(path) != num or pathAve < matrixAve):

        print("Your original path has problem. So here's a new one")

        while(True):
            path=h.randPath(m,num)

            if(len(path)==num and h.calcPath(m,path)/num>matrixAve):
                break
        print("path: ", path)
        print("Number of collected candies: ", h.calcPath(m,path))
        print("Your Average: ", h.calcPath(m,path)/num)
        print("Average generosity: ",matrixAve)
        print("successs")
'''
if __name__=="__main__":
    main()


