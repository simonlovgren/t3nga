#!/usr/bin/env python3
from graphics import *
import math

class GUI:
    def __init__(self):
        self.width = 500
        self.height = 600
        self.board = [500, 500] #Board size [x,y]
        self.grid = [3,3] #Gridsize [x,y]
        self.segments = []
        
        self.createWindow()
        
    def createWindow(self):
        self.w = GraphWin("T3NGa", self.width, self.height, autoflush=False)
        self.w.setBackground("gray")
        
    def createGrid(self):
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
                r.draw(self.w)
                self.segments.append(r)
                xpos = round(xpos+xstep)
                col += 1
            ypos = round(ypos+ystep)
            row += 1
        self.w.update()
    
    def handleClick(self):
        return self.w.getMouse()
        
    def getSegment(self):
        p = self.handleClick()
        i = 0
        for seg in self.segments:
            if(self.inSegment(seg,p)):
                return i
            i += 1 #Update index tracker
        return None # Not click within segment
        
    
    def inSegment(self, seg, p):
        p1 = seg.getP1()
        p2 = seg.getP2()
    
        smallx = min(p1.getX(), p2.getX())
        bigx   = max(p1.getX(), p2.getX())
    
        smally = min(p1.getY(), p2.getY())
        bigy   = max(p1.getY(), p2.getY())
    
        return p.getX() > smallx and p.getX() < bigx and p.getY() > smally and p.getY() < bigy
    
    def addSymbol(self, segID, symbol, color):
        t = Text(self.segments[segID].getCenter(), symbol)
        t.setSize(36)
        t.setTextColor(color)
        t.draw(self.w)
        self.w.update()
    
    def createStatus(self, text):
        fontSize = 20
        margin = 20
        self.gameStatus = Text(Point(self.width/2, self.height-fontSize-margin), text)
        self.gameStatus.setSize(fontSize)
        self.gameStatus.draw(self.w)
        self.w.update()
        
    def setStatus(self, text):
        if not hasattr(self, 'gameStatus'):
            self.createStatus(text)
        else:
            self.gameStatus.setText(text)
    
    def update(self):
        self.w.update()
        
    def close():
        self.w.close()
    
if __name__ == "__main__":
    gui = GUI()
    gui.createGrid()
    while True:
        gui.setStatus("X's turn")
        gui.addSymbol(gui.getSegment(), "X", "blue")
        gui.update()
        gui.setStatus("O's turn")
        gui.addSymbol(gui.getSegment(), "O", "red")
        gui.update()