"""
Class that saves player names and scores.

The first time the program is played, a file is created and the names with
the scores are saved. Every game played afterwards saves the names and
scores as well. If a name is used more than once, the scores for that name
will be updated.
"""

import os
import csv
import Player as player


class SavedData:
    """Save Data Class."""

    def __init__(self):
        """
        Initialize setup of SaveData class.

        Adds the file name, file headers, line count, and creates the
        savedata.csv if one is not found in current directory.
        """
        self.file_name = 'savedata.csv'
        self.info = ['Name', 'Wins', 'Losses', 'Ratio']
        if not os.path.isfile(self.file_name):
            self.write_title()

    def write_title(self):
        """
        Write title of the savedata.csv file.

        Adds Name, Wins, Losses, and Ratio as headers to the csv.
        """
        with open(self.file_name, 'w') as save_data:
            writer = csv.DictWriter(save_data, fieldnames=self.info)
            writer.writeheader()

    def read_data(self, player_one_name, player_two_name):
        """
        Read data from savedata.csv file.

        All players and data are stored in memory. If the list already
        contains current player name, load that data into current players
        stats.
        """
        line_count = 0
        player_one_name = ''.join(player_one_name.split()).lower()
        player_two_name = ''.join(player_two_name.split()).lower()
        players = [player.Player(), player.Player()]
        player_list = []
        players[0].name = player_one_name
        players[1].name = player_two_name
        with open(self.file_name, 'r+') as save_data:
            reader = csv.DictReader(save_data)
            for user in reader:
                if user['Name'] == player_one_name:
                    players[0].name = user['Name']
                    players[0].wins = int(user['Wins'])
                    players[0].losses = int(user['Losses'])
                    players[0].ratio = float(user['Ratio'])
                elif user['Name'] == player_two_name:
                    players[1].name = user['Name']
                    players[1].wins = int(user['Wins'])
                    players[1].losses = int(user['Losses'])
                    players[1].ratio = float(user['Ratio'])
                player_list.append(player.Player(user['Name'],
                                                 int(user['Wins']),
                                                 int(user['Losses']),
                                                 float(user['Ratio'])))
                line_count += 1
        return players, player_list

    def write_data(self, players, player_list):
        """
        Write player data to the savedata.csv file.

        Updates the player_list and gathers the number of players before
        writing players to the file.
        """
        player_list, line_count = self.update_player_list(players, player_list)
        self.write_title()
        with open(self.file_name, 'a+', newline='') as save_data:
            writer = csv.DictWriter(save_data, fieldnames=self.info)
            for i in range(0, line_count):
                writer.writerow({'Name': player_list[i].name,
                                 'Wins': player_list[i].wins,
                                 'Losses': player_list[i].losses,
                                 'Ratio': player_list[i].ratio})

    def update_player_list(self, players, player_list):
        """
        Update player_list with current player data.

        Checks for a non-empty list and if a player exists in the list.
        If one or neither exist, creates new list elements of the players and
        sets the stats. If both exits, updates the player stats for that
        player.
        """
        player0_found = False
        player0_found_index = 0
        player1_found = False
        player1_found_index = 0

        if player_list:
            for i, pl in enumerate(player_list):
                if players[0].name == pl.name:
                    player0_found = True
                    player0_found_index = i
                elif players[1].name == pl.name:
                    player1_found = True
                    player1_found_index = i

        if player1_found:
            player_list[player1_found_index].wins = players[1].wins
            player_list[player1_found_index].losses = players[1].losses
            player_list[player1_found_index].ratio = players[1].ratio
        else:
            player_list.insert(0, player.Player(players[1].name,
                                                players[1].wins,
                                                players[1].losses,
                                                players[1].ratio))
        if player0_found:
            player_list[player0_found_index].wins = players[0].wins
            player_list[player0_found_index].losses = players[0].losses
            player_list[player0_found_index].ratio = players[0].ratio
        else:
            player_list.insert(0, player.Player(players[0].name,
                                                players[0].wins,
                                                players[0].losses,
                                                players[0].ratio))
        return player_list, len(player_list)
