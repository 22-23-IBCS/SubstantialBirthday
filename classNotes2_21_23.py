import random

def haiku222(allList,oneList,twoList,threeList,fourList,syll):

    firstLine=[]
    firstCount=0
    
    while True:
    
        word=allList.pop(random.randrange(len(allList)))
        if word in oneList:
            firstCount=firstCount+1
        if word in twoList:
            firstCount=firstCount+2
        if word in threeList:
            firstCount=firstCount+3
        if word in fourList:
            firstCount=firstCount+4

        firstLine.append(word)

        if firstCount==syll:
            break

        if firstCount>syll:
            lastWord=firstLine.pop(-1)
            if lastWord in oneList:
                firstCount=firstCount-1
            if lastWord in twoList:
                firstCount=firstCount-2
            if lastWord in threeList:
                firstCount=firstCount-3
            if lastWord in fourList:
                firstCount=firstCount-4

            allList.append(lastWord)

            if syll-firstCount==0:
                break

            if syll-firstCount==1:
                replace=oneList.pop(random.randrange(len(oneList)))
                allList.remove(replace)
                firstLine.append(replace)
                break

            if syll-firstCount==2:
                replace=twoList.pop(random.randrange(len(twoList)))
                allList.remove(replace)
                firstLine.append(replace)
                break

            if syll-firstCount==3:
                replace=threeList.pop(random.randrange(len(threeList)))
                allList.remove(replace)
                firstLine.append(replace)
                break
                
            if syll-firstCount==4:
                replace=fourList.pop(random.randrange(len(fourList)))
                allList.remove(replace)
                firstLine.append(replace)
                break
    return(firstLine,allList,oneList,twoList,threeList,fourList)
    

def haiku():
    firstCount=0

    oneSyll=open("oneSyllable.txt")
    a= oneSyll.read()
    allList=a.split()
    oneList=a.split()

    twoSyll=open("twoSyllable.txt")
    b=twoSyll.read()
    for i in b.split():
        allList.append(i)
    twoList=b.split()

    threeSyll=open("threeSyllables.txt")
    c=threeSyll.read()
    for i in c.split():
        allList.append(i)
    threeList=c.split()

    fourSyll=open("fourSyllables.txt")
    d=fourSyll.read()
    for i in d.split():
        allList.append(i)
    fourList=d.split()

    print("Welcome to haiku generater. You can type number of syllables you want for each line.\n")

    syll1=input("How many syllables for the first line? *Type 5 for haiku*\n")
    syll2=input("How many syllables for the second line? *Type 7 for haiku*\n")
    syll3=input("How many syllables for the third line? *Type 5 for haiku\n")
    

    firstLine=haiku222(allList,oneList,twoList,threeList,fourList,int(syll1))
    secondLine=haiku222(firstLine[1],firstLine[2],firstLine[3],firstLine[4],firstLine[5],int(syll2))
    thirdLine=haiku222(secondLine[1],secondLine[2],secondLine[3],secondLine[4],secondLine[5],int(syll3))

    haiku=""
    for w in firstLine[0]:
        haiku=haiku+w+" "
    haiku=haiku+"\n\n"

    for w in secondLine[0]:
        haiku=haiku+w+" "
    haiku=haiku+"\n\n"

    for w in thirdLine[0]:
        haiku=haiku+w+" "
    haiku=haiku+"\n"

    return(haiku)
    

def greeting():
    name = input("Give a name\n")
    return "Hello,"+name+". Welcome to the Class."


def main():
    print(haiku())
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

    
