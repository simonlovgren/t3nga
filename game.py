from random import randint
from gui import *

class Game:
    #def __init__(self):
    
    def playingField(self, board):
        print(board[:3])
        print(board[3:6])
        print(board[6:])
        
        for i in range(0,9):
            if board[i] == 'x':
                self.gui.addMarker(i, 0)
            elif board[i] == 'o':
                self.gui.addMarker(i, 1) 

        self.gui.update()
                       
    def newGame(self,YellerN):

        #loopa tills man antingen fått ett svar y dvs spela en ny omgång eller n ingen ny omgång. exit ifall nej, nyttspel ifall y
        while 1:
            if YellerN == 'y':
                self.gui.close()
                self.start()
            elif YellerN == 'n':
                exit()

            YellerN = input('felaktig input, vill du spela igen y/n?\n')
            
    def start(self, start):
        #loopa tills man antingen fått ett svar y dvs spela en ny omgång eller n ingen ny omgång. exit ifall nej, nyttspel ifall y
        while True:
            if YellerN == 'y':
                self.start()
            elif YellerN == 'n':
                exit()

            YellerN = input('felaktig input, vill du spela igen y/n?\n')

    def winRow(self, board, spelare, koll):

        #Gå igenom dem rutorna som ska kollas, dvs rutorna i koll. Finns det någon ruta som innehåller något annat än spelarens tecken avsluta funktionen. Finns det bara spelarens tecken i koll så har spelaren vunnit.
        for i in koll:
            if board[i] is not spelare:
                return None

        print('grattis ' + spelare + ' du har vunnit, vill du spela igen y/n?\n')
        self.gui.setStatus('grattis ' + spelare + ' du har vunnit, vill du spela igen y/n?\n')
        self.newGame(input())
        
    def winCheck(self, board, spelare):

        #kolla dem vågrätta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst
        for i in [0, 3, 6]:
            koll = [i, i + 1, i + 2]
            self.winRow(board, spelare, koll)

        #kolla dem lodräta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst
        for i in [0, 1, 2]:
            koll = [i, i + 3, i + 6]
            self.winRow(board, spelare, koll)

        #kolla diagonalerna
        self.winRow(board, spelare, [0, 4, 8])
        self.winRow(board, spelare, [2, 4, 6])

        #om det inte finns någon tom ruta, dvs ingen ruta som innehåller '*' så är spelet oavgjort. Informera spelaren och fråga om en ny omgång
        if '*' not in board:
            self.gui.setStatus('oavgjort, vill du spela igen?')
            self.newGame(input('oavgjort, vill du spela igen y/n?\n'))

    def playerAction(self,spelare):
        
        print('spelare ' + spelare + ' välj en tom plats på spelplanen igenom att trycka 0-8')
        self.gui.setStatus('spelare ' + spelare + ' välj en tom plats på spelplanen igenom att trycka på den')
        return self.gui.waitForBoard()
        
        
        
                
    #Människor gör ett drag
    def man(self, spelare, board):
    
        var = self.playerAction(spelare)
        while True:
            if board[var] != '*':
                print('Den platsen är upptagen, försök igen')
                var = self.playerAction(spelare)

            else:
                board[var] = spelare
                return board

    def twoRow(self, board, koll, testa):
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
                    print("varv två")

            for i in [0, 3, 6]:
                koll = [i, i + 1, i + 2]
                if self.twoRow(board, koll, testa) >= 0:
                    board[self.twoRow(board, koll, testa)] = spelare
                    print(spelare, ':')
                    return board

            for i in [0, 1, 2]:
                koll = [i, i + 3, i + 6]
                if self.twoRow(board, koll, testa) >= 0:
                    board[self.twoRow(board, koll, testa)] = spelare
                    print(spelare, ':')
                    return board
        
            if self.twoRow(board, [0, 4, 8], testa) >= 0:
                board[self.twoRow(board, [0, 4, 8], testa)] = spelare
                print(spelare, ':')
                return board

            if self.twoRow(board, [2, 4, 6], testa) >= 0:
                board[self.twoRow(board, [2, 4, 6], testa)] = spelare
                print(spelare, ':')
                return board
        

        print(board)
        plats = []
        for i in range(0, 9):
            if board[i] == '*':
                plats.append(i)
        board[plats[randint(0, len(plats) -1)]] = spelare
        return board
    
    def start(self):
        
        #definera spelplanen
        board = ['*']*9
        tur = 0
        spelare = 'x'
        self.gui = GUI()
        self.gui.createWindow()
        self.gui.createStatus("välkommen till luffarschack")
        self.gui.createMenu(["Human vs AI", "PvP"], 100)
        self.gui.update()
        select = self.gui.waitForMenu()
        if select == 0:
            intelligens = [0, 1]
        elif select == 1:
            intelligens = [0, 0]
        #visa spelplanen för spelarna
        self.playingField(board)
        self.gui.createBoard()
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
                board = self.man(spelare, board)
            else:
                board = self.ai(spelare, board)

            #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
            self.playingField(board)
            self.winCheck(board, spelare)
            tur += 1