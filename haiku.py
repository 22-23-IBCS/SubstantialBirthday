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

    for w in firstLine:
        if w in oneList:
            oneList.remove(w)
        if w in twoList:
            twoList.remove(w)
        if w in threeList:
            threeList.remove(w)
        if w in fourList:
            fourList.remove(w)
            
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

def main():
    print(haiku())

if __name__=="__main__":
    main()
