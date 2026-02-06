import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


def main_menu():
#ask for an input/ Created "menu" view
    selection = input('''
Main Menu (select a number):
[1] Contacts
[2] Browser
[3] Tasks               
                       ''')
#logic to detect which feature should be accessed
    if selection == '1':
        return "Contacts Function Place Holder"
    elif selection == '2':
        return "Browser Function Place Holder"
    elif selection == '3':
        return "Tasks Function Place Holder"
    else:
        return f"Invalid Selection - Please Try Again {main_menu()}"
        

print(main_menu())