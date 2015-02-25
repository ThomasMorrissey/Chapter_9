#! bin/usr/python3
# Program Name: Challenge_2.py
# Author: Thomas Morrissey
# Date Written: 2-24-2015
# Luke Gosnell Help Spell Check.
import random
Ranks = ["A" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
Suit = ["Diamonds","Hearts","Clubs","Spades"]
Player1Counter=0
Player2Counter=0
print("Welcome to WAR!")
print("You and a friend will play war until one of the two of you gains ten points.")
print("Before we begin, please enter your names.")
Player1Name=input("Player One: ")
Player2Name=input("Player Two: ")
while Player1Counter < 10 and Player2Counter < 10:
    Player1CardIndex=random.randrange(len(Ranks))
    Player2CardIndex=random.randrange(len(Ranks))
    Player1Card=Ranks[Player1CardIndex]
    Player2Card=Ranks[Player2CardIndex]
    if Player1CardIndex > 9:
        Player1CardIndex = 10
    else:
        Player1CardIndex = Player1CardIndex + 1
    if Player2CardIndex > 9:
        Player2CardIndex = 10
    else:
        Player2CardIndex = Player2CardIndex + 1
    Player1SuitIndex=random.randrange(len(Suit))
    Player1Suit=Suit[Player1SuitIndex]
    Player2SuitIndex=random.randrange(len(Suit))
    Player2Suit=Suit[Player2SuitIndex]
    print(Player1Name,"has a",Player1Card,"of",Player1Suit+".")
    print(Player2Name,"has a",Player2Card,"of",Player2Suit+".")
    if Player1CardIndex > Player2CardIndex:
        print(Player1Name,"Wins and Gains One Point!")
        Player1Counter = Player1Counter + 1
    elif Player2CardIndex > Player1CardIndex:
        print(Player2Name,"Wins and Gains One Point!")
        Player2Counter=Player2Counter+1
    else:
        print("It's a Draw and No One wins! =(")
    print("Total Scores Are:")
    print(Player1Name+":",Player1Counter)
    print(Player2Name+":",Player2Counter)
    input("Please press the <Enter> key to start a new round.")
if Player1Counter == 10:
    print(Player1Name,"has and has provined to be the ultimate champion!")
else:
    print(Player2Name,"has and has provined to be the ultimate champion!")
print("Thank you for playing!")
input("Please press the <Enter> key to exit.")

