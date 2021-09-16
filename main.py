#!/usr/bin/python3

# Written by Simon Slamka in pursuit of a successful online communication with a girl.
# I could never really talk to people and read them, recognize their intent and emotions. That's the reason I made this.
# Of course, all this is for entertainment purposes only. The model is not so precise and can't be trusted with life.

from email import message
import json
from json import loads
from json import dumps
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sentanal = SentimentIntensityAnalyzer() # initialize the SIA

askMsg = 1
messages = [] # declare a list for a girl's messages

while askMsg == 1:
    message = input("Insert a girl's message:\n")
    for word in message.split(" "):
        if word == "break":
            askMsg = 0
            break
    else:
        messages.append(message)

print (messages)