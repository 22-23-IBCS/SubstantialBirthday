import random
import time


def main():


    L=[]
    n=10
    for i in range(n):          # generates random list
        L.append(random.randint(0,n))

    start = time.time()

    print(L)

    for i in range(len(L)-1): #the length of the sorted list is the amount of time the list was iterated
       curMin = L[i]
       indMin = i # index of minimum
       for j in range(i,len(L)): #starts comparison from the current minimum
           if L[j] < curMin:
               curMin = L[j]
               indMin =     # Time complexity is O(n^2) because of nested loop. 

        temp = L[i]
        L[i] = L[indMin]
        L[indMin] = temp

   
if __name__ == "__main__":
    main()

