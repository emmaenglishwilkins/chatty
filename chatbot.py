import sqlite3, csv
import re
import random
from textblob import TextBlob, Word

conn = sqlite3.connect('chatty1.db', check_same_thread=False)
c = conn.cursor()

'''
#everything else 

'''

def chatbot_response(state, userInput):
    flag = True
    while flag:
        sentence = userinput
        if sentence == "":
            return ("bye!")
            flag = False
        else: 
            return("ur mom")
        '''
        elif check_for_greeting(sentence):
            return check_for_greeting(sentence)
        elif check_for_topic(sentence) is not None:
            return check_for_topic(sentence)
        elif check_for_reflection(sentence):
            return check_for_reflection(sentence)
        elif check_for_facts(sentence):
            return check_for_facts(sentence)
        else:
            return "Sorry I don't know what you are saying."
        '''
if __name__ == '__main__':
	main()
