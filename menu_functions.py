import manageTask, contacts, internet_search


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
        return contacts.new_contact()
    
    elif selection == '2':
        return internet_search.internet_search()
    
    elif selection == '3':
        return manageTask.main()
    else:
        return f"Invalid Selection - Please Try Again {main_menu()}"
        

print(main_menu())