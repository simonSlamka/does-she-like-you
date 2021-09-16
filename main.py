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

askMsg = 1 # declare a bool controlling the while loop
messages = [] # declare a list for messages
sentiments = 0 # declare a variable 'sentiments' and initialize it with a zero

while askMsg == 1:
    message = input("Insert a message:\n")
    msgSentiment = sentanal.polarity_scores(message)["compound"]
    msgSentiment = (msgSentiment+1)/2*100 # this formula converts the compound value of the sentiment in the interval <-1 ... 1> to a percentage
    for word in message.split(" "):
        if word == "break":
            askMsg = 0
            break
    else:
        messages.append(message)
        sentiments += msgSentiment

print (messages)
sentiments = sentiments / len(messages) # divide the sum of all the sentiments by their count
print (sentiments)