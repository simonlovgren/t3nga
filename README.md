T3NGa: Python Project (Documentation: WIP)
==========================================
**T3NGa** is created as a project during an introductory course in IT and Compyter Science. **T3NGa** stands for **T**ic-**T**ac-**T**oe **N**etwork **Ga**me, as it is a LAN-enabled version of tic-tac-toe created in Python.

**OBS! The documentation is a work in progress.**

gui.py
------

###GUI (*class*)
gui.py contains the main code for the grapical user interface. It is built with multiple classes for easy implementation in the logic part of the code, abstracting `graphics.py` yet another step specific for this application. The GUI class is the only interface to be used by the logic part of the code.
```
#!python
gui = GUI()
```

| Method	    								| Description                   					   						|
| --------------------------------------------- | -------------------------------------------------------------------------	|
| `createWindow(title)` 						| Creates a new graphics window without content.	 						|
| `handleClick()`       						| Internal proxy/handle to `graphic.py`.   									|
| `update()`									| Updates window. **Use after finishing drawing frame.** 					|
| `refresh()`									| Proxy/Handle to `update()`.												|
| `close()`										| Closes the window. 														|
| `createStatus(text)`							| Creates text-status area at bottom of the screen and sets status text. 	|
| `setStatus(text)`								| Sets status text. 														|
| `createMenu(buttons, startY = 100)`			| Creates a vertical menu of buttons. 										|
| `waitForMenu()`								| Waits for the user to click on a menu option. 							|
| `createBoard(size, grid)`						| Sets up the board for the game. 											|
| `addMarker(segID, player)`					| Places a player marker on clickable segment with ID `segID`. 				|
| `waitForBoard()`								| Waits for the user to click on a clickable segment of the board. 			|
| `createGrid()`								| **Deprecated** 															|




#### GUI.createWindow([title]) `Void`
Creates a new graphics window where drawn content will appear. Autoflush (automatic update of window) is turned off and update is manually accessed using `gui.update()`. `GUI.createWindow()` **must be called before any other GUI method**.
```
#!python
gui.createWindow("My Window")
```

##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `title` 			| String		| No		| *T3NGa*			| Title of the graphics window.						|


#### GUI.handleClick() `Void`
Internal proxy/handle to the GraphWin-method `getMouse()` in `graphic.py`.
```
#!python
self.handleClick()
```


#### GUI.update() `Void`
Updates/writes the changes to the graphics window. Use this when all calculations for the specific frame is done and all objects have been drawn using `draw()`. This is to be able to rapidly draw multiple objects to the graphics window without unessesary delay.
```
#!python
gui.update()
```


#### GUI.refresh() `Void`
Proxy/handle to `GUI.update()`
```
#!python
gui.refresh()
```


#### GUI.close() `Void`
Closes (terminates) the graphics window.
```
#!python
gui.close()
```


#### GUI.createStatus(text) `Void`
Creates the text-status area at the bottom of the screen - **should only be called if text-status does not already exist in window**.
```
#!python
gui.createStatus("Interface is loading...")
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `text` 			| String		| No		| Empty				| Text to be displayed in text-status area.			|


#### GUI.setStatus(text) `Void`
Sets (updates) the text displayed in text-status area. `GUI.update()` must be called for change to be displayed in graphics window.
```
#!python
gui.createStatus("Interface is loading...")
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `text` 			| String		| Yes		| N/A				| Text to be displayed in text-status area.			|


#### GUI.createMenu(buttons, startY) `Void`
Creates a vertically listed menu of buttons. How many buttons that can be added depends on the size of the graphics window.
```
#!python
gui.createMenu(["Button one", "Button two"], 150)
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `buttons`			| List<String>	| Yes		| N/A				| List of button labels.							|
| `startY` 			| Integer		| No		| 100				| Where menu should start on Y-axis					|


#### GUI.waitForMenu() `Integer`
Awaits user clicking on an available menu option/button.
```
#!python
clickedButtonID = gui.waitForMenu()
```



#### GUI.createBoard(size, grid) `Void`
Draws up the board for the game.
```
#!python
gui.createBoard([500,500], [3,3])
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `size`			| List<Int>		| No		| [500,500]			| Width and height of game area in window. ([width, height])					|
| `grid` 			| List<Int>		| No		| [3,3]				| How to split the game area. Default is a 3x3 grid. ([horizontal, vertical])	|


#### GUI.addMarker(segID, player) `Void`
Places a player specific marker on the segment with supplied segment ID (`segID`).
```
#!python
gui.addMarker(2, 0)
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `segID`			| Int			| Yes		| N/A				| Segment ID where marker should be placed. Segment ID:s start on 0.			|
| `player` 			| Int			| Yes		| N/A				| Player placing marker (marker type). `0` = X, `1` = O 						|



#### GUI.waitForBoard() `Integer`
Awaits user clicking on a clickable segment on the board. Returns ID of segment (`segID`), starting on `0`.
```
#!python
clickedSegmentID = gui.waitForBoard()
```


###Status (*class*)
`Status` is used as a wrapper for the on-screen text-status area.
```
#!python
status = Status()
```

| Method	    								| Description                   					   						|
| --------------------------------------------- | -------------------------------------------------------------------------	|
| `__init__()` 									| Sets up default variables for the `Status` object.						|






###BaseElement (*class*)
`BaseElement` is the base class for most (new) graphics objects and contain the shared (common) methods of the new graphics objects. `BaseElement` is not used directly, but rather used as parent to the new graphics objects.
```
#!python
# Extending newGraphicsObject with BaseElement
class MyGraphObj(BaseElement):
	def __init__(self):
		print("myGraphObj created")

mgo = MyGraphObject()
```

| Method	    								| Description                   					   						|
| --------------------------------------------- | -------------------------------------------------------------------------	|
| `inRectangle(rect, p)` 						| Checks whether `<Point> p` is inside `<Rectangle> rect` or not.			|
| `getTarget(p, elements)`       				| Checks whether `<Point> p` is inside any of the supplied `<List>elements`.|


#### BaseElement.inRectangle(rect, p) `Boolean`
Checks whether `<Point>p` is inside `<Rectangle>rect` or not.
```
#!python
r = Rectangle(Point(0, 0), Point(100, 100))
p = Point(50, 50)
if mgo.inRectangle(r, p): # Returns True in this case
	print("Point P is inside rectangle R")
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `rect`			| Rectangle		| Yes		| N/A				| `Rectangle` object from `graphics.py` to check against.						|
| `p`	 			| Point			| Yes		| N/A				| `Point` to check.																|


#### BaseElement.getTarget(p, elements) `Integer` `None`
Walks through list of rectangular graphics objects and checks if `<Point>p` is inside any one of them. Returns `None` if no element was the target of the click (`Point`).
```
#!python
rectangles = [
Rectangle(Point(0, 0), Point(50, 100),	
Rectangle(Point(50, 0), Point(100, 100)
]
p = Point(75, 50)

target = mgo.getTarget(p, rectangles)
print(target) # 1
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `p`	 			| Point			| Yes		| N/A				| `Point` to check.																|
| `elements`		| List<Elements>| Yes		| N/A				| List of rectangular graphics elements to check `Point` against.				| 


###Board (*class*) `extends BaseElement`
The `Board` class is used to create- and handle the board created for use within `GUI`.
```
#!python
board = Board([500,500], [3,3])
```

| Method	    								| Description                   					   						|
| --------------------------------------------- | -------------------------------------------------------------------------	|
| `__init__(board, grid)` 						| Creates an instance of `Board` and prepares internal variables.			|
| `createGrid(w)`       						| Generates game grid on supplied board size and supplied grid size.		|
| `waitForClick(w)`								| Waits for the user to click on a clickable segment.						|
| `addSymbol(w, segID, player)`					| Adds symbol to board on selected segment.									|
| `undraw()`									| Undraws all graphics objects used in instance of `board`.							 	|



#### Board.\_\_init\_\_(board = [500,500], grid = [3,3]) `Void`
Initializes the class, optionally takes size of board (`board` = [width, height]) and grid size (`grid` = [horizontal, vertical]). **Runs automatically on calling the class.**
```
#!python
board = Board([500,500], [3,3]) #Generates a 500x500px board divided 3 by 3
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `board`	 		| List<Integer>	| No		| [500,500]			| Width of board (`board` = [width, height]).									|
| `grid`			| List<Integer>	| No		| [3,3]				| Grid size, how to divide board (`grid` = [horizontal, vertical]).				| 



#### Board.createGrid(w) `Void`
Calculates grid size, creates rectangles and draws them to GraphWindow `w`. `GUI.update()` **needs to be called for changes to show.**
```
#!python
w = GraphWin(title, self.width, self.height, autoflush=False)
board.createGrid(w) # Calculates and draws grid (board) in GraphWin w
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `w`	 			| GraphWin		| Yes		| N/A				| GraphWin in which grid (board) is to be drawn.								|



#### Board.waitForClick(w) `Integer`
Waits for the player to click on a clickable segment of the board. Returns ID (`segID`) of said segment, starting on `0`.
```
#!python
segID = board.waitForClick(w) # OR using GUI: segID = gui.waitForBoard(w) # Returns ID of clicked grid segment
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `w`	 			| GraphWin		| Yes		| N/A				| GraphWin where board has been drawn.											|


#### Board.addSymbol(w, segID, player) `Void`
Adds a player symbol/marker onto the grid. `segID` is the ID of the segment where the symbol/marker is to be placed. `GUI.update()` **needs to be called for changes to show.**
```
#!python
segID = board.waitForClick(w) # OR segID = gui.waitForBoard(w) # Returns ID of clicked grid segment
player = 0 # 0 = X, 1 = Y
board.addSymbol(w, segID, player) # Calculates and draws grid (board) in GraphWin w
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `w`	 			| GraphWin		| Yes		| N/A				| GraphWin in which symbol is to be drawn.										|
| `segID` 			| Integer		| Yes		| N/A				| ID of segment where symbol is to be placed.									|
| `player`	 		| Integer		| Yes		| N/A				| ID of player as to draw correct symbol. `0` = X, `1` = O						|



#### Board.undraw() `Void`
Undraws all objects associated with `Board`. **Use when creating/drawing new view** (Automatically invoked in `GUI`).
```
#!python
board.undraw()
```

###Menu (*class*) `extends BaseElement`
The `Menu` class is used to easily create- and hande basic graphic menus.
```
#!python
menu = Menu()
```

| Method	    									| Description                   					   						|
| ------------------------------------------------- | -------------------------------------------------------------------------	|
| `__init__(startY = 100, windowSize = [500,500])`	| Creates an instance of `Menu` and prepares internal variables.			|
| `addButtons(buttons, w)`       					| Adds buttons in a vertical list.											|
| `waitForClick(w)`									| Waits for the user to click on a button.									|
| `undraw()`										| Undraws all graphics objects used in instance of `Menu`.				 	|


#### Menu.__init__(startY = 100, windowSize = [500,500]) `Menu`
Returns an instance of `Menu` and prepares internal variables.
```
#!python
# To specify startingpoint on Y-axis as well as window size:
menu = Menu(100, [500,500]) # Menu starts at 100px on y-axis in percieved window of 500x500px
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `startY` 			| Integer		| No		| 100				| Starting point of menu on Y-axis.												|
| `windowSize`		| Integer		| No		| [500,500]			| Size of window (or part of window) where menu is to be displayed.				|


#### Menu.addButtons(buttons, w) `Void`
Adds buttons in a vertical list starting on `startY`. `GUI.update()` **needs to be called for changes to show.**
```
#!python
w = GraphWin(title, self.width, self.height, autoflush=False) # Create GraphWin
menu.addButtons(["Button one", "Button two"], w) # Add buttons with labels "Button One" and "Button two" to GraphWin w
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 																	|
| ----------------- |--------------	| ----------| ------------------| ----------------------------------------------------------------------------	|
| `buttons` 		| List<String>	| Yes		| N/A				| List of button labels (Strings). Buttons will be assigned ID:s starting on 0 as in the list itself	|
| `w`	 			| GraphWin		| Yes		| N/A				| GraphWin in which buttons are to be drawn.									|


#### Menu.waitForClick() `Integer`
Awaits user clicking on an available button.
```
#!python
clickedButtonID = menu.waitForClick() # OR clickedButtonID = gui.waitForMenu()
```

#### Menu.undraw() `Void`
Undraws all objects associated with `Menu`. **Use when creating/drawing new view** (Automatically invoked in `GUI`).
```
#!python
menu.undraw()
```


###Button (*class*) `extends BaseElement`
*Documentation under construction.*

game.py
-------
### game (*class*)
`game.py` contains the class `Game` invoked in `init.py`, which holds the game logic and AI.

```
#!python
game = Game()
```

| Method	    								| Description                   					   						|
| --------------------------------------------- | -------------------------------------------------------------------------	|
| `playingField(self, board)` 					| Displays the game board	 												|
| `newGame(self)`       						| Lets player choose between new game and exiting program   				|
| `start(self, start)`							| starts new game										 					|
| `winRow(self, board, spelare, koll, xInRow)`	| Checks if a row on the board contains xInRow								|
| `winCheck(self, board, spelare, width, xInRow)`| Goes through all possible ways to get xInRow								|
| `playerAction(self,spelare)`					| player clicks on a board position											|
| `man(self, spelare, board)`					| player chooses a position and it is returned if it is a valid choice		|
| `twoRow(self, board, koll, testa)`			| AI checks if a player can win in 1 move 									|
| `ai(self, spelare, board)`					| AI main function 															|
| `start(self)`									| Main function of game. Called to start a game 							|



*Documentation under construction.*

network.py
----------
*Documentation under construction.*

init.py
------
*Documentation under construction.*