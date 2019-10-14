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
            print("Creating savedata.csv...")
            self.writeTitle()
            print("savedata.csv created!")
        else:
            print("savedata.csv located.")
        

    def writeTitle(self):
        with open(self.filename, 'w+') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writeheader()

    
    def readData(self, player1Name, player2Name):
        player1Name = ''.join(player1Name.split()).lower()
        player2Name = ''.join(player2Name.split()).lower()
        players = [player.Player(), player.Player()]
        playerlist = []
        players[0].name = player1Name
        players[1].name = player2Name
        with open(self.filename, 'r+') as savedata:
            reader = csv.DictReader(savedata)
            for user in reader:
                if user['Name'] == player1Name:
                    players[0].name   = user['Name']
                    players[0].wins   = int(user['Wins'])
                    players[0].losses = int(user['Losses'])
                    players[0].ratio  = float(user['Ratio'])
                elif user['Name'] == player2Name:
                    players[1].name   = user['Name']
                    players[1].wins   = int(user['Wins'])
                    players[1].losses = int(user['Losses'])
                    players[1].ratio  = float(user['Ratio'])
                playerlist.append(player.Player())
                playerlist[self.linecount].name = user['Name']
                playerlist[self.linecount].wins = user['Wins']
                playerlist[self.linecount].losses = user['Losses']
                playerlist[self.linecount].ratio = user['Ratio']
                self.linecount+=1
        return players, playerlist


    def writeData(self, players, playerlist):
        with open(self.filename, 'a+', newline='') as savedata:
            writer = csv.DictWriter(savedata, fieldnames=self.info)
            writer.writerow({'Name':players[0].name,     \
                             'Wins':players[0].wins,     \
                             'Losses':players[0].losses, \
                             'Ratio':players[0].ratio})
            writer.writerow({'Name':players[1].name,     \
                             'Wins':players[1].wins,     \
                             'Losses':players[1].losses, \
                             'Ratio':players[1].ratio})
            for i in range(0,self.linecount):
                if playerlist[i].name != players[0].name or \
                    playerlist[i].name != players[1].name:
                    writer.writerow({'Name':playerlist[i].name,     \
                                    'Wins':playerlist[i].wins,      \
                                    'Losses':playerlist[i].losses,  \
                                    'Ratio':playerlist[i].ratio})