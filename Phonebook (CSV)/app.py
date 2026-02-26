from system import search_number, write_number, show_contacts

print('\n📞 Ph.neB..k -------')

exit_commands = ['q', 'quit', 'exit', 'terminate']
while True:
    command = input('\n-- What do you want Search/Add/Contacts? ')
    if command.lower() in exit_commands:
        break

    if command.lower() == 'search':
        name = input('Search: ')
        results = search_number(name)
        if results:
            print('\nFound results:', results)
        else:
            print('\n* Not Found! *')
    elif command.lower() == 'add':
        name = input('Name: ')
        number = input('Number: ')
        write_number(name, number)
        print('Contact Added in Phonebook.')
    elif command.lower() == 'contacts':
        contacts = show_contacts()
        print('All Contacts:', contacts)
