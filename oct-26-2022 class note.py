import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

    
def greedyPath(m, num):
    bestHouses = []
    #sort the houses in terms of best to worst
    

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #using a new starting position
    #return once a fair path is generated
    #if no fair path found, return list of zeros as coordinates
    for i in range(num):
        p = []



        #keep track of the value of the path
        #pick the next best house to start with


        #add neighbors to the path after comparing to see which neighbor is best
        for i in range(num - 1):
            #check to see if we are stuck. If we get stuck, break


            
            #check all possible neighbors. Choose the best neighbor
            #add it to the path and add to the value



            #if path is complete, return path and path value


                return pVal, p

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []

        #keep track of the value of the path
        #choose a random coordinate to start at

        x=random.randint(0,4)
        y=random.randint(0.4)
        p.append([x,y])
        pVal=m[x][y]



        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        for i in range(num - 1):

            neighbors=[[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
            for n in neighbors:
                if (n[0]>4) or (n[0]<0):
                    neighbors.remove(n)
                elif (n[1]>4) or (n[1]<0):
                    neighbors.remove(n)
                if n in p:
                    neighbors.remove(n)

            randN=random.choice(neighbors)
            p.append(randN)
            x=randN[0]
            y=randN[1]
                #choose a random direction and attempt to add the neighbor
                #do not add the neighbor to the path if it is outside of the 5x5
                #or if the neighbor is already in the path
                #break the while loop if it was a successful addition or if stuck
    return pVal, p
                        
                
  
def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses?\n"))

    
    ''' Greedy Path Call '''
    pVal, p = greedyPath(m, num)

    print(p)



    ''' Random Path Call '''
    #calculate the average rating of a house in the neighborhood

    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.

            

        

if __name__ == "__main__":
    main()
