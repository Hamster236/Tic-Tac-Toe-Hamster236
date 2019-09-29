import tkinter as tk
import os
import time
import csv
import Player as player

class SavedData:
    def __init__(self):
        self.filename = 'savedata.csv'
        self.info = ['Name','Wins','Losses','Ratio']
        self.linecount = 0
        if not os.path.isfile(self.filename):
            self.writeTitle()
        
    def writeTitle(self):
        with open(self.filename, 'w+') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writeheader()
        
    def readData(self, player1Name, player2Name):
        #TODO: Remove the copy/paste of this code
        #FIXME: This code can be converted to a list
        player1Name = ''.join(player1Name.split()).lower()
        player2Name = ''.join(player2Name.split()).lower()
        player1 = player.Player()
        player2 = player.Player()
        player1.name = player1Name
        player2.name = player2Name

        # Saving other players for a new file.
        self.playerlist = []
        #player2 = {'name':player2Name, 'wins':0, 'losses':0, 'ratio':0}
        with open(self.filename, 'r+') as savedata:
            reader = csv.DictReader(savedata)
            for user in reader:
                if self.linecount != 0:
                    if user['Name'] == player1Name:
                        player1.name   = user['Name']
                        player1.wins   = int(user['Wins'])
                        player1.losses = int(user['Losses'])
                        player1.ratio  = float(user['Ratio'])
                        self.linecount-=1
                    elif user['Name'] == player2Name:
                        player2.name   = user['Name']
                        player2.wins   = int(user['Wins'])
                        player2.losses = int(user['Losses'])
                        player2.ratio  = float(user['Ratio'])
                        self.linecount-=1
                    else:
                        self.playerlist.append(player.Player())
                        self.playerlist[self.linecount-2].name = user['Name']
                        print(self.playerlist[self.linecount-2].name)
                self.linecount+=1
                print(self.playerlist)
        return player1, player2

    def writeData(self, player1, player2):
        with open(self.filename, 'w', newline='') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writeheader()
            writer.writerow({'Name':player1.name,     \
                             'Wins':player1.wins,     \
                             'Losses':player1.losses, \
                             'Ratio':player1.ratio})
            writer.writerow({'Name':player2.name,     \
                             'Wins':player2.wins,     \
                             'Losses':player2.losses, \
                             'Ratio':player2.ratio})
            for i in range(0,self.linecount):
                writer.writerow({'Name':self.playerlist[i].name,     \
                                'Wins':self.playerlist[i].wins,      \
                                'Losses':self.playerlist[i].losses,  \
                                'Ratio':self.playerlist[i].ratio})