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
        self.playerlist = []
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
        players = [player.Player(), player.Player()]
        players[0].name = player1Name
        players[1].name = player2Name

        #player2 = {'name':player2Name, 'wins':0, 'losses':0, 'ratio':0}
        with open(self.filename, 'r+') as savedata:
            reader = csv.DictReader(savedata)
            for user in reader:
                if self.linecount != 0:
                    if user['Name'] == player1Name:
                        players[0].name   = user['Name']
                        players[0].wins   = int(user['Wins'])
                        players[0].losses = int(user['Losses'])
                        players[0].ratio  = float(user['Ratio'])
                        self.linecount-=1
                    elif user['Name'] == player2Name:
                        players[1].name   = user['Name']
                        players[1].wins   = int(user['Wins'])
                        players[1].losses = int(user['Losses'])
                        players[1].ratio  = float(user['Ratio'])
                        self.linecount-=1
                    else:
                        self.playerlist.append(player.Player())
                        self.playerlist[self.linecount-2].name = user['Name']
                        print(self.playerlist[self.linecount-2].name)
                self.linecount+=1
                print(self.playerlist)
        return players

    def writeData(self, players):
        with open(self.filename, 'w', newline='') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writeheader()
            writer.writerow({'Name':players[0].name,     \
                             'Wins':players[0].wins,     \
                             'Losses':players[0].losses, \
                             'Ratio':players[0].ratio})
            writer.writerow({'Name':players[1].name,     \
                             'Wins':players[1].wins,     \
                             'Losses':players[1].losses, \
                             'Ratio':players[1].ratio})
            for i in range(0,self.linecount):
                writer.writerow({'Name':self.playerlist[i].name,     \
                                'Wins':self.playerlist[i].wins,      \
                                'Losses':self.playerlist[i].losses,  \
                                'Ratio':self.playerlist[i].ratio})