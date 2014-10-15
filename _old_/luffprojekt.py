# funktionen spelplan() printar ut spelplanen första raden printar första raden av spelplanen osv
def spelplan(board):
    print(board[:3])
    print(board[3:6])
    print(board[6:])


#kollar ifall spelaren vill köra en ny spelomgång. YellerN innehåller input från spelaren om de vill spela en ny omgång eller ej
def nytt(YellerN):

    #loopa tills man antingen fått ett svar y dvs spela en ny omgång eller n ingen ny omgång. exit ifall nej, nyttspel ifall y
    while 1:
        if YellerN == 'y':
            nyttspel()
        elif YellerN == 'n':
            exit()

        YellerN = input('felaktig input, vill du spela igen y/n?\n')

#funktionen vinnarrad kollar ifall det är tre i rad
def vinnarrad(board, spelare, koll):

    #Gå igenom dem rutorna som ska kollas, dvs rutorna i koll. Finns det någon ruta som innehåller något annat än spelarens tecken avsluta funktionen. Finns det bara spelarens tecken i koll så har spelaren vunnit.
    for i in koll:
        if board[i] is not spelare:
            return None

    print('grattis ', spelare, ' du har vunnit, vill du spela igen y/n?\n')
    nytt(input())


#Går igenom brädan och skickar alla potentiella tre i rader till vinnarrad()
def vinstkoll(board, spelare):

    #kolla dem vågrätta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst
    for i in [0, 3, 6]:
        koll = [i, i + 1, i + 2]
        vinnarrad(board, spelare, koll)

    #kolla dem lodräta raderna igenom att spara dem i koll och sedan skicka brädet till vinnarrad som kollar ifall raden innehåller en vinst
    for i in [0, 1, 2]:
        koll = [i, i + 3, i + 6]
        vinnarrad(board, spelare, koll)

    #kolla diagonalerna
    vinnarrad(board, spelare, [0, 4, 8])
    vinnarrad(board, spelare, [2, 4, 6])

    #om det inte finns någon tom ruta, dvs ingen ruta som innehåller '*' så är spelet oavgjort. Informera spelaren och fråga om en ny omgång
    if '*' not in board:
        nytt(input('oavgjort, vill du spela igen y/n?\n'))


def attgora(spelare):
    while True:
        try:
            print('spelare ', spelare, 'välj en tom plats på spelplanen igenom att trycka 0-8')
            var = int(input())
            if var >= 0 and var <= 8:
                return var
            print("felaktg input")

        except ValueError:
            print('felaktig input')
            continue


#Människor gör ett drag
def man(spelare, board):
    
    var = attgora(spelare)
    while True:
        if board[var] != '*':
            print('Den platsen är upptagen, försök igen')
            var = attgora(spelare)

        else:
            board[var] = spelare
            return board


def nyttspel():
    #definera spelplanen
    board = ['*'] * 9

    print('Välkommen till luffarschack')
    tur = 0
    spelare = 'x'
    #visa spelplanen för spelarna
    spelplan(board)

    #mainloop i spelet
    while True:

        #hoppa mellan spelare 0 som spelar som x och spelare 1 som spelar som o
        tur %= 2
        if tur == 0:
            spelare = 'x'
        else:
            spelare = 'o'

        
        #Gör ett drag
        board = man(spelare, board)


        #visa spelplanen efter spelarens drag, kolla ifall spelaren har vunnit och öka tur med 1
        spelplan(board)
        vinstkoll(board, spelare)
        tur += 1

#börja en spelomgång!
nyttspel()