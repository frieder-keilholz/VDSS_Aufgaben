__author__      = "Frieder Keilholz"
__email__       = "frieder.keilholz@th-wildau.de"
__status        = "Prototype"

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

        # generate random user
        entry["user"] = fake.name()
        #print(entry["user"])

        entry["nodes"] = ["node-1", "node-3", "node-5"]

        entries.append(entry)

     
    return entries

def saveJSONs(entries):
    try:
        os.mkdir('entries')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

    for entry in entries:
        file = open(os.path.join('entries', entry["_id"] + ".json"), "w")
        file.write(json.dumps(entry,default=str,indent=4))
        file.close()

print("Generate 10000 random ToDo entries...")
entries = buildEntries(10000)
print("Save generated ToDos to JSON-files...")
saveJSONs(entries)