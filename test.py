from graphics import *

win=GraphWin("win", 500,500)

l=Line(Point(100,100),Point(200,200))
l.draw(win)

x=l.getP1()
print(x)
print(x.getX())

print(l.getP2())
