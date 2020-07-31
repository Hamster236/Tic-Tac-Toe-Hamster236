"""
Create Stats Window.

The stats window contains all players and player stats. Player stats are
the name, wins, loss, and ratio of wins per play. It will also contain a
numbering system that will show the most recent players games first.
"""

import tkinter as tk
import tkinter.ttk as ttk
import NewGame as ng


class StatsPage:
    """Stats Page Class."""

    def __init__(self, window, players, player_list, winner_message):
        """
        Initialize the Stats Page Class.

        Input the window, all players, and a most recent winning player
        message. Then create the window.
        """
        self.window = window
        self.players = players
        self.player_list = player_list
        self.winner_message = winner_message
        self.style = ttk.Style()
        self.create_frame()

    def create_frame(self):
        """Create frame and add recent results."""
        stats_frame = tk.Frame(self.window, relief=tk.RAISED)
        stats_frame.grid(row=0, column=0)
        stats_canvas_winner_results = tk.Canvas(stats_frame)
        stats_canvas_winner_results.grid(row=0, column=0)
        self.display_winner(stats_canvas_winner_results)
        stats_canvas_player_results = tk.Canvas(stats_frame)
        stats_canvas_player_results.grid(row=1, column=0)
        self.display_player_stats(stats_canvas_player_results)

        ng.NewGame(self.window, self.players, self.player_list)

    def display_winner(self, canvas):
        """Display Winner."""
        winner_message = tk.Label(canvas, text=self.winner_message)
        winner_message.grid(row=0, column=0)

    def display_player_stats(self, canvas):
        """Display individual player stats."""
        tree = self.treeview_setup(canvas)
        self.fill_treeview(tree)

    def treeview_setup(self, canvas):
        """
        Create list as treeview.

        Creates the headings and columns for the treeview. For added benefit,
        a scrollbar is added to both vertical and horizontal planes. Once
        the headings and scrollbars are added, the window is configured to
        handle the treeview as a list.
        """
        headings = ('name', 'wins', 'losses', 'ratio')
        tree = ttk.Treeview(columns=headings)
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
        y_scroll_bar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
        x_scroll_bar = ttk.Scrollbar(orient=tk.HORIZONTAL, command=tree.xview)
        tree['yscroll'] = y_scroll_bar.set
        tree['xscroll'] = x_scroll_bar.set
        tree.grid(in_=canvas, row=1, column=0, sticky=tk.NSEW)
        y_scroll_bar.grid(in_=canvas, row=1, column=1, sticky=tk.NS)
        x_scroll_bar.grid(in_=canvas, row=2, column=0, sticky=tk.EW)
        canvas.columnconfigure(0, weight=1)
        self.style.map('Treeview',
                       foreground=self.fix_tree_mapping('foreground'),
                       background=self.fix_tree_mapping('background'))
        tree.tag_configure('even', background='white')
        tree.tag_configure('odd', background='grey90')
        return tree

    def fill_treeview(self, tree):
        """Fill Stats list with player stats."""
        for i, player in enumerate(self.player_list, start=1):
            data = [player.name,
                    player.wins,
                    player.losses,
                    "%.3f" % player.ratio]
            if i % 2 == 0:
                tags = ('even')
            else:
                tags = ('odd')
            tree.insert('', tk.END, text='%3d' % i, values=data, tags=tags)

    def fix_tree_mapping(self, option):
        """
        Fix Tree Mapping colors.

        FIXME: This code exists for changing entry colors....
        Should tkinter be updated in the future, can remove.
        Fix reference: https://bugs.python.org/issue36468
        """
        return [elm for elm in self.style.map('Treeview', query_opt=option) if
                elm[:2] != ('!disabled', '!selected')]
