import tkinter as tk

class gameFunctions:
    def __init__(self):
        print("[INFO]\tInitializing game mechanics...")
        self.counter = 0
    
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

    def playerSelect(self, button):
        if (self.counter % 2) ==  0:
            self.playerOneAction(button)
        else:
            self.PlayerTwoAction(button)
        self.counter = self.counter + 1