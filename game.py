from gui import *

class Game:
    #def __init__(self):
    
    def playingField(self, board):
        print(board[:3])
        print(board[3:6])
        print(board[6:])
    
    def newGame(self,YellerN):

        #loopa tills man antingen fått ett svar y dvs spela en ny omgång eller n ingen ny omgång. exit ifall nej, nyttspel ifall y
        while 1:
            if YellerN == 'y':
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

        print('grattis ', spelare, ' du har vunnit, vill du spela igen y/n?\n')
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
            self.newGame(input('oavgjort, vill du spela igen y/n?\n'))

    def playerAction(self,spelare):
        
        print('spelare ', spelare, 'välj en tom plats på spelplanen igenom att trycka 0-8')
        return self.gui.getSegment()
        
        
        
                
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

    def start(self):
        
        #definera spelplanen
        board = ['*']*9

        print('Välkommen till luffarschack')
        tur = 0
        spelare = 'x'
        self.gui = GUI()
        self.gui.createGrid()
        #visa spelplanen för spelarna
        self.playingField(board)

        #mainloop i spelet
        while True:

            #hoppa mellan spelare 0 som spelar som x och spelare 1 som spelar som o
            tur %= 2
            if tur == 0:
                spelare = 'x'
            else:
                spelare = 'o'

        
            #Gör ett drag
            board = self.man(spelare, board)


            #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
            self.playingField(board)
            self.winCheck(board, spelare)
            tur += 1