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
        if os.path.isdir(item): item = '\033[0;34m' + item + '\033[0m'
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

def remover(path, isVerbo=False):
    if os.path.isfile(path):
        os.remove(path)
        if isVerbo: print(f'removed "{path}"')
        return
    
    if os.path.isdir(path):
        for name in os.listdir(path):
            child = os.path.join(path, name)
            if isVerbo: remover(child, isVerbo=True)
            else: remover(child)
        os.rmdir(path)
        if isVerbo: print(f'removed directory "{path}"')
        return
    
    # if the path dosen't exist
    raise FileNotFoundError(f'rm -r: failed to remove "{path}": No such file or Directory')

def rm(commands):
    if incomplete_command(commands): return
    options = ['-r', '-v', '-rv']
    # when we not have 2 options
    if commands[2] not in options:
        files = commands[2:] # for -r and -v
        # when we have not options
        if commands[1] not in options:
            files = commands[1:]
            for file in files:
                if os.path.isfile(file):
                    remover(file)
                else: print(f'rm: cannot remove "{file}": Is a directory')
            return
        # when we have one option
        # when -r
        if commands[1] == '-r':
            for file in files:
                remover(file)
            return
        # when -v
        if commands[1] == '-v':
            for file in files:
                if os.path.isfile(file):
                    remover(file, isVerbo=True)
                else: print(f'rm: cannot remove "{file}": Is a directory')
            return
    # when -rv or -r -v
    if commands[1] == '-rv':
        files = commands[2:]
    else:
        files = commands[3:]

    for file in files:
        remover(file, isVerbo=True)
    return
             
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

def sort(commands):
    if len(commands) != 2:
        print('Usuage: [sort file_name]')
        return

    with open(commands[1]) as f:
        lines = f.readlines()
        lines.sort()
        for line in lines:
            print(line.replace('\n',''))

def join(commands):
    if len(commands) < 3:
        print('Usuage: [sort file_1 file_2] > new_file.txt')
        return
     
    



    with open(commands[1]) as f:
        lines1 = f.readlines()
    with open(commands[2]) as f:
        lines2 = f.readlines()
    
    len1 = len(lines1)
    len2 = len(lines2)
    min_len = min(len1, len2)
    
    new_lines = ''

    for i in range(min_len):
        new_lines += f'{lines1[i].replace('\n', '')} {lines2[i].replace('\n', '')}\n'

    # if user want to make new file by using > new_file.txt
    if len(commands) > 3 and commands[3] == '>': 
        with open(commands[4], 'w') as f:
            f.write(new_lines)
    # if user just want to print
    else: print(new_lines)
    