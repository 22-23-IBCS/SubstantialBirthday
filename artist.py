import turtle

class Artist:

    def __init__(self, t):
        self.t = t
        
    
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def square(self,size=100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)


    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def circle(self,size=100):
        self.t.penup()
        self.t.forward(size)
        self.t.right(90)
        self.t.pendown()
        for i in range(360):
            self.t.forward(1)
            self.t.right(1)

    def star(self, size=100):
        for i in range(5):
            self.t.forward(size)
            self.t.left(72)
            self.t.forward(size)
            self.t.right(144)

    def shavedIce(self):
        self.t.right(250)
        self.t.forward(100)
        self.t.backward(100)
        self.t.right(40)
        self.t.forward(100)
        self.t.right(30)
        for i in range(360):
            self.t.forward(1)
            self.t.left(1)

    def hashTag(self, size=100):
        for i in range(3):
            self.t.forward(size)
            self.t.backward(size/3)
            self.t.right(90)
            self.t.backward(size/3)
        self.t.forward(size)

    def polygon(self,size=100,side=6):
        for i in range(side):
            self.t.forward(size)
            self.t.left(360/side)
            
        

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("white")
    canvas.title("artist")
    t = turtle.Turtle()
    t.speed(5)
    art = Artist(t)

    art.shavedIce()
    art.move(20,0)
    art.square(50)
    art.move(40,10)
    art.triangle()
    art.move(10,20)
    art.circle()
    art.move(70,30)
    art.star()
    art.move(100,40)
    art.hashTag(200)
    art.move(150,30)
    art.polygon(100,7)

    
    
    


if __name__ == "__main__":
    main()
