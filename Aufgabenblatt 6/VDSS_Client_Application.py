#!/usr/bin/env python

"""
This file implements the ToDo List for the client program. Its purpose is to:
    - create a simple console UI
    - make documents searchable by _id
    -- make documents searcheable by everything
    --- make documents searchable by 2 things at the same time (_id  and user)
    ---	make documents searchable by x number of searchterms
    -- make the received document editable
"""

import pymongo
import datetime
import time
import json
import configparser
from pymongo import MongoClient
import configparser
import csv

import VDSS_Client_Module_ToDoGen as ToDoGen

__author__ = 'Maximilian Hartmann, Konstantin Joerss, Julia Reinke'
__credits__ = ['Maximilian Hartmann', 'Konstantin Joerss', 'Julia Reinke']
__version__ = '0.0.26'
__email__ = 'maha2541@th-wildau.de, kojo4103@th-wildau.de, jure5622@th-wildau.de'
__status__ = 'Production'

start_time = 0;
end_time = 0;

csv_path = "logfile.csv"

conf_file = configparser.RawConfigParser()

#is the main method for the ui
def ui_main ():
    ui_clearer()
    # nice asccii art
    print("   _    __    ____    _____   _____           ___             ____                     __                  _____")
    print("  | |  / /   / __ \  / ___/  / ___/          /   |  __  __   / __/   ____ _  ____ _   / /_   ___          / ___/")
    print("  | | / /   / / / /  \__ \   \__ \          / /| | / / / /  / /_    / __ `/ / __ `/  / __ \ / _ \        / __ \ ")
    print("  | |/ /   / /_/ /  ___/ /  ___/ /         / ___ |/ /_/ /  / __/   / /_/ / / /_/ /  / /_/ //  __/       / /_/ / ")
    print("  |___/   /_____/  /____/  /____/         /_/  |_|\__,_/  /_/      \__, /  \__,_/  /_.___/ \___/        \____/  ")
    print("                                                                  /____/                                        ")
    print("")
    print("Hello this is our VDSS client programm user interface \n\n")
    while  ui_main_menu_switcher(ui_input_prompt()):
        print ("Input Wörkt")

#prints the ui Input promt
def ui_input_prompt():
    print("You have the following optins: \nInput: '1' to search for a todo by one category\nInput: '2' to search by multiple categorys\nInput: '3' to create a todo manualy \nInput: '4' to sart benchmarkmode \nInput: 'Exit' to leave")
    first_usr_input = input("\n What do you want to do: \t")
    return first_usr_input
#decides what to do based on the user input
def ui_main_menu_switcher(argument):
    switcher = {
        '1': search_simple,
        '2': search_complex,
        '3': create_todo,
        '4': benchmark_mode,
        '5': ui_yes_no_tester,
        'Exit': ui_exit
    }
    func = switcher.get(argument, lambda: ui_wrong_input() )
    return func()
#converts many yes and no statements into True and False
def ui_yes_no_switcher(argument):
    switcher = {
        'y': True,
        'Y': True,
        'yes': True,
        'Yes': True,
        'j': True,
        'J': True,
        'ja': True,
        'Ja': True,
        'n': False,
        'no': False,
        'N': False,
        'No': False,
        'Nein': False,
        'nein': False
    }
    return switcher.get(argument, lambda: ui_wrong_input() )
def ui_yes_no_tester():
    if (ui_yes_no_switcher(input("Yes no tester"))):
        print("got yes")
    else:
        print('got no')

#user input poromt for the search category
def ui_search_promt():

    print("Please enter the corisponding number of the categroy you want to search with:\n\nEnter '1' to search by ID.\nEnter '2' to search by the title.\nEnter '3' to search by the discription. \nEnter '4' to search by the deadline. (dd-mm-yyyy)\nEnter '5' to search by assigned users.\nEnter '6' to search by language.\n\nYour category choice: ")
#closes the programm
def ui_exit():
    ui_clearer()
    print('ui exit called')
    return False
#is called when a wrong input was detected
def ui_wrong_input():
    ui_clearer()
    print('ERROR: Your input was wrong! Using default! \n\n')
    return True
#lets the user decide what elements gets searched
def ui_element_choice_switcher(argument):
    switcher = {
       '1': '_id',
       '2': 'todo',
       '3': 'text',
       '4': 'until',
       '5': 'users',
       '6': 'language'
       }
    return switcher.get(argument, ui_wrong_input() )
#clears the console
def ui_clearer():

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
#Lets the user select a category to search for and searches for the userinput in the database in that category
def search_simple():
    ui_clearer()
    print("You have chosen to search a ToDo by one category:")
    searched_category = ui_element_choice_switcher(input(ui_search_promt()))
    search_term= input("Please enter your searchterm: ")

    start_time = time.process_time()
    result = mycol.find({searched_category: search_term})
    end_time = time.process_time()
    #csv_writer("search", searched_id, result, (end_time-start_time))
    print("Time for this request: {:5.3f}s".format(end_time-start_time))
    print(result)
    print(mycol.find_one())
    # print (mycol.find({"_id": searched_id}))
    # TODO The if statement should only be called if the search was positive
    if(result):
        if ui_yes_no_switcher(input("Do you want to change or add something to the ToDo item? (default: y)")):
            search_edit(result)
            return True
    ui_clearer()
    return True
#[TO BE IMPLEMENTED] searches with mutiple parameters
def search_complex():
    ui_clearer()
    print("You have chosen to search a ToDo by multple Arguments:")
    search_dictionary = {}
    search_category = ui_element_choice_switcher(input(ui_search_promt()))
    search_dictionary[search_category] = input("Please enter your searchterm: ")
    print("Do you want to add another searchterm?")

    add_search_term = ui_yes_no_switcher(input())
    while (add_search_term):
        search_category = ui_element_choice_switcher(input(uiui_search_promt()))
        search_dictionary[search_category] = input("Please enter your searchterm: ")
        print("Do you want to add another searchterm?")
        add_search_term = ui_yes_no_switcher()

    start_time = time.process_time()
    result = mycol.find(search_dictionary)
    end_time = time.process_time()
    csv_writer("multi_search", "NA", result, (end_time-start_time))
    print("Time for this request: {:5.3f}s".format(endend_time-start_time))
    # TODO The if statement should only be called if the search was positive
    if(search_id):
        if ui_yes_no_switcher(input("do you want to change or add something to the ToDo item?")):
            search_edit()
            return True
    ui_clearer()
    return True
# Lets the user edit the searched document _____________________________________________________________________________________________________________________________________________________________________________
def search_edit(file):
    parsed = json.loads(file)
    json.dumps(parsed, indent=4, sort_keys=True)
    for key in parsed:
        value = parsed[key]
        print("Do you want to change the value of ({}) = ({})?".format(key, value))
        if(ui_yes_no_switcher()):
            print("Please insert the new Value:")
            item[key] == input()
            csv_writer("edit", key, parsed[key], (time.process_time-time.process_time))
    print("Have you done all changes?")
    if(not ui_yes_no_switcher()):
        documentChanger(json.dumps(parsed))
    else:
        return json.dumps(parsed)
#usergenerated todo
def create_todo():
    print('cratingtodo')
    #ToDoGen.createToDo({"ToDo":"ToDoTitel"})

    new_todo={}

    #code for the name
    todo_name = input('Please give your ToDo a name: ')
    #code for the discription
    discription = "---"
    if(ui_yes_no_switcher(input('do you want to add a discription?'))):
        discription = input("Please enter the discription: ")

    #code for the deadline
    end_date = ui_date_input()
    end_date =end_date.strftime("/%d/%m/%Y")
    #code for assigned users
    number_of_assigned_users = int(input("How many users do you want to assign the task: "))
    assignd_users = []
    while number_of_assigned_users>0:
        assignd_users.append(input('Please enter the Name: '))
        number_of_assigned_users-=1
    #code for subtasks
    subtasks = []
    if (ui_yes_no_switcher(input("Do you want to add subtasks?"))):
        num_of_subtask = int(input("How many subtasks do you want to add?"))
        while num_of_subtask>0:
            subtasks.append({"titel": input("Please enter the subtask: ")})
            num_of_subtask-=1
    #code for language
    todo_language = input("Please specify the language of the todo: ")
    #code for notes
    notes= []
    if (ui_yes_no_switcher(input("Do you want to add Notes? "))):
        note_count = int(input('Please enter how many notes you want to add: '))

        while note_count>0:
            note_name = input("Please enter who is responsible: ")
            note_date = ui_date_input()
            note_descr = input("Please enter a discription")
            note_dictionary = { "who" : note_name, "when" : note_date, "what" : note_descr}
            notes.append(note_dictionary)
            note_count=-1

        print("note adder pls")

    new_todo = {"todo": todo_name ,"text": discription , "until": end_date , "user": assignd_users , "sub_tasks": subtasks , "language":todo_language , "notes":notes}
    new_todo_json = ToDoGen.createToDo(new_todo)
    print(new_todo_json)
    mycol.insert_one(new_todo)
    return True
#methode for dateinput
def ui_date_input():
    print('Please enter the Deadline: ')
    year = int(input('Please enter a year: '))
    month = int(input('Please enter a month: '))
    day = int(input('Please enter a day: '))
    end_date = datetime.date(year, month, day)
    
    return end_date
#starts benchmarkmode
def benchmark_mode():

    print('BENCHMARK MODE ENABLED!!!!\n\n')
    i=int(input('Please enter how many todos you want to generate: '))
    while(i>0):
        mycol.insert_one(ToDoGen.generateToDo())
        i-=1
    return True

def connection_reader():
    ip = ""
    port = ""
    conf_file.read('config.txt')
    sections = conf_file.sections()
    print(conf_file.sections()[0])
    #for section in sections:
    #    print(section)
    #    for value in conf_file[section]:
    #        print(value)
    ip = conf_file[conf_file.sections()[0]]["ip"]
    port = conf_file[conf_file.sections()[0]]["port"]
    print(ip + " " + port)
    return ip, port

def csv_writer(type, value, result, duration):
    with open(csv_path, mode='w') as log_file:
        log_writer = csv.writer(log_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        log_writer.writerow([time.process_time, type, value, result, duration])


print("VDSS client programm starting:")
#myclient = MongoClient("mongodb://192.168.2.170:9001,192.168.2.170:9002,192.168.2.170:9003/?replicaSet=rs2")
myclient = MongoClient("mongodb://192.168.178.112:10000/")
mydb = myclient["test"]
mycol = mydb["test"] # should be todo

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)
print (myclient)
ui_main()
