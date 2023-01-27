import random
import time

#bubble sort
def BubbleSort(L):
    start = time.time()
    for i in range(len(L) - 1):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    stop = time.time()
    timePassed = stop - start
    return timePassed


#selection sort
def SelectionSort(L):
    start = time.time()
    for i in range(len(L) - 1):
        curMin = L[i]
        curInd = i
        for j in range(i, len(L)):
            if L[j] < curMin:
                curMin = L[j]
                curInd = j
        temp = curMin
        L[curInd] = L[i]
        L[i] = temp
    stop = time.time()
    timePassed = stop - start
    return timePassed


#insertion sort
def InsertionSort(L):
    start = time.time()
    sortedL = [L[0]]
    for i in range(1, len(L)):
        for j in range(len(sortedL)):
            if L[i] < sortedL[j]:
                break
            elif j == len(sortedL) - 1:
                j += 1
        sortedL.insert(j, L[i])           
    stop = time.time()
    timePassed = stop - start
    return timePassed


#quick sort
def QuickSort(L):
    start = time.time()
    sortedL = quick(L)
    stop = time.time()
    timePassed = stop - start
    return timePassed

def quick(L):
    if len(L) <= 1:
        return L
    else:
        pivot = L.pop(len(L)//2)
        left = []
        right = []
        for elem in L:
            if elem < pivot:
                left.append(elem)
            else:
                right.append(elem)
        return quick(left) + [pivot] + quick(right)

#merge sort
def MergeSort(L):
    start = time.time()
    merge(L)
    stop = time.time()
    timePassed = stop - start
    return timePassed

def merge(L):
    if len(L) > 1:
        m = len(L)//2
        left = L[:m]
        right = L[m:]
        merge(left)
        merge(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1


def main():

    L = []
    n =32000
    for i in range(n):
        L.append(random.randint(0, n))

    t=0
    
    for i in range (10):
        t=MergeSort(L)+t

    average=t/10
    #t = SelectionSort(L)
    #t = InsertionSort(L)
    #t = QuickSort(L)
    #t = MergeSort(L)

    print("For n = " + str(n) + "\nTime passed: " + str(average) + " seconds")

if __name__ == "__main__":
    main()
