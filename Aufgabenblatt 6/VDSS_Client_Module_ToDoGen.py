from faker import Faker
fake = Faker()

import random
import datetime
import json

languages = ["Python", "C", "C++", "C#", "Java", "JavaScript", "Perl", "Go", "ABAP", "SQL"]

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
    
    users = []
    for _ in range(random.randint(1,5)):
            users.append(fake.name())
    entry["user"] = users
    
    sub_tasks = []
    for _ in range(random.randint(0,10)):
        sub_tasks.append({"title":fake.sentence()})
    entry["sub_tasks"] = sub_tasks

    entry["language"] = languages[random.randint(1,len(languages))]

    jsonDoc = json.dumps(entry,default=str,indent=4)
    print(jsonDoc)
    return jsonDoc

generateToDo()