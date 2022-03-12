"""
A little program for evaluating a girl's responses using the NLTK SIA.
"""

#!/usr/bin/python3

# Written by Simon Slamka in pursuit of a successful online communication with a girl.
# I could never really talk to people and read them, recognize their intent and emotions.
# That's the reason I made this.
# Of course, all this is for entertainment purposes only.
# The model is not so precise and can't be trusted with life.

# Put in more messages to potentially increase precision.

from __future__ import division
from nltk.sentiment import SentimentIntensityAnalyzer

sentanal = SentimentIntensityAnalyzer()  # initialize the SIA

ASK_MSG = 1  # declare a bool controlling the while loop
messages = []  # declare a list for messages
SENTIMENTS = 0  # declare a variable 'sentiments' and initialize it with a zero

while ASK_MSG == 1:
    message = input("Insert a message:\n")
    MSG_SENTIMENT = sentanal.polarity_scores(message)["compound"]
    # this formula converts the compound value of the sentiment
    # in the interval <-1 ... 1> to a percentage
    MSG_SENTIMENT = (MSG_SENTIMENT + 1) / 2 * 100
    for word in message.split(" "):
        if word == "break":
            ASK_MSG = 0
            break
    else:
        messages.append(message)
        SENTIMENTS += MSG_SENTIMENT

print("")
print("'break' keyword detected, terminating loop ...")
print("-------------------------------")
print("")
print("")
# divide the sum of all the sentiments by their float(count)
SENTIMENTS = SENTIMENTS / float(len(messages))
print("Total sentiment of her messages: ", SENTIMENTS)
if SENTIMENTS > 80:
    print("She probably likes you!")
elif SENTIMENTS > 65 < 80:
    print("Her messages are positive, but with no stronger feelings to them.")
elif SENTIMENTS > 50 < 65:
    print("Her responses are very neutral. Isn't she just your friend?")
else:
    print(
        "This is not good ... she either doesn't care much or just can't talk properly."
    )
    print(
        "Don't give it too much thought though, happens to all of us ..."
    )
