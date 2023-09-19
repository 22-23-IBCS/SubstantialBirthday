from button import*

l_numbers = ["0","1","2","3","4","5","6","7","8","9"]

win = GraphWin("pw", 600, 600)
e = Entry(Point(300,300), 30)
e.draw(win)
t = Text(Point(300,250), "Please enter a password")
t.draw(win)
t1 = Text(Point(300,200),"Password Strength: ")
t1.draw(win)

b = Button(win, Point(400,400), Point(480, 450), "gray", "Enter")

while True:
    m = win.getMouse()
    pw = e.getText()
    if b.isClicked(m):
        pw = str(pw)

        strongletter = False
        strongNumber = False

        lettercount = 0
        numbercount = 0
            
        for i in pw:
                
            if i not in l_numbers:
                lettercount = lettercount +1
                
            if i in l_numbers:
                numbercount = numbercount+1

        if lettercount >= 10:
            strongletter = True
        if numbercount >= 5:
            strongNumber = True

        print(strongletter, strongNumber, lettercount, numbercount)

        if strongletter == True and strongNumber == True:
            t1.setText("Password Strength: Strong")
        if strongletter == False and strongNumber == True:
            t1.setText("Password Strength: weak, need more letters")
        if strongletter == True and strongNumber == False:
            t1.setText("Password Strength: weak, need more numbers")
        if strongletter == False and strongNumber == False:
            t1.setText("Password Strength: weak, need more letters and numbers")
        break

e2 = Entry(Point(300,350), 30)
e2.draw(win)
t.setText("Retype your password in the blank space\nThen, click Enter")

while True:

    m = win.getMouse()
    if b.isClicked(m):
        s1 = e.getText()
        s2 = e2.getText()
        
        if s1 == s2:
            t.setText("Password Verified!")
        else:
            t.setText("Password NOT verified :(")
        break



