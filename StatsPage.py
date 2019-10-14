import tkinter as tk

class StatsPage:
    def __init__(self, window, playerlist, winner_message):
        self.window = window
        self.playerlist = playerlist
        self.winner_message = winner_message
        self.createFrame()

    def createFrame(self):
        stats_frame = tk.Frame(self.window, bg='White', relief=tk.RAISED)
        stats_frame.grid(row=0, column=0)

        stats_canvas_winner_results = tk.Canvas(stats_frame)
        stats_canvas_winner_results.grid(row=0, column=0)

        self.displayWinner(stats_canvas_winner_results)

        stats_canvas_player_results = tk.Canvas(stats_frame)
        stats_canvas_player_results.grid(row=1, column=0)
        
        self.displayPlayerStats(stats_canvas_player_results)

    def displayWinner(self, canvas):
        winner_message = tk.Label(canvas, text=self.winner_message)
        winner_message.grid(row=0, column=0)

    def displayPlayerStats(self, canvas):
        scrollbar = tk.Scrollbar(canvas)
        scrollbar.grid(row=1, column=5, sticky='ns')
        self.listbox_names = tk.Listbox(canvas, yscrollcommand=scrollbar.set)
        self.listbox_wins = tk.Listbox(canvas, yscrollcommand=scrollbar.set)
        self.listbox_losses = tk.Listbox(canvas, yscrollcommand=scrollbar.set)
        self.listbox_ratios = tk.Listbox(canvas, yscrollcommand=scrollbar.set)
        for player in self.playerlist:
            self.listbox_names.insert(tk.END, player.name)
            self.listbox_wins.insert(tk.END, player.wins)
            self.listbox_losses.insert(tk.END, player.losses)
            self.listbox_ratios.insert(tk.END, player.ratio)
        self.listbox_names.grid(row=1, column=0)
        self.listbox_wins.grid(row=1, column=1)
        self.listbox_losses.grid(row=1, column=2)
        self.listbox_ratios.grid(row=1, column=3)
        scrollbar.config(command=self.scrollbarContol)


    def scrollbarContol(self, *args):
        self.listbox_names.yview(*args)
        self.listbox_wins.yview(*args)
        self.listbox_losses.yview(*args)
        self.listbox_ratios.yview(*args)