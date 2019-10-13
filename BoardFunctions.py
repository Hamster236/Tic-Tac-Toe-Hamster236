import tkinter as tk
import BoardDraw as bd
import SaveData as sd
import StatsPage as sp

class BoardFunctions:
    def __init__(self, window):
        self.window = window

    def __setup__(self):
        # Defining counters
        self.counter = 0
        self.winner  = 0
        self.playedGames = 1
        self.playerWins = [0, 0]

        # Calling the saved data file
        self.sd = sd.SavedData()
        
        # Calling the drawing board
        self.bd = bd.BoardDraw(self.window)
        self.bd.__create__()
        self.configButtons()

        # Clearing stats and updating message board
        self.clearStats()
        self.setMessageLabel()
        self.messageUpdate('Player ' + self.players[0].name + '\'s Turn')

    def setMessageLabel(self):
        self.messageLabel = self.bd.__label__()

    def setBoardSize(self, boardSize):
        self.boardSize = boardSize

    def setBestOfGames(self, numberOfGames):
        self.numberOfGames = numberOfGames
        self.winnersAdvantage = self.numberOfGames // 2 + 1

    def setPlayer(self, players):
        self.players = players

    def configButtons(self):
        self.boardButtons = []
        self.boardButtons = self.bd.__buttons__(self.boardSize)

        for i in range(self.boardSize * self.boardSize):
            self.boardButtons[i].configure(command=lambda i=i: self.playerSelect(self.boardButtons[i], i+1))
            self.boardButtons[i].grid(row=(int(i/self.boardSize)%self.boardSize)+1,column=(int(i)%self.boardSize))

    def clearStats(self):
        numElements = self.boardSize * self.boardSize + 1
        self.players[0].spaces = [0] * numElements
        self.players[1].spaces = [0] * numElements
        self.counter = 0

    def clearBoard(self):
        for i in range(self.boardSize * self.boardSize):
            self.boardButtons[i].configure(state='normal',text='-',fg='Black')
    
    def endFrameSetup(self):
        self.endFrame = tk.Frame(self.window, bg='White')
        self.endFrame.grid(row=0,column=0,sticky='nsew')
    
    def messageUpdate(self, message):
        self.messageLabel.config(text=message)
        self.window.update()

    def playerOneAction(self, button):
        '''
        playerOneAction is the button configure for player one.
        When Player One selects a button, the button will update 
        with an "X" and disable functionality with the button.
        '''
        button.config(text='X',state='disabled',disabledforeground='Red')

    def PlayerTwoAction(self, button):
        button.config(text='O',state='disabled',disabledforeground='Blue')

    def catsGameCheck(self):
        if self.counter == self.boardSize*self.boardSize and self.winner == 0:
            self.messageUpdate("Cats Game!")
            self.clearStats()
            self.clearBoard()

    def playerSelect(self, button, id):
        self.id = id
        if (self.counter % 2) ==  0:
            self.playerOneAction(button)
            self.messageUpdate(self.players[1].name + '\'s Turn')
            self.checkWin(button, self.players[0])
        else:
            self.PlayerTwoAction(button)
            self.messageUpdate(self.players[0].name + '\'s Turn')
            self.checkWin(button, self.players[1])
        self.counter = self.counter + 1
        self.catsGameCheck()

    def checkRow(self, player):
        # Create a counter for the row. If False, no winner.
        rowWin = False
        for i in range(0, self.boardSize):
            countToWin = 0
            for j in range(1, self.boardSize+1):
                if player.spaces[self.boardSize*i + j] is 1:
                    countToWin+=1
            if countToWin is self.boardSize:
                rowWin = True
                break
        return rowWin

    def checkColumn(self, player):
        columnWin = False
        for i in range(1, self.boardSize+1):
            countToWin = 0
            for j in range(0, self.boardSize):
                if player.spaces[i + self.boardSize*j] is 1:
                    countToWin+=1
            if countToWin is self.boardSize:
                columnWin = True
                break
        return columnWin

    def checkDiagonal(self, player):
        diagonalWin = False
        countToWin = 0
        for i in range(0, self.boardSize):
            if player.spaces[(self.boardSize*i)+(i+1)] is 1:
                countToWin+=1
        if countToWin is not self.boardSize:
            countToWin = 0
            for i in range(1, self.boardSize+1):
                if player.spaces[(self.boardSize*i) - (i-1)] is 1:
                    countToWin+=1
            if countToWin is self.boardSize:
                diagonalWin = True
        else:
            diagonalWin = True
        return diagonalWin

    def readyForReset(self):
        if self.playedGames is not self.numberOfGames and \
           self.playerWins[0] is not self.winnersAdvantage and \
           self.playerWins[1] is not self.winnersAdvantage:
            self.clearStats()
            self.clearBoard()
            self.playedGames+=1
            if self.playedGames%2 is 0:
                self.counter = 0
            else:
                self.counter = 1
        else:
            if self.playerWins[0] > self.playerWins[1]:
                winnerMessage = self.players[0].name + " is the Best!!"
            else:
                winnerMessage = self.players[1].name + " is the Best!!"
            if self.players[0].losses != 0:
                self.players[0].ratio = self.players[0].wins / (self.players[0].wins + self.players[0].losses)
            else:
                self.players[0].ratio = 1.0
            if self.players[1].losses != 0:
                self.players[1].ratio = self.players[1].wins / (self.players[1].wins + self.players[1].losses)
            else:
                self.players[1].ratio = 1.0
            self.sd.writeData(self.players) # Update SaveData for this param
            self.bd.__destroy__()
            self.endFrameSetup()
            # endLabel = tk.Label(self.endFrame, text=winnerMessage)
            # endLabel.grid(row=1,column=1,columnspan=2)
            sp.StatsPage(self.endFrame, self.sd.playerlist, winnerMessage)

    # TODO: This function needs to be refactored to be solely based on player. 
    def checkWin(self, button, player):
        '''
        checkWin checks for 3 buttons in a straight line. If the player
        has 3 buttons in a straight line, they are deemed the winner.
        
        *** inputs ***
        button: The button that was clicked
        player: Either playerOne or playerTwo

        *** Logic ***
        Each player is a boardSize x boardSize element array all 
        initialized to 0. The elements change to 1 if that button is 
        pressed.
        
        Once the winner is found:
        1. Message displaying winner
        2. Board reset
        '''
        player.spaces[self.id] = 1
        rowCheck = self.checkRow(player)
        if rowCheck is not True:
            columnCheck = self.checkColumn(player)
            if columnCheck is not True:
                diagCheck = self.checkDiagonal(player)

        if rowCheck or columnCheck or diagCheck:
            if player is self.players[0]:
                self.messageUpdate(self.players[0].name + " is the winner!")
                self.players[0].wins+=1
                self.players[1].losses+=1
                self.playerWins[0]+=1
                self.readyForReset()
            else:
                self.messageUpdate(self.players[1].name + "is the winner!")
                self.players[1].wins+=1
                self.players[0].losses+=1
                self.playerWins[1]+=1
                self.readyForReset()