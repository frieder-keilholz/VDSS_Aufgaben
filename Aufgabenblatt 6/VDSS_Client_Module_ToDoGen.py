#!/usr/bin/env python

"""
This file implements the module to generate new ToDo entries.
It generates test data as JSON files and turns dicts in usable documents.
"""

__author__ = 'Frieder Keilholz'
__credits__ = ['Frieder Keilholz']
__version__ = '0.0.8'
__email__ = 'frke4357@th-wildau'
__status__ = 'Finished'

import time
import random
import datetime
import json

from faker import Faker
fake = Faker()

languages = ["Python", "C", "C++", "C#", "Java", "JavaScript", "Perl", "Go", "ABAP", "SQL"]

# by user input
def createToDo(dict):
    #print("Create ToDo-JSON-Document by user-given values")
    entry = {}
    entry["todo"] = dict["todo"]
    entry["text"] = dict["text"]
    entry["until"] = dict["until"]
    entry["user"] = dict["user"]
    entry["sub_tasks"] = dict["sub_tasks"]
    entry["language"] = dict["language"]
    jsonDoc = json.dumps(entry, default=str,indent=4)
    print(jsonDoc)
    return jsonDoc

# generate random ToDo
def generateToDo():
    #print("Generate Random ToDo-JSON-Document")
    entry = {}
    entry["todo"] = fake.sentence()
    entry["text"] = fake.text()
    entry["until"] = fake.future_datetime(end_date='+10y')

    users = []
    for _ in range(random.randint(1,5)):
            users.append(fake.name())
    entry["user"] = users

    sub_tasks = []
    for _ in range(random.randint(0,10)):
        sub_tasks.append({"title":fake.sentence()})
    entry["sub_tasks"] = sub_tasks

    entry["language"] = languages[random.randint(1,len(languages))-1]

    jsonDoc = json.dumps(entry,default=str,indent=4)
    #print(jsonDoc)
    return jsonDoc

start = time.time()
for _ in range(1,1000):
    generateToDo()
elapsed = time.time() - start
print(elapsed)
