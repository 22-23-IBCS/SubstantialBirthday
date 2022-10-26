def prob1(l):
    for i in range(len(l)):
        if()
        if(l[i]==7 and l[i-1]==7):
            return(True)
        else: return(False)

def prime(num):
    if (num>1):
        for i in range(2,num-1):
            if (num%i==0):
                return(True)
    else: return(False)

def prob2(l):
    n=0
    for i in range(len(l)):
        if(prime(l[i])==True):
            n=n+l[i]
    return(n)


print(prob2([1,2,3,7,7]))
        

