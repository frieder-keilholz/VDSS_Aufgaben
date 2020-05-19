"""
ToDo List fot the client program
	
- Make simple Console UI
- Make documents searchable by _id
--	Make documents searcheable by everything
---		Make documents searchable by 2 things at the same time (_id  and user)
---		Make documents serchable by x number of searchterms
--	Add stuff to the revcived document
 >:c


"""
import pymongo
import datetime
from pymongo import MongoClient

import VDSS_Client_Module_ToDoGen as ToDoGen

#is the main method for the ui
def ui_main ():
    ui_clearer()
    print("Hello this is our VDSS client programm user interface \n\n")
    while  ui_main_menu_switcher(ui_input_prompt()):
        print ("Input Wörkt")

#prints the ui Input promt
def ui_input_prompt():
    print("You have the following optins: \nInput: '1' to search for a todo by 'id'\nInput: '2' to search by multiple things\nInput: '3' to create a todo manualy \nInput: '4' to sart benchmarkmode \nInput: 'Exit' to leave")
    first_usr_input = input("\n What do you want to do: \t")
    return first_usr_input

#decides what to do based on the user input
def ui_main_menu_switcher(argument):
    switcher = {
        '1': search_simple,
        '2': search_complex,
        '3': create_todo,
        '4': benchmark_mode,
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
    return switcher.get(argument, ui_wrong_input() )

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

#clears the console
def ui_clearer():

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#searches after an _id
def search_simple():
    ui_clearer()
    print("You have chosen to search a ToDo by its '_id':")
    searched_id = input("_id:")
    result = mycol.find({"_id": searched_id})
    print(result)
    print(mycol.find_one())
    # print (mycol.find({"_id": searched_id}))
    # TODO The if statement should only be called if the search was positive
    if(result):
        if ui_yes_no_switcher(input("Do you want to change or add something to the ToDo item? (default: y)")):
            search_edit()
            return True
    ui_clearer()
    return True

#[TO BE IMPLEMENTED] searches with mutiple parameters
def search_complex():
    ui_clearer()
    print("You have chosen to search a ToDo by multple Arguments:")
    search_id = input("_id:")
    # TODO The if statement should only be called if the search was positive
    if(search_id):
        if ui_yes_no_switcher(input("do you want to change or add something to the ToDo item?")):
            search_edit()
            return True
    ui_clearer()
    return True

#[TO BE IMPLEMENTED] Lets the user edit the searched document _____________________________________________________________________________________________________________________________________________________________________________
def search_edit():

    print("Edits are currently not imlemented yet")

#usergenerated todo
def create_todo():
    print('cratingtodo')
    #ToDoGen.createToDo({"ToDo":"ToDoTitel"})
    
    new_todo={}
    #code for the name
    todo_name = input('Please give your ToDo a name: ')
    #code for the discription
    if(ui_yes_no_switcher(input('do you want to add a discription?'))):
        discription = input("Please enter the discription: ")

    #code for the deadline
    print('Please enter the Deadline: ')
    year = int(input('Please enter a year: '))
    month = int(input('Please enter a month: '))
    day = int(input('Please enter a day: '))
    end_date = datetime.date(year, month, day)
    #code for assigned users
    number_of_assigned_users = int(input("How many users do you want to assign the task: (default: 'y') "))
    assignd_users = []
    while number_of_assigned_users>0:
        assignd_users.append(input('Please enter the Name: '))
        number_of_assigned_users-=1
    #code for subtasks
    subtasks = []
    if (ui_yes_no_switcher(input("Do you want to add subtasks?"))):
        num_of_subtask = int(input("How many subtasks do you want to add?"))
        while num_of_subtask>0:
            subtasks.append(input("Please enter the subtask: "))
    #code for language
    todo_language = input("Please specify the language of the todo: ")
    #code for notes
    if (ui_yes_no_switcher(input("Do you want to add Notes? "))):
        print("note adder pls")
    return True

#starts benchmarkmode   
def benchmark_mode():
    
    print('BENCHMARK MODE ENABLED!!!!\n\n')
    i=int(input('Please enter how many todos you want to generate: '))
    while(i>0):
        mycol.insert_one(ToDoGen.generateToDo())
        i-=1
    return True

#def connection_reader():

print("VDSS clinet programm starting:")
#myclient = MongoClient("mongodb://192.168.2.170:9001,192.168.2.170:9002,192.168.2.170:9003/?replicaSet=rs2")
myclient = MongoClient("mongodb://192.168.2.162:10000/")
mydb = myclient["test"]
mycol = mydb["test"] # should be todo

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)
print (myclient)
ui_main()