import os
from list_item import ListItem

SAVED_LIST_PATH = './saved_lists'

MAIN_OPTS = 2

welcome_txt = """
Welcome to Shoptimizer! Please select from the following options:
1) Copy saved list.
2) Create new master list.
>"""

input_choice_txt = """
Please select an option between 1 and {MAIN_OPTS}.
>"""

def __retrieve_list_path():
    saved_lists = os.listdir(SAVED_LIST_PATH)
    print("Please type the name of the list you'd like to copy:")
    for i, v in enumerate(saved_lists, start = 1):
        print(f"{i}. {v}")
    choice = input(">")
    while choice not in saved_lists:
        choice = input("Please enter a valid filename.\n>")
    return os.path.join(SAVED_LIST_PATH, choice)

def create_new_master_list():
    pass

def get_saved_list(list_path):
    list = []
    with open(list_path) as list_file:
        for item in list_file:
            list.append(ListItem(item))
    return list


def create_new_list_item():
    pass


def toggle_item_completeness():
    pass


print(welcome_txt)
opt_choice = None
while opt_choice not in range(1,3):
    try: 
        opt_choice = int(input(input_choice_txt))
    except ValueError as e:
        print(input_choice_txt)


if opt_choice == 1: # Copy Saved List
    list_path = __retrieve_list_path()
    list = get_saved_list(list_path)
    choice = int(input(""" What would you like to do?
          1. Add new list item
          2. Mark item complete/uncomplete

          Please enter the number below:
          >"""))
    match choice:
        case 1:
            create_new_list_item(list)
        case 2: 
            toggle_item_completeness()


    
elif opt_choice == 2:   # Create New Master List
    create_new_master_list()



        


