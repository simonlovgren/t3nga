T3NGa: Python Project (Documentation: WIP)
=====================
**T3NGa** is created as a project during an introductory course in IT and Compyter Science. **T3NGa** stands for **T**ic-**T**ac-**T**oe **N**etwork **Ga**me, as it is a LAN-enabled version of tic-tac-toe created in Python.

**OBS! The documentation is a work in progress.**

gui.py
------

###GUI (*class*)
gui.py is the main code for the grapical user interface. It is built with multiple classes for easy implementation in the logic part of the code, abstracting `graphics.py` yet another step specific for this application. The GUI class is the only interface to be used by the logic part of the code.
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




#### GUI.createWindow([title])
Creates a new graphics window where drawn content will appear. Autoflush (automatic update of window) is turned off and update is manually accessed using `gui.update()`. `GUI.createWindow()` **must be called before any other GUI method**.
```
#!python
gui.createWindow("My Window")
```

##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `title` 			| String		| No		| *T3NGa*			| Title of the graphics window.						|


#### GUI.handleClick()
Internal proxy/handle to the GraphWin-method `getMouse()` in `graphic.py`.
```
#!python
self.handleClick()
```


#### GUI.update()
Updates/writes the changes to the graphics window. Use this when all calculations for the specific frame is done and all objects have been drawn using `draw()`. This is to be able to rapidly draw multiple objects to the graphics window without unessesary delay.
```
#!python
gui.update()
```


#### GUI.refresh()
Proxy/handle to `GUI.update()`
```
#!python
gui.refresh()
```


#### GUI.close()
Closes (terminates) the graphics window.
```
#!python
gui.close()
```


#### GUI.createStatus(text)
Creates the text-status area at the bottom of the screen - **should only be called if text-status does not already exist in window**.
```
#!python
gui.createStatus("Interface is loading...")
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `text` 			| String		| No		| Empty				| Text to be displayed in text-status area.			|


#### GUI.setStatus(text)
Sets (updates) the text displayed in text-status area. `GUI.update()` must be called for change to be displayed in graphics window.
```
#!python
gui.createStatus("Interface is loading...")
```
##### Parameters
| Parameter			| Type			| Required	| Default			| Description 										|
| ----------------- |--------------	| ----------| ------------------| -------------------------------------------------	|
| `text` 			| String		| Yes		| N/A				| Text to be displayed in text-status area.			|


#### GUI.createMenu(buttons, startY)
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



#### GUI.createBoard(size, grid)
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


#### GUI.addMarker(segID, player)
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


###Board (*class*)
Documentation under construction.

###Menu (*class*)
Documentation under construction.

###Button (*class*)
Documentation under construction.


game.py
-------
Documentation under construction.

network.py
----------
Documentation under construction.

init.py
------
Documentation under construction.