#!/usr/bin/env python3
from graphics import *
import math
import re

class GUI:
    def __init__(self):
        self.width = 500
        self.height = 525

        self.display = None

    def createWindow(self, title="T3NGa"):
        self.w = GraphWin(title, self.width, self.height, autoflush=False)
        self.w.setBackground("gray")
        self.w.configure(highlightthickness=0)
        self.w.update()
    
    def handleClick(self):
        return self.w.getMouse()
    
    def update(self):
        self.w.update()

    def refresh(self):
        self.update()
        
    def close(self):
        self.w.close()    
    
    # ------------ Status Area --------------#

    def createStatus(self, text = ""):
        # Create instance of Status
        self.gameStatus = Status()

        # Create status background
        bgStart = [0, self.height - self.gameStatus.height]
        bgEnd = [self.width + 2, self.height + 2]
        self.gameStatus.background = Rectangle(Point(bgStart[0], bgStart[1]), Point(bgEnd[0], bgEnd[1]))
        self.gameStatus.background.setFill("gray10")
        self.gameStatus.background.setWidth(0)
        self.gameStatus.background.draw(self.w)

        # Create text
        fontSize = self.gameStatus.textSize
        margin = self.gameStatus.textMargin

        self.gameStatus.text = Text(Point(self.width/2, self.height-fontSize-margin), text)
        self.gameStatus.text.setTextColor("gray90")
        self.gameStatus.text.setSize(fontSize)
        self.gameStatus.text.draw(self.w)
        
    def setStatus(self, text):
        if not hasattr(self, 'gameStatus'):
            self.createStatus(text)
        else:
            self.gameStatus.text.setText(text)

    # -------------- Create and maintain the menu ---------------- #
    def createMenu(self, buttons, startY = 100):
        if self.display != None:
            self.display.undraw()
            self.display = None
        self.display = Menu(startY)
        self.display.addButtons(buttons, self.w)

    def waitForMenu(self):
        return self.display.waitForClick(self.w)

    # -------------- Create and maintain the board ---------------- #
    def createBoard(self, size = [500, 500], grid = [3,3]):
        if self.display != None:
            self.display.undraw()
            self.display = None
        self.display = Board(size, grid)
        self.display.createGrid(self.w)

    def addMarker(self, segID, player):
        self.display.addSymbol(self.w, segID, player)

    def waitForBoard(self):
        return self.display.waitForClick(self.w)

    # ------------------- Network game --------------------------#
    def networkJoinForm(self):
        if self.display != None:
            self.display.undraw()
            self.display = None

        self.display = NetworkJoinForm(self.w)

    def joinNetworkFormData(self):
        return self.display.getData()

    def waitForJoinForm(self):
        return self.display.waitForClick(self.w)

    # ------------------- Deprecated functions -------------------- #
    def createGrid(self):
        print("Deprecated")

################# STATUS ################
class Status:    
    def __init__(self):
        self.text = None
        self.background = None
        self.height = 25
        self.textSize = 10
        self.textMargin = 2



############### SHARED METHODS ##################
class BaseElement:
    def inRectangle(self, rect, p):
        p1 = rect.getP1()
        p2 = rect.getP2()
    
        smallx = min(p1.getX(), p2.getX())
        bigx   = max(p1.getX(), p2.getX())
    
        smally = min(p1.getY(), p2.getY())
        bigy   = max(p1.getY(), p2.getY())
    
        return p.getX() > smallx and p.getX() < bigx and p.getY() > smally and p.getY() < bigy

    def getTarget(self, p, elements):
        
        i = 0
        for element in elements:
            if(self.inRectangle(element,p)):
                return i
            i += 1 #Update index tracker
        return None # Not click within element


################# BOARD #################
class Board(BaseElement):
    def __init__(self, board = [500, 500], grid = [3,3]):
        self.segments = [] # Empty list for clickable segments
        self.clickable = [] # Possibly used for storing calculated clickable areas
        self.symbols = []
        self.board = board #Board size [x,y]
        self.grid = grid #Gridsize [x,y]

    def createGrid(self, w):
        # Calculate step height- and width in pixels
        xstep = self.board[0] / self.grid[0] 
        ystep = self.board[1] / self.grid[1]
        
        # Loop for each row
        seg = 0 #initial segment in list
        row = 0 #initial row
        ypos = 0 #initial Y position
        while row < self.grid[1]:
            #Loop for each column in row
            col = 0 #initial column
            xpos = 0 #initial x position
            while col < self.grid[0]:
                r = Rectangle(Point(xpos, ypos), Point(round(xpos+xstep), round(ypos+ystep)))
                #r.setFill("red")
                r.draw(w)
                self.segments.append(r)
                xpos = round(xpos+xstep)
                col += 1
            ypos = round(ypos+ystep)
            row += 1


    def addSymbol(self, w, segID, player):
        if player == 0:
            symbol = "X"
            color = "blue"
        else:
            symbol = "O"
            color = "red"
        t = Text(self.segments[segID].getCenter(), symbol)
        t.setSize(36)
        t.setTextColor(color)
        t.draw(w)

        self.symbols.append(t)

    def waitForClick(self, w):
        boardClicked = False
        eID = None
        while not boardClicked:
            p = w.getMouse()
            eID = self.getTarget(p, self.segments)
            if(eID != None):
                boardClicked = True
        return eID


    def undraw(self):
        # Segments
        for segment in self.segments:
            segment.undraw()
        self.segments = []
        # Symbols
        for symbol in self.symbols:
            symbol.undraw()
        self.symbols = []



################# MENU #################
class Menu(BaseElement):
    def __init__(self, startY = 100, windowSize = [500, 500]):
        self.buttons = []
        self.windowSize = windowSize
        self.buttonStart = startY
        self.buttonMargin = 5
        self.buttonSize = [250, 35]

    def addButtons(self, buttons, w):
        # Create buttons
        y = self.buttonStart
        xLeft = (self.windowSize[0]/2)-(self.buttonSize[0]/2)
        xRight = (self.windowSize[0]/2)+(self.buttonSize[0]/2)

        for button in buttons:
            #self.buttons.append(Image(Point(self.buttonStart, self.buttonStart), "images/test2.gif"))
            b = Button(p1 = Point(xLeft, y), p2 = Point(xRight, y+self.buttonSize[1]), text = button)
            self.buttons.append(b)
            y += self.buttonSize[1]+self.buttonMargin

        # Draw buttons
        for button in self.buttons:
            button.draw(w)

    def waitForClick(self, w):
        menuClicked = False
        eID = None
        while not menuClicked:
            p = w.getMouse()
            eID = self.getTarget(p, self.buttons)
            if(eID != None):
                menuClicked = True
        return eID

    def undraw(self):
        for button in self.buttons:
            button.undraw()
        self.buttons = []




################# BUTTON #################
class Button(BaseElement):
    def __init__(self, p1, p2, text, color="gray10", textColor = "gray90"):
        self.rectangle = Rectangle(p1, p2)
        self.rectangle.setFill(color)
        self.text = Text(self.rectangle.getCenter(), text)
        self.text.setTextColor(textColor)

    def draw(self, w):
        self.rectangle.draw(w)
        self.text.draw(w)

    def getCenter(self):
        return self.rectangle.getCenter()

    def getP1(self):
        return self.rectangle.getP1()

    def getP2(self):
        return self.rectangle.getP2()

    def undraw(self):
        self.rectangle.undraw()
        self.text.undraw()
    
    def waitForClick(self, w):
        buttonClicked = False
        eID = None
        while not buttonClicked:
            p = w.getMouse()
            eID = self.getTarget(p, [self.rectangle])
            if(eID != None):
                buttonClicked = True
        return True


################# input #################
class Input(BaseElement):
    def __init__(self, label="Label", default="", width=20, center=Point(0,0), labelColor="gray15", textColor="gray25", fill="white"):
        

        # Set up input area
        self.input = Entry(center, width)
        self.input.setTextColor(textColor)
        self.input.setFill(fill)
        self.input.setSize(13)

        # Set up label
        self.text = Text(center, label)
        self.text.setTextColor(labelColor)

        # Reposition elements
        self.input.move(0,20) # Move input below label

        # Insert default data
        if str(default) != "":
            self.input.setText(default)

    def getText(self):
        return self.input.getText()

    def setFill(self, color):
        self.input.setFill(color)

    def setTextColor(self, color):
        self.input.setTextColor(color)

    def draw(self, w):
        self.input.draw(w)
        self.text.draw(w)

    def undraw(self):
        self.input.undraw()
        self.text.undraw()


########### Network Join Form ###########
class NetworkJoinForm(BaseElement):

    def __init__(self, w, startY=100):
        self.ip = Input(label="IP address", default="127.0.0.1", width=15, center=Point(250,startY))
        self.port = Input(label="Port", default="22500", width=5, center=Point(250,startY+50))
        self.bt = Button(Point(250-50, startY+100), Point(250+50, startY+125), "Join", color="gray10", textColor = "gray90")

        self.ip.draw(w)
        self.port.draw(w)
        self.bt.draw(w)

    def undraw(self):
        self.ip.undraw()
        self.port.undraw()
        self.bt.undraw()

    def getData(self):
        return (self.ip.getText(), self.port.getText())

    def highlightField(self, field):
        field.setFill('pink1')
        field.setTextColor('red')

    def unHighlightField(self, field):
        field.setFill('white')
        field.setTextColor('gray10')

    def waitForClick(self, w):
        ip = ""
        port = ""
        check = DataCheck()
        while not check.ip(ip) or not check.intInRange(port):
            self.bt.waitForClick(w)
            ip = self.ip.getText()
            try:
                port = int(self.port.getText())
            except Exception as e:
                port = None

            if not check.ip(ip):
                self.highlightField(self.ip)
            else:
                self.unHighlightField(self.ip)
            if not check.intInRange(port):
                self.highlightField(self.port)
            else:
                self.unHighlightField(self.port)

        return (ip, port)

############## FormCheck ##########
class DataCheck():
    def intInRange(self, test, min=0, max=999999):
        try:
            return (test > min and test < max)
        except Exception:
            return False

    def ip(self, test):
        regx = r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}'
        return re.match(regx, test) != None


















if __name__ == "__main__":
    #Load GUI
    gui = GUI()

    # Create GUI window
    gui.createWindow()

    # Load status area
    gui.createStatus()

    gui.setStatus("Creating menu...")

    # Update/Refresh GUI after making changes
    gui.update()

    # Add board
    gui.createMenu(["Test Board", "Test input"], 100)

    # Update status
    gui.setStatus("Welcome traveller!")

    # Update/Refresh GUI after making changes
    gui.update()

    m = None
    while m == None:
        # Wait for menu click
        m = gui.waitForMenu()

        # Print what has been clicked
        gui.setStatus("You clicked button #" + str(m+1) + " ("+str(m)+")")
        gui.update()

    # Evaluate test selection
    # Board test
    if m == 0:
        gui.createBoard()
        gameOn = True
        while gameOn:
            # Wait for menu click
            m = gui.waitForBoard()

            gui.addMarker(m, 1)

            # Print what has been clicked
            gui.setStatus("You clicked segment #" + str(m+1) + " ("+str(m)+")")
            gui.update()

    # Input test
    elif m == 1:
        gui.networkJoinForm()
        gui.update()

        print(gui.waitForJoinForm())

        '''
        ip = Input(label="IP address", default="", width=15, center=Point(250,100))
        ip.draw(gui.w)
        port = Input(label="Port", default="22500", width=5, center=Point(250,150))
        port.draw(gui.w)

        bt = Button(Point(250-50, 200), Point(250+50, 225), "Join", color="gray10", textColor = "gray90")
        bt.draw(gui.w)

        gui.display.undraw()
        gui.update()

        ipi = ""
        pi = ""
        while not isIP(ipi) or not isPort(pi):
            bt.waitForClick(gui.w)
            ipi = ip.getText()
            pi = int(port.getText())

        print("Connect to: ", ipi, ":", pi)
        '''
        '''
        inp = Entry(Point(500/2, 100), 40)
        inp.setTextColor('gray50')
        inp.setFill('white')
        inp.draw(gui.w)
        gui.display.undraw()
        gui.update()

        text = ""
        while text != "end":
            print(gui.w.getMouse())
            gtext = inp.getText()
            if text != gtext:
                gui.setStatus(gtext)
                text = gtext
        '''


    '''
    gui.createGrid()
    while True:
        gui.setStatus("X's turn")
        gui.addSymbol(gui.getSegment(), "X", "blue")
        gui.update()
        gui.setStatus("O's turn")
        gui.addSymbol(gui.getSegment(), "O", "red")
        gui.update()
    '''

    input("Press Enter to exit")