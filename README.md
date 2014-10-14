T3NGa: Python Project
=====================
**T3NGa** is created as a project during an introductory course in IT and Compyter Science. **T3NGa** stands for **T**ic-**T**ac-**T**oe **N**etwork **Ga**me, as it is a LAN-enabled version of tic-tac-toe created in Python.

###GUI 
gui.py is the main code for the grapical user interface. It is built with multiple classes for easy implementation in the logic part of the code, abstracting `graphics.py` yet another step specific for this application.
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