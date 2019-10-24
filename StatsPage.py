import tkinter as tk
import tkinter.ttk as ttk

class StatsPage:
    def __init__(self, window, playerlist, winner_message):
        self.window = window
        self.playerlist = playerlist
        self.winner_message = winner_message
        self.style = ttk.Style()
        self.createFrame()


    def createFrame(self):
        stats_frame = tk.Frame(self.window, relief=tk.RAISED)
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
        tree = self.TreeviewSetup(canvas)
        self.fillTreeview(tree)


    def TreeviewSetup(self, canvas):
        # data columns
        headings = ('name', 'wins', 'losses', 'ratio')

        # Treeview setup
        tree = ttk.Treeview(columns=headings)

        # headings and columns setup
        tree.heading('#0', text='#', anchor=tk.E)
        tree.heading('name', text='Name', anchor=tk.W)
        tree.heading('wins', text='Wins', anchor=tk.E)
        tree.heading('losses', text='Losses', anchor=tk.E)
        tree.heading('ratio', text='W/L Ratio', anchor=tk.E)

        tree.column('#0', stretch=0, width=50, anchor=tk.E)
        tree.column('name', stretch=1, width=100, anchor=tk.W)
        tree.column('wins', stretch=0, width=50, anchor=tk.E)
        tree.column('losses', stretch=0, width=50, anchor=tk.E)
        tree.column('ratio', stretch=0, width=75, anchor=tk.E)

        # scrollbar setup
        y_scroll_bar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
        x_scroll_bar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=tree.xview)
        tree['yscroll'] = y_scroll_bar.set
        tree['xscroll'] = x_scroll_bar.set

        # grid setup
        tree.grid(in_=canvas, row=1, column=0, sticky=tk.NSEW)
        y_scroll_bar.grid(in_=canvas, row=1, column=1, sticky=tk.NS)
        x_scroll_bar.grid(in_=canvas, row=2, column=0, sticky=tk.EW)

        # resize the column size of the window
        canvas.columnconfigure(0, weight=1)

        # FIXME:
        self.style.map('Treeview', foreground=self.fixTreeMapping('foreground'),
                       background=self.fixTreeMapping('background'))

        # tags for even and odd to show rows
        tree.tag_configure('even', background='white')
        tree.tag_configure('odd', background='grey90')

        return tree

    
    def fillTreeview(self, tree):
        for i, player in enumerate(self.playerlist, start=1):
            data = [player.name, player.wins, player.losses, player.ratio]
            if i%2 == 0:
                tags = ('even')
            else:
                tags = ('odd')
            tree.insert('', tk.END, text='%3d'%i, values=data, tags=tags)

    
    # FIXME: This code exists for changing entry colors....
    # Should tkinter be updated in the future, can remove.
    def fixTreeMapping(self, option):
        return [elm for elm in self.style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]