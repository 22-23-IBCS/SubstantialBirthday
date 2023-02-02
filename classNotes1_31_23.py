import random
import math
def khang():
    n=random.randint(1,10)
    if n<5:
        print("Khang!)
    else:
        print("Herry!")
        
def main():

    #data types (Srrings, Intergers, Floats)

    name = "Adwaya" #string requires quotation mark
    name2 = "Joseph"

    #concatanation
    print(name+" "+name2)

    #indexing
    print(name[4])

    #substrings
    print(name2[0:2]) #stopping index is not included
    print(name[1:])
    print(name2[:4])

    x = 10
    print(x)
    print(x+5)
    print(x*2)

    #mod operator: yields remainder
    print(x%3)

    #interger division: Rounds out to interger
    print(x//3)

    #can change data typr
    y=x/3
    print(type(y))
    y=int(y)


    z = 20
    z = float(x)
    print(x)
    z=20.54673589835
    
    #can round number  with round function
    print(round(x,3))

    #Lists! Each list is a collection of elements in a specific order(position)
    L=[2.5, "Frank", True, 0, 23, x]

    print(L[0])
    print(L[3:])

    #Calling methods need parentaces

    n=Khang()
    print(n)
    print(Khang())

    

if __name__ == "__main__":
    main()

    
