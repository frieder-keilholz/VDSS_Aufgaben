"""
Simple TO_DO_List with redis
Create Tasks with timestamp and to be done date, show tasks (unordered), delete tasks, flush task list
"""
__author__ = "Christopher Grätz"
__date__ = "2020-04-07"

import redis
import sys
from datetime import date

host = "graetznas.myds.me"
port = 6377
password = ""


def print_header():
    print("\033[32m###########################################")
    print("#                 \033[3;32mToDo-Liste              #")
    print("###########################################")
    print("           1 Aufgabe hinzufügen\n"
          "           2 Aufgabe entfernen\n"
          "           3 To-Do-Liste ansehen\n"
          "           4 To-Do-Liste löschen\n"
          "           5 Exit")
    print("##########################################\033[0;30m")


def get_selection(smallest, biggest):
    """
    get the user input from console
    :param smallest: first menu item
    :param biggest: last menu item
    """
    while True:
        try:
            user_input = int(input('\n\033[1;31mWas wollen sie tun?\033[0;30m\n'))
            if user_input == 1:
                task = input("Aufgabe hinzufügen: ")
                today = date.today()
                time = input("Bis wann: ")
                insertToDo(task, today, time)
            if user_input == 2:
                print("Aufgabe entfernen")
                task = input("Task: ")
                deleteTask(task)
            if user_input == 3:
                print("ToDo-Liste ansehen")
                getToDos()
            if user_input == 4:
                print("ToDo-Liste löschen")
                deleteAll()
            if user_input == 5:
                print("Tschüss")
                sys.exit()
        except ValueError:
            pass
        except KeyboardInterrupt:
            break
        if user_input is not None and not smallest <= user_input <= biggest:
            print('Bitte geben Sie eine Zahl '
                  'zwischen {0} und {1} ein!'.format(smallest, biggest))


def insertToDo(task, today, time):
    redisDB.hset(task, "created: " + str(today), "to be done by: " + str(time))
    # redisDB.set(task, str(today), str(time))


def deleteTask(task):
    try:
        if redisDB.exists(task):
            redisDB.delete(task)
        else:
            print("No such entry")
    except:
        print("Not possible - no such entry")


def getToDos():
    print('DB-Size: ' + str(redisDB.dbsize()))
    # print('{:^52} | {:<30}'.format('to', 'Task'))
    # print('{:-<53}|{:-<31}'.format('', ''))
    keys = redisDB.keys()
    for key in keys:
        print("Task: " + str(key))
        # print('{:^10} | {:<30}'.format(str(redisDB.hgetall(key)), key))
        print(redisDB.hgetall(key))
        print()


def deleteAll():
    redisDB.flushall()
    getToDos()


if __name__ == '__main__':
    print_header()
    redisDB = redis.Redis(host=host, port=port, db=0, password=password, charset="utf-8", decode_responses=True)
    get_selection(1, 4)
