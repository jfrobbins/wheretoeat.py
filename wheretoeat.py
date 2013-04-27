#!/usr/bin/env python3

#from tkinter import *
import sys
import random
#import os
import getpass
from datetime import datetime

class foodage:
    def __init__(self, args):
        user = getpass.getuser().upper()
        time =datetime.time(datetime.now())

        #this is a dictionary (lookuptable/map)
        #   { key : value, ... }
        #   the keys can be any type (string, numeric)
        #   the values can be lists, or single values
        #       {1: ['blah', 'blah2'] }
        #       { 'italian' : ['liltaliano', 'olive garden', 'carrabas'] }
        genres = { 1: 'italian', 2: 'japanese' }
        

        #build a list of places:
        #standard places:
        self.places = ['thai', 'lil tokyo', 'moose cafe', 'liberty', 'indian', 'giannos']
        if user[:1] == 'SP':
            # moar thai
            self.places += ['thai'] * 3
        else:
            #add non-scott options:
            self.places += ['firehouse']

        if time < datetime(1980,1,1,10, 30, 0, 0).time():
           self.places.append('moose breakfast!')
        
    def getChoice(self):
        #return a random choice:
        eatAt = random.choice(self.places)
        print("\nHow do you feel about " + eatAt + " today?")
        response = input("u mad bro? (Y/n)")
        if response.upper() == "N":
            return eatAt
        else:
            return 0
        
    def whereToEat(self):
        #loop through based on user responses (return value of the method)
        eatHere = self.getChoice()
        while eatHere == 0:
            eatHere = self.getChoice()
            
        print("")
        print("You should *definitely* eat " + eatHere + " today!\n")
        
if __name__ == '__main__':
    #main program execution starts here:
    app = foodage(sys.argv[1:])
    #execute class method:
    app.whereToEat()
