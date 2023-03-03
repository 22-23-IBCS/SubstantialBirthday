from graphics import*
from button import*

#define different methods to answer a question / solve a problem

#Create a circle inscribed within a square at least 100px wide
def problem1():
    win = GraphWin("SquareCircle",500,400)
    S = Rectangle(Point(1,1),Point(201,201)) #Two points are top left and bottom right point of the square
    S.draw(win)
    C = Circle(Point(101,101),100)
    C.draw(win)

#Create a GUI which gets two user inputs as intergers and
#displays in Text if they are the same number
def problem2():
    win2 = GraphWin("SquareCircle",500,400)
    T = Text(Point(200,100), "")
    T.draw(win2)
    E1 = Entry(Point(100,300), 20) #Takes a point and width
    E1.draw(win2)
    E2 = Entry(Point(300,300), 20) 
    E2.draw(win2)
    while True:
        num1 = E1.getText()
        num2 = E2.getText()
        if (num1==num2) and (num1!=""):
            T.setText("They are the same")
        else:
            T.setText("They are not the same")

#Creates a GUI which gets one user input as an interger and draws a circle
#with that radius
def problem3():
    win3 = GraphWin("UserCircle",500,400)
    E3 = Entry(Point(100,300),20)
    E3.draw(win3)
    E3.setText("1")

    while True:
        r=int(E3.getText())
        C2=Circle(Point(100,100),r)
        C2.draw(win3)

#Create a GUI which gets two string as input and tests if they are
#anagrams of each other (Anagrams are "scrambled letters of eachother)
# Joseph -- Sphoej
def problem4():
    win4 = GraphWin("SquareCircle",500,400)
    T = Text(Point(200,100), "")
    T.draw(win4)
    E1 = Entry(Point(100,300), 20) #Takes a point and width
    E1.draw(win4)
    E2 = Entry(Point(300,300), 20) 
    E2.draw(win4)
    while True:
        str1 = E1.getText()
        str2 = E2.getText()
        an=True
        
        #compare anagrams
        if len(str1)!= len(str2):
            an=False
        
        l1 = list(str1)
        l2 = list(str2)
    
        for c in l1:
            if c in l2:
                if c in l2:
                    l2.remove(c)
                    
                else:
                    an=False
                    break

        T.setText(str(an))

#Create a GUI which draws a table with 3 columns and 5 rows.
# colums should be equal width
#rows should be equal length
def problem5():
    win5 = GraphWin("Table",500,400)
    y1=50
    y2=100
    for c in range(5):
        y1=y1+50
        y2=y2+50
        x1=50
        x2=150
        for i in range(3):
            row=Rectangle(Point(x1,y1),Point(x2,y2))
            row.draw(win5)
            x1=x2
            y1=y1
            x2=x2+100
            y2=y2
        



#Create a GUI with a 'target' (a circle with 3 sections)
# if the user clicks within the target. The text updates and says "hit"
#if the user clicks outside the target the text updates and says "miss"
def problem6():
    while True:
        win6 = GraphWin("Target",500,400)
        text=Text(Point(250,100),"")
        text.draw(win6)
        C1=Circle(Point(250,200), 25)
        C2=Circle(Point(250,200),50)
        C3=Circle(Point(250,200),75)
        C1.draw(win6)
        C2.draw(win6)
        C3.draw(win6)

        l=[]

        while True:
            
            m = win6.getMouse()
            x = m.getX()
            y = m.getY()
         
            distanceX=250-x
            distanceY=200-y
            distance=(distanceX**2)+(distanceY**2)
            r=75
            if (r**2)>=distance:
                text.setText("")
                text.setText("Hit")
            else:
                text.setText("")
                text.setText("Missed")
                
    
def main():

    #problem1()
    #problem2()
    #problem3()
    #problem4()
    #problem5()
    problem6()
    

if __name__=="__main__":
    main()
