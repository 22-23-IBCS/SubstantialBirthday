l=["jack","mac","miller","mac"]

d={}
for i in range(len(l)):
    count=0
    for e in range(len(l)):
        if(l[i]==l[e]):
            count=count+1
    d.update({l[i]:count})
h=max(d,key=d.get)

print(h)
