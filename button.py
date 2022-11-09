from graphics import *

class Button(Rectangle):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(p1,p2)
        super().draw(win)
        super().setFill(color)

        self.minX = p1.getX()
        self.maxX = p2.getX()
        self.minY = p1.getY()
        self.maxY = p2.getY()

        self.text = Text(Point((self.minX+self.maxX)/2,(self.minY+self.maxY)/2),text)
        self.text.draw(win)

    def isClicked(self,p):
        x = p.getX()
        y = p.getY()

        #if self.minX < x < self.maxX:
            
    
        if(x>self.minX):
            if(x<self.maxX):
                if(y>self.minY):
                    if(y<self.maxY):
                        return True
                    
        return False

class Quitbutton(Button):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(win, p1, p2, color, text)

    def isQuit(self,p):
        return super().isClicked(p)
        
    
                    
def main():

    win = GraphWin("Button example",500,500)
    B = Button(win, Point(300,100),Point(400,175),"Red","button")
    Quit = Quitbutton(win,Point(300,200),Point(400,275),"Red","Quit")

    i=0

    while True:
        m = win.getMouse()

        if (B.isClicked(m)):
           C=Circle(Point(250,250),50+i*20)
           print("Clicked")

        if(Quit.isQuit(m)==True):
            print("quit")
            break

        i=i+1
        
    win.close()


if __name__ == "__main__":
    main()
        

        
        
        
        
    
