import tkinter as tk
import BoardDraw as bd
import SaveData as sd
import StatsPage as sp

class BoardFunctions:
    def __init__(self, window):
        self.window = window

    def setup(self):
        self.counter = 0
        self.winner  = 0
        self.played_games = 1
        self.player_wins = [0, 0]
        self.sd = sd.SavedData()
        
        self.bd = bd.BoardDraw(self.window)
        self.bd.create()

        self.config_buttons()
        self.clear_stats()
        self.set_message_label()
        self.message_update('Player ' + self.players[0].name + '\'s Turn')

    def set_message_label(self):
        self.message_label = self.bd.label()

    def set_board_size(self, board_size):
        self.board_size = board_size

    def set_best_of_games(self, number_of_games):
        self.number_of_games = number_of_games
        self.winners_advantage = self.number_of_games // 2 + 1

    def set_player(self, players, player_list):
        self.players = players
        self.player_list = player_list

    def config_buttons(self):
        self.board_buttons = []
        self.board_buttons = self.bd.buttons(self.board_size)

        for i in range(self.board_size * self.board_size):
            self.board_buttons[i].configure(command=lambda i=i: self.player_select(self.board_buttons[i], i+1))
            self.board_buttons[i].grid(row=(int(i/self.board_size)%self.board_size)+1,column=(int(i)%self.board_size))

    def clear_stats(self):
        num_elements = self.board_size * self.board_size + 1
        self.players[0].spaces = [0] * num_elements
        self.players[1].spaces = [0] * num_elements
        self.counter = 0

    def clear_board(self):
        for i in range(self.board_size * self.board_size):
            self.board_buttons[i].configure(state='normal',text='-',fg='Black')
    
    def end_frame_setup(self):
        self.end_frame = tk.Frame(self.window, bg='White')
        self.end_frame.grid(row=0,column=0,sticky='nsew')
    
    def message_update(self, message):
        self.message_label.config(text=message)
        self.window.update()

    def player_one_action(self, button):
        button.config(text='X',state='disabled',disabledforeground='Red')

    def player_two_action(self, button):
        button.config(text='O',state='disabled',disabledforeground='Blue')

    def cats_game_check(self):
        if self.counter == self.board_size * self.board_size and self.winner == 0:
            self.message_update("Cats Game!")
            self.clear_stats()
            self.clear_board()

    def player_select(self, button, id):
        self.id = id
        if (self.counter % 2) ==  0:
            self.player_one_action(button)
            self.message_update(self.players[1].name + '\'s Turn')
            self.check_win(button, self.players[0])
        else:
            self.player_two_action(button)
            self.message_update(self.players[0].name + '\'s Turn')
            self.check_win(button, self.players[1])
        self.counter = self.counter + 1
        self.cats_game_check()

    def check_row(self, player):
        # Create a counter for the row. If False, no winner.
        row_win = False
        for i in range(0, self.board_size):
            count_to_win = 0
            for j in range(1, self.board_size+1):
                if player.spaces[self.board_size*i + j] is 1:
                    count_to_win+=1
            if count_to_win is self.board_size:
                row_win = True
                break
        return row_win

    def check_column(self, player):
        column_win = False
        for i in range(1, self.board_size+1):
            count_to_win = 0
            for j in range(0, self.board_size):
                if player.spaces[i + self.board_size*j] is 1:
                    count_to_win+=1
            if count_to_win is self.board_size:
                column_win = True
                break
        return column_win

    def check_diagonal(self, player):
        diagonal_win = False
        count_to_win = 0
        for i in range(0, self.board_size):
            if player.spaces[(self.board_size*i)+(i+1)] is 1:
                count_to_win+=1
        if count_to_win is not self.board_size:
            count_to_win = 0
            for i in range(1, self.board_size+1):
                if player.spaces[(self.board_size*i) - (i-1)] is 1:
                    count_to_win+=1
            if count_to_win is self.board_size:
                diagonal_win = True
        else:
            diagonal_win = True
        return diagonal_win

    def ready_for_reset(self):
        if self.played_games is not self.number_of_games and \
           self.player_wins[0] is not self.winners_advantage and \
           self.player_wins[1] is not self.winners_advantage:
            self.clear_stats()
            self.clear_board()
            self.played_games+=1
            if self.played_games%2 is 0:
                self.counter = 0
            else:
                self.counter = 1
        else:
            if self.player_wins[0] > self.player_wins[1]:
                winner_message = self.players[0].name + " is the Best!!"
            else:
                winner_message = self.players[1].name + " is the Best!!"
            if self.players[0].losses != 0:
                self.players[0].ratio = self.players[0].wins / (self.players[0].wins + self.players[0].losses)
            else:
                self.players[0].ratio = 1.0
            if self.players[1].losses != 0:
                self.players[1].ratio = self.players[1].wins / (self.players[1].wins + self.players[1].losses)
            else:
                self.players[1].ratio = 1.0
            self.sd.write_data(self.players, self.player_list) # Update SaveData for this param
            self.bd.destroy()
            self.end_frame_setup()
            sp.StatsPage(self.end_frame, self.player_list, winner_message)

    def check_win(self, button, player):
        player.spaces[self.id] = 1
        row_check = self.check_row(player)
        if row_check is not True:
            column_check = self.check_column(player)
            if column_check is not True:
                diag_check = self.check_diagonal(player)

        if row_check or column_check or diag_check:
            if player is self.players[0]:
                self.message_update(self.players[0].name + " is the winner!")
                self.players[0].wins+=1
                self.players[1].losses+=1
                self.player_wins[0]+=1
                self.ready_for_reset()
            else:
                self.message_update(self.players[1].name + "is the winner!")
                self.players[1].wins+=1
                self.players[0].losses+=1
                self.player_wins[1]+=1
                self.ready_for_reset()