#IBCS Python Coding Quiz
#Name: Junha Yoo

from graphics import *
import random

def fourCorners():
    win1=GraphWin("Four Corner",500,500)
    box1=Rectangle(Point(0,0),Point(500/4,500/4))
    box2=Rectangle(Point(500,0),Point(500-(500/4),500/4))
    box3=Rectangle(Point(0,500),Point(500/4,500-(500/4)))
    box4=Rectangle(Point(500,500),Point(500-(500/4),500-(500/4)))
    box1.draw(win1)
    box2.draw(win1)
    box3.draw(win1)
    box4.draw(win1)

def generatePhoneNumber():
    win2=GraphWin("Generate Phone Number",500,500)
    E1 = Entry(Point(250,200),20)
    E1.draw(win2)
    areaCode=E1.getText()
    txt=Text(Point(250,300),"")
    txt.draw(win2)
    l1=[]
    l2=[]
    for i in range(3):
        l1.append(random.randint(0,9))
    for i in range(4):
        l2.append(random.randint(0,9))
    num3Digit=""
    num4Digit=""
    for n1 in l1:
        num3Digit=num3Digit+str(n1)
    for n2 in l2:
        num4Digit=num4Digit+str(n2)
        
    while True:
        areaCode=E1.getText()
        txt.setText(areaCode+" "+num3Digit+" "+num4Digit)
        

def main():
    fourCorners()
    generatePhoneNumber()

if __name__=="__main__":
    main()
    
