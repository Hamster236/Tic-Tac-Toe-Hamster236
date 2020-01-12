import tkinter as tk
import os
import time
import csv
import Player as player


class SavedData:
    def __init__(self):
        self.file_name = 'savedata.csv'
        self.info = ['Name','Wins','Losses','Ratio']
        self.line_count = 0
        if not os.path.isfile(self.file_name):
            self.write_title()        

    def write_title(self):
        with open(self.file_name, 'w+') as save_data:
            writer = csv.DictWriter(save_data, fieldnames=self.info)
            writer.writeheader()

    
    def read_data(self, player_one_name, player_two_name):
        player_one_name = ''.join(player_one_name.split()).lower()
        player_two_name = ''.join(player_one_name.split()).lower()
        players = [player.Player(), player.Player()]
        player_list = []
        players[0].name = player_one_name
        players[1].name = player_two_name
        with open(self.file_name, 'r+') as save_data:
            reader = csv.DictReader(save_data)
            for user in reader:
                if user['Name'] == player_one_name:
                    players[0].name   = user['Name']
                    players[0].wins   = int(user['Wins'])
                    players[0].losses = int(user['Losses'])
                    players[0].ratio  = float(user['Ratio'])
                elif user['Name'] == player_two_name:
                    players[1].name   = user['Name']
                    players[1].wins   = int(user['Wins'])
                    players[1].losses = int(user['Losses'])
                    players[1].ratio  = float(user['Ratio'])
                player_list.append(player.Player())
                player_list[self.line_count].name = user['Name']
                player_list[self.line_count].wins = user['Wins']
                player_list[self.line_count].losses = user['Losses']
                player_list[self.line_count].ratio = user['Ratio']
                self.line_count+=1
        return players, player_list


    def write_data(self, players, player_list):
        with open(self.file_name, 'a+', newline='') as save_data:
            writer = csv.DictWriter(save_data, fieldnames=self.info)
            writer.writerow({'Name':players[0].name,     \
                             'Wins':players[0].wins,     \
                             'Losses':players[0].losses, \
                             'Ratio':players[0].ratio})
            writer.writerow({'Name':players[1].name,     \
                             'Wins':players[1].wins,     \
                             'Losses':players[1].losses, \
                             'Ratio':players[1].ratio})
            for i in range(0,self.line_count):
                if player_list[i].name != players[0].name or \
                    player_list[i].name != players[1].name:
                    writer.writerow({'Name':player_list[i].name,     \
                                    'Wins':player_list[i].wins,      \
                                    'Losses':player_list[i].losses,  \
                                    'Ratio':player_list[i].ratio})