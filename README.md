T3NGa: Python Project
=====================
**T3NGa** is created as a project during an introductory course in IT and Compyter Science. **T3NGa** stands for **T**ic-Tac-Toe **N**etwork **Ga**me, as it is a LAN-enabled version of tic-tac-toe created in Python.

Files, Classes, Methods and Functions
=====================================

GUI, *class* (gui.py)
---------------------
gui.py is the main code for the grapical user interface. It is built with multiple classes for easy implementation in the logic part of the code, abstracting `graphics.py` yet another step specific for this application.

```
gui = GUI()

### createWindow([title])
Creates a new graphics window.