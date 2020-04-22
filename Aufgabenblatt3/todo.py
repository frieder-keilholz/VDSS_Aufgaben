"""
To-Do program following the file of Christopher Grätz
"""

__author__ = "Julia Reinke"
__date__ = "2020-04-20"

import redis
import redisDB
import sys
import datetime
import socket
import random

host = "192.168.2.168"
port = 6379
password = ""

def welcome():
    print("Hallo! Willkommen bei Ihrer ToDo-Liste!\n")
    print(" 1 Aufgabe hinzufügen\n"
          " 2 Aufgabe entfernen\n"
          " 3 To-Do-Liste ansehen\n"
          " 4 To-Do-Liste löschen\n"
          " 5 Beenden\n")

def get_user_input():
    while True:
        try:
            user_input = int(input("Geben Sie bitte eine der oben genannten Zahlen ein um zu starten."))
            if user_input == 1:
                mission = input("Aufgabe hinzufügen: ")
                today = date.today()
                #now added name to ToDo
                name = input("Nutzername: ")
                deadline = input("Deadline: ")
                #now added IP of user to ToDo
                ip = socket.gethostbyname(socket.gethostname())
                insertToDo(mission, today, deadline, name, ip)
            if user_input == 2:
                print("Aufgabe entfernen")
                mission = input("Mission: ")
                deleteMission(mission)
            if user_input == 3:
                print("ToDo-Liste ansehen")
                getToDos()
            if user_input == 4:
                print("ToDo-Liste löschen")
                deleteAll()
            if user_input == 5:
                print("Programm wird beendet...")
                sys.exit()
        except ValueError:
            pass
        except KeyboardInterrupt:
            break
        if user_input is not None and not first <= user_input <= last:
            print("Bitte geben Sie eine Zahl zwischen 1 und 4 ein!")

def insertToDo(mission, today, deadline, name, ip):
    try:
        redisDB.hset(mission, " erstellt am " + str(today), + " von Name: " + name + " IP: " + ip + " erledigt bis " + str(deadline))
    except Exception as e:
        print(e)


def deleteMission(mission):
    try:
        if redisDB.exists(mission):
            redisDB.delete(mission)
        else:
            print("Dieser Eintrag existiert nicht")
    except:
        print("Nicht möglich, da dieser Eintrag nicht existiert.")


def getToDos():
    print('DB-Size: ' + str(redisDB.dbsize()))
    keys = redisDB.keys()
    for key in keys:
        print("ToDo: " + str(key))
        print(redisDB.hgetall(key))
        print()

def deleteAll():
    redisDB.flushall()
    getToDos()

###############################Task Sheet 3###############################

def use_rndm_date():
    """
    Method to create a random date between today and the last day of the year from:
    https://www.w3resource.com/python-exercises/math/python-math-exercise-74.php

    used with a small change
    """
    start_dt = date.today().toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))

def create_a_1001_ToDos():
    i = 0
    for toDo in a_thousand_todos(1001):
        i += 1
        name = str("user" + i)
        mission = str("ToDo" + i)
        deadline = use_rndm_date()
        today = date.today()
        ip = socket.gethostbyname(socket.gethostname())
        insertToDo(mission, today, deadline, name, ip)

if __name__ == '__main__':
    welcome()
    redisDB = redis.Redis(host=host, port=port, db=0, password = password, charset="utf-8", decode_responses=True)
    get_user_input()
