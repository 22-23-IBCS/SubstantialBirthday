import random
import time

class List:
    def __init__(self):
        self.L = [2,1,4,3,6,5,9,8,7]

    def getList(self):
        return self.L
    

def main():
    l=List()

    L3=[]
    n=100
    for i in range(n):          # generates random list
        L3.append(random.randint(0,n))

    start = time.time()
    

    print(l.getList)

    while True:

 
        L1=l.getList()

        L2=[]

        L_elements=[]

        for i in range(len(L1)):
            L_elements.append(L1[i])

        for i in range(len(L1)):
            maxPos = len(L_elements) - 1
            randomPos = random.randint(0, maxPos)
            n=L_elements[randomPos]
            L2.append(n)
            L_elements.remove(n)
            
        isSorted = True
        for i in range(len(L1) - 1):
            if L2[i] > L2[i+1]:
                isSorted = False
                #print(L2)        

        if isSorted:
            print("ordered: ",L2)
            stop = time.time()
            total = stop - start
            print("Time: ",str(total))
            break
        

if __name__ == "__main__":
    main()
