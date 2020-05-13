from faker import Faker
fake = Faker()

import random
import datetime
import json

# by user input
def createToDo(dict):
    print("Create ToDo-JSON-Document by user-given values")

# generate random ToDo
def generateToDo():
    print("Generate Random ToDo-JSON-Document")
    entry = {}
    entry["todo"] = fake.sentence()
    entry["text"] = fake.text()
    entry["until"] = fake.future_datetime(end_date='+10y')
    entry["user"] = user
    return json.dumps(entry,default=str,indent=4)
    