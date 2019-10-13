import tkinter as tk

class StatsPage:
    def __init__(self, window, players, winner_message):
        self.window = window
        self.players = players
        self.winner_message = winner_message

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
        for i, player in enumerate(self.players):
            for j in range(4):
                tk.Label(canvas, text=player[i][j])