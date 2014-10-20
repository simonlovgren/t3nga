from random import randint
from gui import *
import sys
import time

class Game:
    #def __init__(self):
    
    def playingField(self, board):
        #print(board[:3])
        #print(board[3:6])
        #print(board[6:])
        
        #Gå igenom board och sätt ut x och o på rätt platser i GUIn
        for i in  range(0, len(board)):
            if board[i] == 'x':
                self.gui.addMarker(i, 0)
            elif board[i] == 'o':
                self.gui.addMarker(i, 1) 
        self.gui.update()
                       
    def newGame(self):

        #När spelet är slut så kommer en meny fram där spelaren får välja mellan nytt spel eller att avslupa.
        self.gui.createMenu(["nytt spel", "avsluta programmet"],100)
        self.gui.update()
        ny = self.gui.waitForMenu()


        #starta ett nytt spel eller avsluta programmet
        if ny == 0:
            #self.gui.close()  # Changed so main menu displays in same window
            self.start(True)
        elif ny == 1:
            sys.exit()

    def winRow(self, board, spelare, koll, xInRow):

        #Gå igenom dem rutorna som ska kollas, dvs rutorna i koll. Finns det xInRow antal rutor med samma tecken i rad så har någon vunnit. När counter
        # är lika med xInRow så har någon vunnit och användaren frågas om nytt spel

        counter = 0
        for i in koll:
            if board[i] is not spelare:
                counter = 0
            else:
                counter += 1
            if counter >= xInRow:
                self.msleep(250) # Sleep to allow user to see final screen
                self.gui.setStatus('grattis ' + spelare + ' du har vunnit, vill du spela igen?')
                self.gui.update()
                self.newGame()

        return None
        
    def winCheck(self, board, spelare, width, xInRow):

        # Kolla dem vågrätta raderna ifall dem innehåller en vinst 
        koll = []
        for i in range(0, width):
            i *= width
            for j in range(0, width):
                koll.append(i+j)
            self.winRow(board, spelare, koll, xInRow)
            koll = []

        # kolla dem lodräta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst
        for i in range(0, width):
            for j in range(0, width):
                koll.append(i+(j*width))
            self.winRow(board, spelare, koll, xInRow)
            koll = []

        # kolla diagonalerna
        # från vänster högst up till höger långt ner
        for i in range(0, width-xInRow+1):
            
            for j in range(i, width-i):
                if i > 0:
                    koll.append(i)
                koll.append(i+j*(width+1))
            self.winRow(board, spelare, koll, xInRow)
            koll = []

        # från höger högst upp till vänster längst ner
        for i in range(xInRow-1, width):

            for j in range(0, i+1):
                koll.append(i+j*(width-1))
            self.winRow(board, spelare, koll, xInRow)
            koll = []               

        # från vänstra sidan av spelplanen till botten
        for i in range(1, width-xInRow + 1):
            for j in range(0, width-i):
                koll.append(i*width + j*(width + 1))
            self.winRow(board, spelare, koll, xInRow)  
            koll = [] 

        # från högra sidan av spelplanen till botten
        for i in range(2, width-xInRow+2):
            for j in range(0, width-i +1):
                koll.append(i*width-1 + j*(width - 1))
            self.winRow(board, spelare, koll, xInRow) 
            koll = [] 


        #om det inte finns någon tom ruta, dvs ingen ruta som innehåller '*' så är spelet oavgjort. Informera spelaren och fråga om en ny omgång.
        if '*' not in board:
            self.msleep(250) # Sleep to allow user to see final screen
            self.gui.setStatus('oavgjort, vill du spela igen?')
            self.gui.update()
            self.newGame()        
        
                
    #Människor gör ett drag
    def man(self, spelare, board):
        # player action väljer ut var spelaren klickar. Ifall det är en tom plats blir den nu spelarens.
        self.gui.setStatus('spelare ' + spelare + ' välj en tom plats på spelplanen igenom att trycka på den')
        self.gui.update()

        while True:
            var = self.gui.waitForBoard()
            if board[var] == '*':
                break
            else:
                self.gui.setStatus('Rutan är upptagen, välj en annan ruta.')
                self.gui.update()
        
        board[var] = spelare
        return board

    def twoRow(self, board, koll, testa):
        # Värderar segment beroende på närliggande symboler i rad
        spe = 0
        tom = 0
        for i in koll:
            if board[i] == testa:
                spe += 1
            elif board[i] == '*':
                spe += 3
                tom = i
        if spe == 5:
            return tom

        return -1

    def ai(self, spelare, board):
         
        koll = []
        
        for a in range(0, 2):
            if a == 0:
                testa = spelare
            else:
                if spelare == 'x':
                    testa = 'o'
                else:
                    testa = 'x'

            # Horizontal lines
            for i in [0, 3, 6]:
                koll = [i, i + 1, i + 2]
                if self.twoRow(board, koll, testa) >= 0:
                    board[self.twoRow(board, koll, testa)] = spelare
                    return board
            # Vertical lines
            for i in [0, 1, 2]:
                koll = [i, i + 3, i + 6]
                if self.twoRow(board, koll, testa) >= 0:
                    board[self.twoRow(board, koll, testa)] = spelare
                    return board
            
            # Diagonals
            if self.twoRow(board, [0, 4, 8], testa) >= 0:
                board[self.twoRow(board, [0, 4, 8], testa)] = spelare
                return board

            if self.twoRow(board, [2, 4, 6], testa) >= 0:
                board[self.twoRow(board, [2, 4, 6], testa)] = spelare
                return board
        
        plats = []
        for i in range(0, 9):
            if board[i] == '*':
                plats.append(i)
        board[plats[randint(0, len(plats) -1)]] = spelare
        return board
    
    def start(self, newGame=False):

        #definera spelplanen
        tur = 0
        spelare = 'x'

        # Check if returning to menu
        if not newGame:
            # Starting for the first time
            self.gui = GUI()
            self.gui.createWindow()
            self.gui.createStatus("välkommen till luffarschack")
        else:
            # Returning to main menu
            self.gui.setStatus("välkommen till luffarschack")

        # Display main menu
        select = self.mainMenu()
        
        # Respond to menu selection
        if select == 0:
            # Play against AI @ 3x3 grid
            intelligens = [0, 1]
            width = 3
            xInRow = 3
        
        elif select == 1:
            # PVP
            intelligens = [0, 0]
            # Display board selection
            width = self.boardMenu()
            #välj hur många i rad man ska ha för att vinna
            xInRow = self.xInRowMenu(width)

        elif select == 2:
            # Close game
            sys.exit()

        #visa spelplanen för spelarna
        board = ['*']*(width**2)
        self.playingField(board)
        self.gui.createBoard([500,500],[width,width])
        self.gui.update()

        #mainloop i spelet
        while True:

            #hoppa mellan spelare 0 som spelar som x och spelare 1 som spelar som o
            tur %= 2
            if tur == 0:
                spelare = 'x'
            else:
                spelare = 'o'
        
            #Gör ett drag
            if intelligens[tur] == 0:
                # Vänta på spelare
                board = self.man(spelare, board)
            else:
                # AI
                self.msleep(randint(50,250)) # Sleep a couple milliseconds to "emulate" a real person
                board = self.ai(spelare, board)

            #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
            self.playingField(board)
            self.winCheck(board, spelare, width, xInRow)
            tur += 1




    ###  Menues
    def mainMenu(self):
        self.gui.createMenu(["Human vs AI", "PvP", "Avsluta spelet"], 100)
        self.gui.update()
        return self.gui.waitForMenu()

    def boardMenu(self):
        self.gui.setStatus("Välj hur stort spelbräde du vill ha")
        self.gui.createMenu(["3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"], 100)
        self.gui.update()
        return self.gui.waitForMenu() + 3

    def xInRowMenu(self, width):
        self.gui.setStatus("välj hur många i rad man ska ha för att vinna")
        self.gui.createMenu(list(map(str,range(2,width+1))), 100)
        self.gui.update()
        return self.gui.waitForMenu() + 2

    ### Millisleep
    def msleep(self, sleep):
        ref, now = time.clock(), time.clock() # Set reference to now
        while (now - ref) < (sleep/1000):
            now = time.clock()