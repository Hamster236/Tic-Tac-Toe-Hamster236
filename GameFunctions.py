import tkinter as tk

class gameFunctions:
    def __init__(self, window):
        print("[INFO]\tInitializing game mechanics...")
        self.window = window

        # Player/Winner variables
        self.counter = 0
        self.winner = 0

        self.playerOne = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.playerTwo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.id = 0
    
    def playerOneAction(self, button):
        '''
        playerOneAction is the button configure for player one.
        When Player One selects a button, the button will update 
        with an "X" and disable functionality with the button.

        TODO: There are 2 methods that I can roll with here...
        1. Disable the button completely but do no shading, or
        2. Implement a counter that will allow for a message to
        display stating that a player cannot click on the button
        because it has already been clicked before.

        Implementing method 1.
        '''
        button.config(text='X',
                      state='disabled',
                      disabledforeground='Red')

    def PlayerTwoAction(self, button):
        button.config(text='O',
                      state='disabled',
                      disabledforeground='Blue')

    def catsGameCheck(self):
        if self.counter == 9 and self.winner == 0:
            self.window.destroy()

    def playerSelect(self, button, id):
        self.id = id
        if (self.counter % 2) ==  0:
            self.playerOneAction(button)
            self.checkWin(button, self.playerOne)
        else:
            self.PlayerTwoAction(button)
            self.checkWin(button, self.playerTwo)
        self.counter = self.counter + 1
        self.catsGameCheck()

    def checkButton(self, button, player):
        if self.id == 1:
            player[1] = 1
        elif self.id == 2:
            player[2] = 1
        elif self.id == 3:
            player[3] = 1
        elif self.id == 4:
            player[4] = 1
        elif self.id == 5:
            player[5] = 1
        elif self.id == 6:
            player[6] = 1
        elif self.id == 7:
            player[7] = 1
        elif self.id == 8:
            player[8] = 1
        elif self.id == 9:
            player[9] = 1
        else:
            # should never reach here
            player[0] = 0

    def checkWin(self, button, player):
        # Setting button
        self.checkButton(button, player)
        # 1st Row
        if player[1] == 1 and player[2] == 1 and player[3] == 1:
            player[0] = 1
        # 2nd Row
        elif player[4] == 1 and player[5] == 1 and player[6] == 1:
            player[0] = 1
        # 3rd Row
        elif player[7] == 1 and player[8] == 1 and player[9] == 1:
            player[0] = 1
        # 1st Column
        elif player[1] == 1 and player[4] == 1 and player[7] == 1:
            player[0] = 1
        # 2nd Column
        elif player[2] == 1 and player[5] == 1 and player[8] == 1:
            player[0] = 1
        # 3rd Column
        elif player[3] == 1 and player[6] == 1 and player[9] == 1:
            player[0] = 1
        # Top Left to Bottom Right
        elif player[1] == 1 and player[5] == 1 and player[9] == 1:
            player[0] = 1
        # Bottom Left to Top Right
        elif player[7] == 1 and player[5] == 1 and player[3] == 1:
            player[0] = 1

        if player[0] == 1:
            self.window.destroy()