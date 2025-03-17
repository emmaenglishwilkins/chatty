import re
import sqlite3
from collections import Counter
from string import punctuation 
from math import sqrt

conn = sqlite3.connect('chatty1.db', check_same_thread=False)
c = conn.cursor()

create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(sentence TEXT UNIQUE, used INT NOT NULL DEFAULT 0)',
    'CREATE TABLE associations (word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)'
]

for req in create_table_request_list: 
    try: 
        c.execute(req)
    except: 
        pass

