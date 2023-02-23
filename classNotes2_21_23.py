import random

def haiku():
    oneSyll=open("oneSyllable.txt")
    a= oneSyll.read()
    oneList=a.split()

    twoSyll=open("twoSyllable.txt")
    b=twoSyll.read()
    oneList.append(b.split())

    print(oneList)

    threeSyll=open("threeSyllables.txt")
    threeList=threeSyll.read()

    fourSyll=open("fourSyllables.txt")
    fourList=fourSyll.read()

    firstLine=({0},{1},{2},{3},{4})
    secondLine=({0},{1},{2},{3},{4},{5},{6})
    thirdLine=({0},{1},{2},{3},{4})
    
    
    
    

   # for oneSyll
def greeting():
    name = input("Give a name\n")
    return "Hello,"+name+". Welcome to the Class."

def main():
    haiku()
'''
    sample = open("sampleText.txt")
    myString=sample.read()
    myList=myString.split()
    for word in myList:
        word = word.lower()
        if "an" in word:
            print(word)


    #String formatting
    #Create place-holders for various strings and "fields"
    #print things with the place holders substuting different values

    name="Mr.Considine"
    greeting = "Hello, {}. Welcome to the class"
    # Change place-holder with the value of name
    
    print(greeting.format(name))

    name="Frank"
    print(greeting.format(name))

    text = "Congrats, {2}, you got a {0} on the final exam! Thanks {1}"
    name = "Mr.Phillips"
    grade = "99"
    print(text.format(name,"Finn",grade))

    #Can also format intergers and floats
    price = 4.67999999
    txt = "Yikes, gas costs ${:2f} a gallon!"
    print(txt.format(price))
'''

if __name__=="__main__":
    main()

    
