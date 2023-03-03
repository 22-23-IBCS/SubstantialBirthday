from button import*
import random
import time

class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
        

    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)

    def undraw(self):
        self.C.undraw()
        self.T.undraw()

    def addNeighbor(self, n):
        self.neighbors.append(n)

    def getCenter(self):
        return self.center

    def getNeighbors(self):
        return self.neighbors

    def color(self, c):
        self.C.setFill(c)

    def getDegree(self):
        return len(self.neighbors)

    def getName(self):
        return self.name        

class Graph:

    def __init__(self, n, e, win):
        #self.numCoord={}
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                name = "# "+str(numN+1)#names[numN]
                N = Node(x, y, win, name)
                self.nodes.append(N)
                #self.numCoord.update({name:[x,y]})
                numN += 1

            if numN == n:
                break

        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)

        for node in self.nodes:
            node.draw(win)
            node.color("white")

    def getNumCoord(self):
        return self.numCoord

    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()

    def getAllDegrees(self):
        d={}
        for n in self.nodes:
            print(str(n.getDegree()) + " : " + n.getName())

    def makeDict(self):
        self.allNodes={}
        for n in self.nodes:
            self.allNodes[n.getName()]=n.getDegree()
        return(self.allNodes)

    def nameList(self):
        self.allNodes=self.makeDict()
        self.name = list(self.allNodes.keys())
        return(self.name)

    def degreeList(self):
        self.allNodes=self.makeDict()
        self.degree = list(self.allNodes.values())
        return(self.degree)
    
    def maxDegree(self):
        self.keys = self.nameList()
        self.values = self.degreeList()
        self.maxi = max(self.values)
        self.index=[]

        for i in range(len(self.values)):
            if self.values[i] == self.maxi:
                self.index.append(i)     
        for i in self.index:
            self.name=self.keys[i]
            print(str(self.name)+" has the greatest degree of "+str(self.maxi))

        return(self.maxi)

    def minDegree(self):
        self.keys = self.nameList()
        self.values = self.degreeList()
        self.mini = min(self.values)
        self.index=[]

        for i in range(len(self.values)):
            if self.values[i] == self.mini:
                self.index.append(i)   
        for i in self.index:
            self.name=self.keys[i]
            print(str(self.name)+" has the smallest degree of "+str(self.mini))

        return(self.mini)

    def hasCycle(self):
        self.degree= self.degreeList()
        self.name=self.nameList()
        self.l2=[]

        for w in self.degree:
            if w>=2:
                self.l2.append(w)
                self.name.pop(0)

        sum1=0

        for w in self.l2:
            sum1=sum1+w
            print(sum1)
            print(self.name)
            if len(self.name)*2<=sum1:
                return True

        return False
                
def main():

    win = GraphWin("Graph Example", 800, 600)
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Gen.isClicked(m):
            G.delete()
            #Create a graph with (num Nodes, num Edges)
            G = Graph(6, 5, win)
            G.getAllDegrees()
            G.maxDegree()
            G.minDegree()
            print(G.hasCycle())
         
    win.close()


if __name__ == "__main__":
    main()
