import os
import sys
import datetime

def incomplete_command(commands):
   if len(commands) < 2: 
        print(f'{commands[0]}: missing operand')
        return True
   return False

def pwd(commands):
    print(os.getcwd())

def cd(commands):
    if incomplete_command(commands): return
 
    # check if user say for up dir
    if commands[1] == '..': os.chdir(os.getcwd() + '..')
    # check this path is available or not
    try: os.chdir(os.getcwd()+f"\\{commands[1]}")
    except FileNotFoundError: print('No such file or directory')

def exit(commands):
    sys.exit(0)

def ls(commands):
    items = os.listdir(os.getcwd())
    for item in items:
        print(item, end=' ')
    print()

def mkdir(commands):
    if incomplete_command(commands): return
    
    # for every folder that user gives
    folders = commands[1:]
    for folder in folders:
        try: os.mkdir(folder)
        except FileExistsError: print(f'mkdir: cannot create "{folder}": File exists')
       
def rmdir(commands):
    if incomplete_command(commands): return
    
    # for every folder that user gives
    folders = commands[1:]
    for folder in folders:
        try: os.rmdir(folder)
        except OSError:
            print(f'rmdir: failed to remove "{folder}": Directory not empty')
        except FileNotFoundError:
            print(f'rmdir: failed to remove "{folder}": No such file or directory')

def touch(commands):
    if incomplete_command(commands): return
    # for every file that user gives for create
    files = commands[1:]
    for file in files:
        try: 
            with open(file, "w") as f:
                nothing = True
        except FileNotFoundError: print(f'The system cannot find the path specified: "{file}"')

def cat(commands):
    if incomplete_command(commands): return

    # for every file that user gives for read its content
    files = commands[1:]
    for file in files:
        try:
            with open(file, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print(f'cat: "{file}": No sach file or directory')

def remove(files):
    for file in files:
            if os.path.isfile(file):
                os.remove(file)
            elif os.path.isdir(file):
                print(f'rm: cannot remove "{file}": Is a directory')
            else: print(f'rm: "{file}": No sach file or directory')
    return True

# Not completed
def removedir(folders_n_files, isVerbose=False):
    for file in folders_n_files:
         if os.path.isfile(file):
             os.remove(file)
             if isVerbose: print(f'removed file "{file}"')
         elif os.path.isdir(file):
            try: 
                 os.rmdir(file)
                 if isVerbose: print(f'removed directory "{file}"')
            except: 
                os.chdir(os.getcwd()+f'\\{file}')
                list_of_files = os.listdir(os.getcwd())
                if list_of_files != 0: 
                    removedir(list_of_files)
            else: 
                os.chdir('..')
         else: 
             print(f'rm: "{file}": No sach file or directory')

def rm(commands):
    if incomplete_command(commands): return

    options = ['-r', '-rv', '-v']
    if commands[1] in options:
        # With verbose
        if commands[2] in options and commands[2] != commands[1] or commands[1] == '-rv':
            folders_n_files = commands[3:]
            if commands[1] == '-rv': folders_n_files = commands[2:]
            removedir(folders_n_files, isVerbose=True)
        # Without verbose
        else:
            folders_n_files = commands[2:]
            removedir(folders_n_files)
    else:
        files = commands[1:]
        remove(files)
             
def date(commands):
    curr_time = datetime.datetime.now()
    timezone = curr_time.astimezone().tzname()
    print(curr_time.strftime(f"%a %b %d %H:%M:%C {timezone} %Y"))

def cp(commands):
    if len(commands) < 3: print('cp: missing operands')
    source = commands[1]
    destination = commands[2]
    with open(source, 'r') as f:
        content = f.read()
    with open(destination, 'w') as f:
        f.write(content)

def mv(commands):
    if len(commands) < 3: print('mv: missing operands')

    source = commands[1]
    destination = commands[2]
    with open(source, 'r') as f:
        content = f.read()
    with open(destination, 'w') as f:
        f.write(content)
    source = commands[1:2]
    remove(source)

def echo(commands):
    if '>' not in commands:
        txt = commands[1:]
        txt = ' '.join(txt).replace('"', '')
        print(txt)
        return
    
    txt = commands[1:-2]
    txt = ' '.join(txt).replace('"', '')
    
    file = commands[-1]
    with open(file, 'w') as f:
        f.write(txt)    
