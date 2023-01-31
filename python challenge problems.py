from graphics import *
import time

def madlib():
    win=GraphWin("Madlib",800,300)

    verb = Entry(Point(480,100),10)
    noun1 = Entry(Point(600,100),10)
    noun2 = Entry(Point(185,150),10)
    noun3 = Entry(Point(485,150),10)
    adj = Entry(Point(200,100),10)
    exclam = Entry(Point(690,150),10)

    noun1.draw(win)
    noun2.draw(win)
    noun3.draw(win)
    verb.draw(win)
    adj.draw(win)
    exclam.draw(win)

    sign1 = Text(Point(200,120),"adjective")
    sign1.draw(win)

    sign2 = Text(Point(480,120),"verb")
    sign2.draw(win)

    sign3 = Text(Point(600,120),"noun")
    sign3.draw(win)

    sign4 = Text(Point(185,170),"noun")
    sign4.draw(win)

    sign5 = Text(Point(485,170),"noun")
    sign5.draw(win)

    sign6 = Text(Point(690,170),"exclamanation")
    sign6.draw(win)



    txt1 = Text(Point(100,100),"All I ate was a")
    txt1.setSize(18)
    txt1.draw(win)

    txt2 = Text(Point(270,100),"pizza.")
    txt2.setSize(18)
    txt2.draw(win)

    txt3 = Text(Point(370,100), "I was planning to")
    txt3.setSize(18)
    txt3.draw(win)

    txt4 = Text(Point(540,100),"But")
    txt4.setSize(18)
    txt4.draw(win)

    txt5 = Text(Point(690,100),"stopped me.")
    txt5.setSize(18)
    txt5.draw(win)

    txt6 = Text(Point(90,150),"So I went to")
    txt6.setSize(18)
    txt6.draw(win)

    txt7 = Text(Point(260,150),"instead.")
    txt7.setSize(18)
    txt7.draw(win)

    txt8 = Text(Point(260,150),"instead.")
    txt8.setSize(18)
    txt8.draw(win)

    txt9 = Text(Point(370,150),"On my way I saw")
    txt9.setSize(18)
    txt9.draw(win)

    txt10 = Text(Point(590,150),"and screamed: ")
    txt10.setSize(18)
    txt10.draw(win)

def gravity():
    win = GraphWin("Gravity", 500,500)
    x=250
    y=1.5
    circle = Circle(Point(x,y),10)
    circle.draw(win)
    while True:
        circle.undraw()
        y=y**1.098
        circle = Circle(Point(x,y),10)
        circle.draw(win)
        time.sleep(0.01)
        if (y>500):
            circle.undraw()
            y=490
            circle = Circle(Point(x,y),10)
            circle.draw(win)
            break

def bounce():

    win = GraphWin("Gravity", 500,500)
    x=250
    y=1.5
    circle = Circle(Point(x,y),10)
    circle.draw(win)
    while True:
        circle.undraw()
        y=y**1.098
        circle = Circle(Point(x,y),10)
        circle.draw(win)
        time.sleep(0.01)
        if (y>500):
            circle.undraw()
            y=300
            circle = Circle(Point(x,y),10)
            circle.draw(win)
            circle.undraw()
            while y<500:
                circle = Circle(Point(x,490),10)
                time.sleep(0.001)
                circle.draw(win)
                circle.undraw()
                y=y+30
                circle = Circle(Point(x,y),10)
                time.sleep(0.001)
                circle.draw(win)
                circle.undraw()

            circle = Circle(Point(x,490),10)
            circle.draw(win)
            break

                
          

def main():
    #madlib()
    #gravity()
    bounce()


    
if __name__=="__main__":
    main()
