import random
from graphics import *
from button import *

numbers = ["0","1","2","3","4","5","6","7","8","9"]
sign = ["+","-"]

d4 = [1,2,3,4]
d6 = [1,2,3,4,5,6]
d10 = [1,2,3,4,5,6,7,8,9,10]
d12 = [1,2,3,4,5,6,7,8,9,10,11,12]
d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def roleDice(allDiceValues=[[0,1,2,3,4,5,6,7,8,9]], time="1"):
    values = []
    sumRound = []
    for i in range(time):
        for d in allDiceValues:
            sumRound.append(d[random.randint(0,len(d)-1)])
        values.append(sum(sumRound))
    total = sum(values)
    #print(values)
    return(total,values)

def isInt(userTxt,numbers):
    letter = 0
    if len(userTxt)>0:
        for a in userTxt:
            if a not in numbers:
                letter=letter+1
        if letter==0:
            userTxt = int(userTxt)
            return(True)

def modifierIsInt(m,sign= ["+","-"],numbers = ["0","1","2","3","4","5","6","7","8","9"]):
    letter = 0
    if len(m)>0:
        for i in range(1,len(m)):
            if str(m)[i] not in numbers:
                letter = letter+1
               
        if letter == 0:
            if str(m)[0]=="-":
                m = int(m)
                return(m)
            if str(m)[0]=="+":
                m.replace("+","")
                m = int(m)
                return(m)
            if str(m)[0] in numbers:
                m = int(m)
                return(m)
            
def calcSuccessRate(allDiceValues,succVal,modifier): #run random roles for 1000 times and output predicted success rate
    m = modifierIsInt(modifier,["+","-"],["0","1","2","3","4","5","6","7","8","9"])
    if type(m) != int:
        m = int(0)

    result=[]
    count=0

    for i in range(1000):
        v = roleDice(allDiceValues,1)[0]
        if v+m>=succVal:
            count=count+1
    return(round((count/1000)*100,2))

def main():
    win = GraphWin("gui",850,600)
    
    dice4 = Button(win, Point(20,100), Point(150,170),"white","4 sides")
    dice6 = Button(win, Point(20,200), Point(150,270),"white","6 sides")
    dice10 = Button(win, Point(20,300), Point(150,370),"white","10 sides")
    dice12 = Button(win, Point(20,400), Point(150,470),"white","12 sides")
    dice20 = Button(win, Point(20,500), Point(150,570),"white","20 sides")
    roll = Button(win, Point(700,280), Point(800,360), "red", "Roll")
    stop = Button(win, Point(700,410), Point(800,490), "red", "Quit")
    succRate=Button(win,Point(700,150),Point(800,230),"red","show success rate")
    

    userStat = Entry(Point(90,70),18)
    userStat.draw(win)
    userModifier = Entry(Point(300,70),18)
    userModifier.draw(win)
    userSucc = Entry(Point(510,70),18)
    userSucc.draw(win)
    userTime = Entry(Point(730,70),18)
    userTime.draw(win)

    statTxt = Text(Point(90,45),"User Stat:")
    statTxt.draw(win)
    modifierTxt = Text(Point(300,45), "Modifier:")
    modifierTxt.draw(win)
    succValueTxt = Text(Point(510,45),"Success Value:")
    succValueTxt.draw(win)
    timeTxt = Text(Point(730,45),"Number of time dice is rolled:")
    timeTxt.draw(win)
    allValuesTxt = Text(Point(450,100),"Results: ")
    allValuesTxt.setSize(15)
    allValuesTxt.draw(win)
    diceValuesTxt = Text(Point(300,120),"")
    totalnumBox = Rectangle(Point(300,190),Point(600,490))
    totalnumBox.draw(win)
    totalTxt = Text(Point(450,170),"Total:")
    totalTxt.setSize(15)
    totalTxt.draw(win)
    totalNum = Text(Point(450,340),"")
    totalNum.setSize(35)
    totalNum.draw(win)
    successRateTxt = Text(Point(300,520), "Predicted Success Rate (%):")
    successRateTxt.setSize(15)
    successRateTxt.draw(win)
    successRateNum = Text(Point(300,550),"")
    successRateNum.draw(win)
    newStatTxt = Text(Point(450,520), "New user stat:")
    newStatTxt.setSize(15)
    newStatTxt.draw(win)
    newStatNum = Text(Point(450,550),"")
    successOrNotTxt = Text(Point(600,520),"Success or Fail:")
    successOrNotTxt.setSize(15)
    successOrNotTxt.draw(win)
    successOrNotTxt2 = Text(Point(600,550),"")
    successOrNotTxt2.draw(win)

    
    clickedDices = []
    clickedButton = []
    while True:
        m = win.getMouse()
        allResults = []

        if stop.isClicked(m):
            break
        
        if dice4.isClicked(m):
            if "d4" in clickedButton:
                clickedDices.remove(d4)
                clickedButton.remove("d4")
                dice4.setFill("white")  
            else:
                clickedButton.append("d4")
                clickedDices.append(d4)
                dice4.setFill("red")
        if dice6.isClicked(m):
            if "d6" in clickedButton:
                clickedDices.remove(d6)
                clickedButton.remove("d6")
                dice6.setFill("white")
            else:
                clickedButton.append("d6")
                clickedDices.append(d6)
                dice6.setFill("red")
        if dice10.isClicked(m):
            if "d10" in clickedButton:
                clickedDices.remove(d10)
                clickedButton.remove("d10")
                dice10.setFill("white")
            else:
                clickedButton.append("d10")
                clickedDices.append(d10)
                dice10.setFill("red")
        if dice12.isClicked(m):
            if "d12" in clickedButton:
                clickedDices.remove(d12)
                clickedButton.remove("d12")
                dice12.setFill("white")
            else:
                clickedButton.append("d12")
                clickedDices.append(d12)
                dice12.setFill("red")
        if dice20.isClicked(m):
            if "d20" in clickedButton:
                clickedDices.remove(d20)
                clickedButton.remove("d20")
                dice20.setFill("white")
            else:
                clickedButton.append("d20")
                clickedDices.append(d20)
                dice20.setFill("red")

        if succRate.isClicked(m):
            if len(clickedDices)>0:
                s = userSucc.getText()
                if isInt(s,numbers) == True:
                    x=calcSuccessRate(clickedDices, int(s), userModifier.getText())
                    successRateNum.undraw()
                    successRateNum = Text(Point(300,550),x)
                    successRateNum.setSize(15)
                    successRateNum.draw(win)
                    

        if roll.isClicked(m):
            letter = 0

            #determining wheather successValue is a valid value
            successValue = userSucc.getText()
            if len(successValue)>0:
                if isInt(successValue,numbers) == True:
                    successValue = int(successValue)

            #determining wheather modifier is a valid value
            modifier = userModifier.getText()
            modifier = modifierIsInt(modifier,sign,numbers)

            #determining wheather time is a valid value
            if len(clickedDices)>0:
                time = userTime.getText()
                if isInt(time,numbers) == True:
                        calc = roleDice(clickedDices, int(time)) #rolling the dice
            #displaying all values on GUI
                        diceValuesTxt.undraw()
                        #print(len(calc[1])) #test
                        if len(calc[1])>45:
                            diceValuesTxt = Text(Point(450,125),"Dice is rolled too many times. All of the values can't fit in the screen.")
                        elif len(calc[1])<=45:
                            diceValuesTxt = Text(Point(450,125),calc[1])
            #calculating total values without modifier
                        diceValuesTxt.setSize(15)
                        diceValuesTxt.draw(win)
                        total = int(calc[0])
                        totalNum.undraw()
                        totalNum = Text(Point(450,340),str(total))
                        totalNum.setSize(35)
                        totalNum.draw(win)
                        
            #calculating total value if modifier is present
                        if type(modifier) == int:
                            total = int(total) + modifier
                            totalNum.undraw()
                            totalNum = Text(Point(450,340),str(total))
                            totalNum.setSize(35)
                            totalNum.draw(win)
                        
            #calculating new stat
                        stat = userStat.getText()
                        if len(stat)>0:
                            if isInt(stat,numbers) == True:
                                newStat = int(stat)+total
                                newStatNum.undraw()
                                newStatNum = Text(Point(450,550),newStat)
                                newStatNum.setSize(15)
                                newStatNum.draw(win)
                                
            #comparing dice value to success value
                        if type(successValue) == int:
                            if successValue <= total:
                                successOrNotTxt2.undraw()
                                successOrNotTxt2 = Text(Point(600,550),"Success")
                                successOrNotTxt2.setSize(15)
                                successOrNotTxt2.draw(win)
                            else:
                                successOrNotTxt2.undraw()
                                successOrNotTxt2 = Text(Point(600,550),"Fail")
                                successOrNotTxt2.setSize(15)
                                successOrNotTxt2.draw(win)
    win.close()
    
if __name__ == "__main__":
    main()




    
