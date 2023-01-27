def IsEven(x):
    a=x%2
    if(a==0):
        return True
    else: return False

def IsSorted(l):
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            return False
    return True
   

    
def main():
    print(IsEven(5))
    print(IsSorted([1,2,3,4]))

if __name__ == "__main__":
    main()
    
