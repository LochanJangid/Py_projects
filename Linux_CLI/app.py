import os

from check_cmd import check_command

# Welcome display
print('\n-Welcome to Linux CLI')
print('a linux terminal simulator for window users.')
print('\nTo see available commands, type "help" and press enter\n')

main_path = os.getcwd()
# Set Linux Design Terminal
username = input("Username: ")
linux_path = f'{username}@Linux-Terminal:~'

while True:
    current_path = os.getcwd()
    new_linux_path = current_path.replace(main_path, linux_path)

    command = input(new_linux_path + '$')
    commands = command.split()
    check_command(commands)
    