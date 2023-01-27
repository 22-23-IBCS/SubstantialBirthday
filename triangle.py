a=int(5)
b=int(10)
c=int(5)

l=[]
l.append(a)
l.append(b)
l.append(c)

max1=max(l)
l.remove(max1)

sum1=l[0]+l[1]

if sum1>max1:
    print("True")
else:
    print("False")
