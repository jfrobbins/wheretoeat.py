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
                 
        if user[:1] == 'SP':
            self.places = ['thai', 'thai', 'lil tokyo', 'thai', 'thai', 'moose cafe', 'liberty']
        else:
            self.places = ['thai', 'italian', 'lil tokyo', 'indian', 'giannos', 'not firehouse', 'moose cafe', 'liberty']

        if time < datetime(1980,1,1,10, 30, 0, 0).time():
           self.places.append('moose breakfast!')
        
    def getChoice(self):
        eatAt = random.choice(self.places)
        print("\nHow do you feel about " + eatAt + " today?")
        response = input("u mad bro? (Y/n)")
        if response.upper() == "N":
            return eatAt
        else:
            return 0
        
    def whereToEat(self):
        eatHere = self.getChoice()
        while eatHere == 0:
            eatHere = self.getChoice()
            
        print("")
        print("You should *definitely* eat " + eatHere + " today!")
        
if __name__ == '__main__':
    app = foodage(sys.argv[1:])
    app.whereToEat()
