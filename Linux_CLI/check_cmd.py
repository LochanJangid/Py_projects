import run_cmd

def check_command(commands):
    """see command and check which command it is and if available call it."""
    command = commands[0]
    available_commands = ['pwd', 'cd', 'exit', 'ls', 'mkdir', 'rmdir', 'touch', 'cat', 'rm', 'date', 'cp', 'mv', 'echo', 'sort', 'join']

    if command == 'help':
        print('Available commands are:', end=' ')
        for available_command in available_commands[:-1]: 
            print(available_command, end=', ')
        print(available_commands[-1])
    elif command in available_commands:
        try: getattr(run_cmd, command)(commands)
        except AttributeError: print('Command Not Available yet.')
    else:
        print(f'{command}: command not found')
