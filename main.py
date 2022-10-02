import json
import csv

#   Temp data
class Data:
    def __init__(self):
        self.temp_data = {}
        self.pk_list = {0, }
    
    def update(self, new_data):
        self.temp_data = new_data

#   Functions
def add():
    print('selected add')
    ticket = {
        'number': input('Ticket number "leave it blank for simple tasks": '),
        'description': input('Describe your last task: '),
        'status': input('Status of this task: '),
    }
    
    #   Create dict object and register the key into pk_list
    pk = max(d1.pk_list) + 1
    d1.pk_list.add(pk)
    d1.temp_data[pk] = ticket


def list_():
    print('selected list')
    for key, value in d1.temp_data.items():
        print(f'TASK {key} => {value}')


def remove():
    print('selected remove')
    task = int(input("Enter the number of the task: "))
    print(d1.temp_data[task])
    
    # Check if task in temp_data
    if task not in d1.temp_data:
        print(f'Task {task} => not found!')
        return remove()
    else:
        confirm_ver = ['yes', 'no']
        while True:
            print(f'Task {task} => will be deleted, are you sure? => {d1.temp_data[task]}')
            confirm = input(f'Place "yes" or "no": ')
            if confirm.lower() not in confirm_ver:
                print('Invalid option, try again!')
            else:
                del d1.temp_data[task]
                print(f'Task {task} removed!')
                return False

def edit():
    print('selected edit')


def save():
    print('selected save')
    with open('save.json', 'w') as file:
        json.dump(d1.temp_data, file, indent=4)

def load():
    print('selected load')
    with open('save.json', 'r') as file:
        data = json.load(file)
    d1.update(data)


def export():
    print('selected export')


def exit():
    print('bye')
    return 'exit'

#   Main menu
def main_menu(command):

    options = {
        'add': add,
        'list': list_,
        'edit': edit,
        'remove': remove,
        'save': save,
        'export': export,
        'load': load,
        'exit': exit,
    }

    #   Check commands
    if command in options:
        return options[command]()
    else:
        print(f'Select one of these options: ')
        for i, option in enumerate(options):
            print(f'{i} - {option}')
        
        return

#   Main loop
def main_cli():
    run = True
    while run:
        command = input('\$:> ')
        response = main_menu(command)
        if response == 'exit':
            run = False

if __name__ == '__main__':
    d1 = Data()
    main_cli()
