def Search(l,n):
    if len(l)==0:
        return False

    if l[0]==n:
        return True
    
    else:
        if l[0]!=n:
            x=l.pop(0)
            return Search(l,n)

def BinarySearch(l,n):

    if len(l)>1:
        left=[]
        right=[]
        p=int(len(l)/2)
        for i in range (p):
            left.append(l[i])
        
        for i in range(p,len(l)):
            right.append(l[i])

        return BinarySearch(right,n),BinarySearch(left,n)
    
        


print(BinarySearch([1,2,3],2))
    
