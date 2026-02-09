import os

from check_cmd import check_command

# Welcome display
print('\n-Welcome to Linux CLI')
print('a linux terminal simulator for window users.')
print('\nTo see available commands, type "help" and press enter\n')

main_path = os.getcwd()
# Set Linux Design Terminal
username = input("Username: ")
linux_path = '\033[1;32m'+ f'{username}@Linux-Terminal:~'+'\033[0m'

while True:
    current_path = os.getcwd()
    new_current_path = current_path.replace(main_path, '')
    # Fill colors
    new_current_path = '\033[0;34m' + new_current_path + '\033[0m'
    new_linux_path = linux_path + new_current_path

    command = input(new_linux_path + '$')
    commands = command.split()
    check_command(commands)
    