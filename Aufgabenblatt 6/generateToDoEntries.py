__author__      = "Frieder Keilholz"
__email__       = "frieder.keilholz@th-wildau.de"
__status__      = "Prototype"
__version__     = 2    

# # # # # # # # # # # # # # # # #
# Faker Package vorrausgesetzt  #
# pip3 install Faker            #
# # # # # # # # # # # # # # # # #
from faker import Faker

import random
import datetime

import json
import os
import errno

fake = Faker()

def buildEntries(numOfeEtries):
    entries = []
    initSeed = int(random.randint(1,9999999))
    for _ in range(numOfeEtries):
        entriesPerUser = []

        # generate random user
        user = fake.name()

        for _ in range(random.randint(1,10)):
            entry = {}

            # generate unique random ID
            random.seed(initSeed)
            initSeed+=1
            entry["_id"] = str(hex(random.getrandbits(96))).split('0x')[1]
            #print(entry["_id"])

            # generate random todo
            entry["todo"] = fake.sentence()
            #print(entry["todo"])

            # generate random text
            entry["text"] = fake.text()
            #print(entry["text"])

            # generate random deadline
            entry["until"] = fake.future_datetime(end_date='+10y')
            #print(entry["until"])

            # set username
            entry["user"] = user
            #print(entry["user"])

            # set nodes
            entry["nodes"] = ["node-1", "node-3", "node-5"]
            
            entriesPerUser.append(entry)
        entries.append(entriesPerUser)
     
    return entries

def saveJSONs(entries):
    try:
        os.mkdir('entries')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    for entry in entries:
        file = open(os.path.join('entries', entry[0]["_id"] + ".json"), "w")
        file.write(json.dumps(entry,default=str,indent=4))
        file.close()

print("Generate 1000 random ToDo-User entries...")
now = datetime.datetime.now()
entries = buildEntries(100000)
print("Save generated ToDos to JSON-files...")
print(datetime.datetime.now() - now)
saveJSONs(entries)

""" 
Timetesting on 9700k @5.1ghz
times
100k: 0:05:02.440824
10k:  0:00:30.522318
"""
""" 
Timetesting on 3600X @UbuntuVM
times
100k: 0:05:07.994340
10k:  0:00:30.694395
"""
