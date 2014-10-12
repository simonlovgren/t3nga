#!/usr/bin/env python3
from graphics import *
import math

class GUI:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.grid = [3,3] #Gridsize [x,y]
        self.segments = []
        
        self.createWindow()
        
    def createWindow(self):
        self.w = GraphWin("T3NGa", self.width, self.height, autoflush=False)
        self.w.setBackground("gray")
        
    def createGrid(self):
        # Calculate step height- and width in pixels
        xstep = self.width / self.grid[0] 
        ystep = self.height / self.grid[1]
        
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
                r.setFill("red")
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
        
gui = GUI()
gui.createGrid()
print(gui.segments)
while True:
    print(gui.getSegment())