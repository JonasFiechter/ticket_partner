#   Temp data
temp_data = {}
pk_list = {0, }

#   Functions
def add():
    print('selected add')
    ticket = {
        'number': input('Ticket number "leave it blank for simple tasks": '),
        'description': input('Describe your last task: '),
        'status': input('Status of this task: '),
    }
    
    #   Create dict object and register the key into pk_list
    pk = max(pk_list) + 1
    pk_list.add(pk)
    temp_data[pk] = ticket

def list_():
    print('selected list')
    for key, value in temp_data.items():
        print(f'TASK {key} => {value}')

def remove():
    print('selected remove')
    task = int(input("Enter the number of the task: "))
    print(temp_data[task])
    
    # Check if task in temp_data
    if task not in temp_data:
        print(f'Task {task} => not found!')
        return remove()
    else:
        confirm_ver = ['yes', 'no']
        while True:
            print(f'Task {task} => will be deleted, are you sure? => {temp_data[task]}')
            confirm = input(f'Place "yes" or "no": ')
            if confirm.lower() not in confirm_ver:
                print('Invalid option, try again!')
            else:
                del temp_data[task]
                print(f'Task {task} removed!')
                return False

def edit():
    print('selected edit')

#   Main menu
def main_menu(command):

    options = {
        'add': add,
        'list': list_,
        'edit': edit,
        'remove': remove,
    }

    #   Check commands
    if command in options:
        options[command]()
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
        main_menu(command)


if __name__ == '__main__':
    main_cli()
