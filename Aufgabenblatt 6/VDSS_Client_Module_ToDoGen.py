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
    for _ in range(random.randint(1,5)):
        entry["user"] = fake.name()
    return json.dumps(entry,default=str,indent=4)
    