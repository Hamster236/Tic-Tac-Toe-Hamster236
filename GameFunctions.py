import tkinter as tk

class gameFunctions:
    def __init__(self, window):
        print("[INFO]\tInitializing game mechanics...")
        self.window = window

        # Player/Winner variables
        self.counter = 0
        self.winner = 0
    
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

    def playerSelect(self, button):
        if (self.counter % 2) ==  0:
            self.playerOneAction(button)
        else:
            self.PlayerTwoAction(button)
        self.counter = self.counter + 1
        self.catsGameCheck()

    def checkButton(self, button, id, player):
        if id == 1:
            player[1,1] = 1
        elif id == 2:
            player[1,2] = 1
        elif id == 3:
            player[1,3] = 1
        elif id == 4:
            player[2,1] = 1
        elif id == 5:
            player[2,2] = 1
        elif id == 6:
            player[2,3] = 1
        elif id == 7:
            player[3,1] = 1
        elif id == 8:
            player[3,2] = 1
        elif id == 9:
            player[3,3] = 1
        else:
            # should never reach here
            player[0,0] = 0

    def checkWin(self, player):
        # 1st Row
        if player[1,1] == 1 and player[1,2] == 1 and player[1,3] == 1:
            player[1,0] = 1
        # 2nd Row
        elif player[2,1] == 1 and player[2,2] == 1 and player[2,3] == 1:
            player[1,0] = 1
        # 3rd Row
        elif player[3,1] == 1 and player[3,2] == 1 and player[3,3] == 1:
            player[1,0] = 1
        # 1st Column
        elif player[1,1] == 1 and player[2,1] == 1 and player[3,1] == 1:
            player[1,0] = 1
        # 2nd Column
        elif player[1,2] == 1 and player[2,2] == 1 and player[3,2] == 1:
            player[1,0] = 1
        # 3rd Column
        elif player[1,3] == 1 and player[2,3] == 1 and player[3,3] == 1:
            player[1,0] = 1
        # Top Left to Bottom Right
        elif player[1,1] == 1 and player[2,2] == 1 and player[3,3] == 1:
            player[1,0] = 1
        # Bottom Left to Top Right
        elif player[3,1] == 1 and player[2,2] == 1 and player[1,3] == 1:
            player[1,0] = 1