#   Temp data
temp_data = {}

#   Functions
def add():
    print('selected add')
    ticket = {
        'number': input('Ticket number "leave it blank for simple tasks": '),
        'description': input('Describe your last task: '),
        'status': input('Status of this task: '),
    }
    
    #   Check if number exists, if not place an automatic one
    
    temp_data[ticket[str(len())]] = ticket

def list_():
    print('selected list')
    for key, value in temp_data.items():
        print(f'TASK => {value}')

def remove():
    print('selected remove')

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