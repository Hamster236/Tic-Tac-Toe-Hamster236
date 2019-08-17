import tkinter as tk
import os
import time
import csv
import Player as player

class SavedData:
    def __init__(self):
        self.filename = 'savedata.csv'
        self.info = ['Name','Wins','Losses','Ratio']
        if not os.path.isfile(self.filename):
            self.writeTitle()
        
    def writeTitle(self):
        with open(self.filename, 'w+') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writeheader()
        
    def readData(self, player1Name, player2Name):
        player1Name = ''.join(player1Name.split()).lower()
        player2Name = ''.join(player2Name.split()).lower()
        player1 = player.Player()
        player2 = player.Player()
        player1.name = player1Name
        player2.name = player2Name
        #player2 = {'name':player2Name, 'wins':0, 'losses':0, 'ratio':0}
        with open(self.filename, 'r+') as savedata:
            reader = csv.DictReader(savedata)
            linecount = 0
            for user in reader:
                if linecount != 0:
                    if user['Name'] == player1Name:
                        player1.name   = user['Name']
                        player1.wins   = int(user['Wins'])
                        player1.losses = int(user['Losses'])
                        player1.ratio  = float(user['Ratio'])
                    if user['Name'] == player2Name:
                        player2.name   = user['Name']
                        player2.wins   = int(user['Wins'])
                        player2.losses = int(user['Losses'])
                        player2.ratio  = float(user['Ratio'])
                linecount+=1
        return player1, player2

    def writeData(self, player1, player2):
        writeSuccess1 = True
        writeSuccess2 = True
        with open(self.filename, 'a+', newline='') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            reader = csv.DictReader(savedata)
            for player in reader:
                if player['Name'] == player1.name:
                    writer.writerow({'Name':player1.name,    \
                                     'Wins':player1.wins,    \
                                     'Losses':player1.losses,\
                                     'Ratio':player1.ratio})
                    writeSuccess1 = False
                if player['Name'] == player2.name:
                    writer.writerow({'Name':player2.name,    \
                                     'Wins':player2.wins,    \
                                     'Losses':player2.losses,\
                                     'Ratio':player2.ratio})
                    writeSuccess2 = False
            if writeSuccess1:
                writer.writerow({'Name':player1.name,    \
                                 'Wins':player1.wins,    \
                                 'Losses':player1.losses,\
                                 'Ratio':player1.ratio})
            if writeSuccess2:
                writer.writerow({'Name':player2.name,    \
                                 'Wins':player2.wins,    \
                                 'Losses':player2.losses,\
                                 'Ratio':player2.ratio})