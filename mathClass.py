import random
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
s=[]
b=[]
g=[]
history=[]
attempt=0
while True:
    counter=0
    counter1=0
    tried=[]
    for i in range(9):
        x=random.randint(0,18-counter)
        counter=counter+1
        s.append(l[x])
        l.remove(l[x])
        tried.append(x)

    for i in range(9):
        x=random.randint(0,18-counter)
        counter=counter+1
        b.append(l[x])
        l.remove(l[x])
        tried.append(x)

    g.append(l[0])
    history.append(tried)

    sumS=0
    sumB=0
    for i in range(9):
        sumS=sumS+s[i]
        sumB=sumB+b[i]
    
    if(sumS==sumB+90 and sumS+sumB+g[0]==190):
        print("Done")
        break

    else:
        s.clear()
        b.clear()
        g.clear()
        l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    attempt=attempt+1
    print("attempt: ",attempt)
        

   #elif(counter2>10):
     #   break
    #counter2=counter2+1

print(s)
print(b)
print(g)

        
        
        
