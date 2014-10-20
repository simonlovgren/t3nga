from random import randint
from gui import *
import network, sys

class Game:
    #def __init__(self):
    
    def playingField(self, board):
        print(board[:3])
        print(board[3:6])
        print(board[6:])
        
        for i in  range(0, len(board)):
            if board[i] == 'x':
                self.gui.addMarker(i, 0)
            elif board[i] == 'o':
                self.gui.addMarker(i, 1) 
        self.gui.update()
                       
    def newGame(self,YellerN):

        #loopa tills man antingen fått ett svar y dvs spela en ny omgång eller n ingen ny omgång. exit ifall nej, nyttspel ifall y
        while 1:
            if YellerN == 'y':
                self.start(True)
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
        
    def winCheck(self, board, spelare, height, width):

        koll = []
        for i in range(0, height):
            i *= width
            for j in range(0, width):
                koll.append(i+j)
            self.winRow(board, spelare, koll)
            koll = []

        #kolla dem lodräta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst

        for i in range(0, width):
            for j in range(0, height):
                koll.append(i+(j*width))
            self.winRow(board, spelare, koll)
            koll = []


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
    
    def start(self, restart = False):
        
        #definera spelplanen
        self.height = 5
        self.width = 5
        self.board = ['*']*(self.height*self.width)

        self.tur = 0
        self.spelare = 'x'

        # Start GUI
        if not restart:
            self.gui = GUI()
            self.gui.createWindow()
            self.gui.createStatus("välkommen till luffarschack")
        else:
            self.gui.setStatus("välkommen till luffarschack")
        self.gui.createMenu(["Human vs AI", "PvP", "Create LAN Game", "Join LAN Game", "Exit game"], 100)
        self.gui.update()

        select = self.gui.waitForMenu()
        if select == 0:
            intelligens = [0, 1]
            self.localGame(intelligens)
        elif select == 1:
            intelligens = [0, 0]
            self.localGame(intelligens)
        elif select == 2:
            self.createNetworkGame()
        elif select == 3:
            self.joinNetworkGame()
        else:
            sys.exit()

    #### Local game loop
    def localGame(self, intelligens):
        #visa spelplanen för spelarna
        self.playingField(self.board)
        self.gui.createBoard([500,500],[self.height,self.width])
        self.gui.update()

        #mainloop i spelet
        while True:

            #hoppa mellan spelare 0 som spelar som x och spelare 1 som spelar som o
            self.tur %= 2
            if self.tur == 0:
                self.spelare = 'x'
            else:
                self.spelare = 'o'

        
            #Gör ett drag
            if intelligens[self.tur] == 0:
                self.board = self.man(self.spelare, self.board)
            else:
                self.board = self.ai(self.spelare, self.board)

            #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
            self.playingField(self.board)
            self.winCheck(self.board, self.spelare, self.height, self.width)
            self.tur += 1




    ##### Network Game
    def createNetworkGame(self):
        print("Create Network Game")
        server = network.MasterSocket(22500)
        print('Your IP:', server.getIP())
        print('Waiting for connection')


        server.listen()
        accept = False

        self.gui.setStatus("Waiting player connect to: " + server.getIP())
        self.gui.update()

        while not accept:
            accept = server.startAcceptingClient()
        print('Connection from', server.addr[0])
        self.gui.setStatus("Player connected from " + server.addr[0])
        self.gui.update()

        # try ack
        ack = False
        tries = 3
        randInt = randint(1574,677852)
        while not ack and tries > 0:
            server.send("ACK:" + str(randInt))
            ackR = server.recieve()
            ackR = network.DataParser.parseData((), ackR)
            if ackR.command == "OK" and ackR.content == str(randInt):
                ack = True
                print("Client OK")

            tries -= 1

        # Client OK, randomize who starts
        localPlayer = randint(0,1)
        remotePlayer = int(not localPlayer)

        # Send remote player
        server.send("PLAYER:" + str(remotePlayer))

        # Wait for OK
        data = server.recieve()
        data = network.DataParser().parseData(data)
        if data.command == "OK":
            print("Client OK")
        else:
            print("Client not responding")

        # Send board
        server.send("BOARD:" + ",".join(self.board))

        # Wait for OK
        data = server.recieve()
        data = network.DataParser().parseData(data)
        if data.command == "OK":
            print("Client OK")
        else:
            print("Client not responding")

        # Send grid
        server.send("GRID:" + str(self.width) + "," + str(self.height))

        # Wait for OK
        data = server.recieve()
        data = network.DataParser().parseData(data)
        if data.command == "OK":
            print("Client OK")
        else:
            print("Client not responding")

        # Display board
        self.gui.createBoard([500,500],[self.height,self.width])

        # Wait for remote set up
        data = ""
        tries = 5
        while data != "CLIENT:READY":
            data = server.recieve()
            data = network.DataParser().parseData(data)
            data = data.command + ":" + data.content

        turn = 0
        playerTurn = 0
        trials = 5
        # Main game-server loop
        while trials > 0:

            # Check which player is to make a move
            playerTurn = (turn % 2 == 0)

            if(turn == localPlayer):
                print("Server turn")
                # Server's turn
                self.gui.setStatus("Your turn!")
                self.gui.update()

                # Wait for input
                move = None
                while not self.validateMove(self.board, move):
                    move = self.gui.waitForBoard()

                print("Server move: ", move)

            else:
                print("Remote turn")
                # Client's turn
                server.send("TURN:REMOTE")
                self.gui.setStatus("Opponent's turn!")
                self.gui.update()

                print("TURN:REMOTE sent")

                # Wait for move
                move = None
                while not self.validateMove(self.board, move):
                    move = network.DataParser().parseData(":")
                    while move.command != "MOVE":
                    print("Awaiting move")
                        move = server.recieve()
                        move = network.DataParser().parseData(data)
                        print("Recieved:", move.command, move.content)
                    print("Received move:", move.content)

                    if not self.validateMove(move.content):
                        print("Invalid move")
                        server.send("MOVE:INVALID")
                print("Valid move")
                server.send("MOVE:VALID")

                print("Client move:", move.content)

            trials -= 1
            turn += 1

            '''
            #Gör ett drag
            if intelligens[self.tur] == 0:
                self.board = self.man(player, self.board)

            #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
            self.playingField(self.board)
            self.winCheck(self.board, self.spelare, self.height, self.width)
            self.tur += 1
            '''


        server.close()
        self.start(True) # Goto main menu
        

    def joinNetworkGame(self):
        self.gui.networkJoinForm()
        self.gui.update()

        addr = self.gui.waitForJoinForm()

        client = network.SlaveSocket(addr[1])
        client.connect(addr[0])

        # wait for ack
        ack = False
        tries = 3
        while not ack and tries > 0:
            ackR = client.recieve()
            ackR = network.DataParser().parseData(ackR)

            if ackR.command == "ACK" and ackR.content:
                ack = True
            else:
                print("Ack failed")

            tries -= 1

        print("Server ACK, sending OK")

        client.send("OK:" + ackR.content)

        # Wait for player assignment
        data = client.recieve()
        print(data)
        data = network.DataParser().parseData(data)

        player = int(data.content)

        # Send OK
        client.send("OK:")

        # Wait for board
        data = client.recieve()
        data = network.DataParser().parseData(data)

        board = data.content.split(",")

        # Send OK
        client.send("OK:")

        # Wait for grid
        data = client.recieve()
        data = network.DataParser().parseData(data)

        grid = list(map(int, data.content.split(","))) # Convert back to list of ints
        print(grid)

        # Send OK
        client.send("OK:")

        # Display board
        self.gui.createBoard([500,500],[grid[0], grid[1]])

        # START ACTUAL GAME SESSION
        gameOn = True
        looped = False
        while gameOn:
            if not looped and player == 0:
                self.gui.setStatus("Waiting for server!")
            else:
                self.gui.setStatus("Opponent's turn!")
            self.gui.update()

            client.send("CLIENT:READY") # Send ready to server

            # Wait for turn
            myTurn = "SERVER"

            while myTurn != "REMOTE":
                turn = network.DataParser().parseData(client.recieve())
                print(turn.command, turn.content)
                if turn.command == "TURN":
                    myTurn = turn.content
                print(myTurn, turn.content)

            self.gui.setStatus("Your turn!")
            self.gui.update()

            moveOK = "INVALID"
            while moveOK != "VALID":
                move = self.gui.waitForBoard()
                print("Move selected:", move)
                client.send("MOVE:" + str(move))
                print("Move sent:", move)
                moveOK = network.DataParser().parseData(client.recieve()).content

                if(moveOK != "VALID"):
                    self.gui.setStatus("Invalid move, try again!")

        looped = True

        client.close()
        self.start(True) # goto main menu


    def validateMove(self, board, move):
            if move == None:
                return False
            else: 
                move = int(move)

            if board[move] != '*':
                return False
            else:
                return True  