from graphics import *
from button import *

def main():
    
    win = GraphWin("Character Creation", 800,600)

    B1 = Button(win, Point(650,50), Point(750,70),"salmon","Face")
    
    B2 = Button(win, Point(650,80), Point(750,100),"salmon","Big Eyes")

    B3 = Button(win, Point(650,110), Point(750,130),"salmon","Small Eyes")

    B4 = Button(win, Point(650,140), Point(750,160),"salmon","Big Nose")

    B5 = Button(win, Point(650,170), Point(750,190),"salmon","Small Nose")

    B6 = Button(win, Point(650,200), Point(750,220),"salmon","Big Mouth")

    B7 = Button(win, Point(650,230), Point(750,250),"salmon","Small Mouth")
    
    Q = Quitbutton(win, Point(650,500),Point(750,575))
    
    Face = Oval(Point(150, 50), Point(550, 550))

    bigEye1 = Circle(Point(350, 250),40)

    bigEye2 = Circle(Point(450, 250),40)
    #bigEye2.draw(win)

    smallEye1 = Circle(Point(350, 250),20)

    smallEye2 = Circle(Point(450, 250),20)

    bigNose1 = Line(Point(400,300),Point(500,400))
    
    bigNose2 = Line(Point(500,400),Point(400,400))
    
    smallNose1 = Line(Point(400,300),Point(450,350))
    
    smallNose2 = Line(Point(450,350),Point(400,350))

    bigMouth = Oval(Point(500,420),Point(300,490))

    smallMouth = Oval(Point(450,420),Point(350,450))

    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            bigEye1.undraw()
            bigEye2.undraw()
            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B4.isClicked(m):
            bigNose1.undraw()
            bigNose2.undraw()
            smallNose1.undraw()
            smallNose2.undraw()
            bigNose1.draw(win)
            bigNose2.draw(win)

        if B5.isClicked(m):
            bigNose1.undraw()
            bigNose2.undraw()
            smallNose1.undraw()
            smallNose2.undraw()
            smallNose1.draw(win)
            smallNose2.draw(win)

        if B6.isClicked(m):
            bigMouth.undraw()
            smallMouth.undraw()
            bigMouth.draw(win)

        if B7.isClicked(m):
            bigMouth.undraw()
            smallMouth.undraw()
            smallMouth.draw(win)
      
      

        if Q.isQuit(m):
            break

    win.close()


    
if __name__=="__main__":
    main()
