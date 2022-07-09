def filefinder():
    #The main program being run.
    command = input()
    while True:
        correct = False
        commands = command.split()
        if len(commands) == 1:
            if commands[0] == 'Q':
                return None
            else:
                print('ERROR')
        elif len(commands) >= 2:
            while correct == False:
                if len(commands) == 2:
                    correct = True
                else:
                    if commands[2] not in ('-r', '-f', '-s', '-e', '-n'):
                        commands[1] = commands[1] + ' ' + commands[2]
                        commands.pop(2)
                    else:
                        correct = True
                    
            if commands[0] == 'Q':
                return None
            elif commands[0] == 'L':
                p = Path(commands[1])
                if p.exists():
                    if len(commands) == 2:
                        direct = []
                        for item in p.iterdir():
                            if item.is_dir():
                                direct.append(item)
                            else:
                                print(item)
                        for item in direct:
                            print(item)
                    if len(commands) > 2:
                        if commands[2] == '-r':
                            if len(commands) == 3:
                                LoptionR(p)
                            else:
                                if commands[3] == '-s':
                                    file = ''
                                    for i in range(4, len(commands)):
                                        if i != len(commands) - 1:
                                            file += commands[i] + ' '
                                        else:
                                            file += commands[i]
                                    LoptionRS(p, file)
                                elif commands[3] == '-e':
                                    LoptionRE(p, commands[4])
                                elif commands[3] == '-f':
                                    LoptionRF(p)
                                else:
                                    print('ERROR')
                        elif commands[2] == '-f':
                            LoptionF(p)
                        elif commands[2] == '-s':
                            file = ''
                            for i in range(3, len(commands)):
                                if i != len(commands) - 1:
                                    file += commands[i] + ' '
                                else:
                                    file += commands[i]
                            LoptionS(p, file)
                        elif commands[2] == '-e':
                            LoptionE(p, commands[3])
                        else:
                            print('ERROR')
                else:
                     print('ERROR')
            elif command[0] == 'C':
                if len(commands) < 4:
                    print('ERROR')
                else:
                    file = ''
                    for i in range(3, len(commands)):
                        if i != len(commands) - 1:
                            file += commands[i] + ' '
                        else:
                            file += commands[i]
                    p2 = Path(commands[1])
                    new_file = file + '.dsu'
                    file_exist = False
                    if p2.exists():
                        for item in p2.iterdir():
                            if item.name == new_file:
                                file_exist = True
                                print('ERROR')
                            else:
                                pass
                        if file_exist == False:   
                            with open(p2 / new_file, 'w') as p:
                                p.close()
                            for item in p2.iterdir():
                                if item.name == new_file:
                                    print(item)
                                else:
                                    pass
                        else:
                            pass
                    else:
                        pass
            elif command[0] == 'D':
                if len(commands) < 2:
                    print('ERROR')
                elif len(commands) == 2:
                    p3 = Path(commands[1])
                    file_name = p3.name.split('.')
                    if file_name[-1] == 'dsu':
                        p3.unlink(missing_ok=True)
                        print(p3, 'DELETED')
                    else:
                        print('ERROR')
                else:
                    file = commands[1]
                    for i in range(2, len(commands)):
                        file += ' ' + commands[i]
                    p3 = Path(file)
                    file_name = p3.name.split('.')
                    if file.name[-1] == 'dsu':
                        p3.unlink(missing_ok=True)
                        print(p3, 'DELETED')
                    else:
                        print('ERROR')
                            
            elif command[0] == 'R':
                if len(commands) < 2:
                    print('ERROR')
                elif len(commands) == 2:
                    p4 = Path(commands[1])
                    file_name = p4.name.split('.')
                    if file_name[-1] == 'dsu':
                        if p4.exists():
                            with open(p4, 'r') as f:
                                file_content = f.read()
                                if p4.stat().st_size == 0:
                                    print('EMPTY')
                                else:
                                    print(file_content, end='')
                                f.close()
                        else:
                            print('ERROR')
                    else:
                        print('ERROR')
                        
                elif len(commands) > 2:
                    file = commands[1]
                    for i in range(2, len(commands)):
                        file += ' ' + commands[i]
                    p4 = Path(file)
                    file_name = p4.name.split('.')
                    if file_name[-1] == 'dsu':
                        if p4.exists():
                            with open(p4, 'r') as f:
                                file_content = f.read()
                                if p4.stat().st_size == 0:
                                    print('EMPTY')
                                else:
                                    print(file_content, end='')
                                f.close()
                        else:
                            print('ERROR')
                    else:
                        print('ERROR')
                else:
                    print('ERROR')
            else:
                print('ERROR')
                  
        command = input()


def LoptionR(directory):
    #The recursive function for '-r' command.
    for item in directory.iterdir():
        print(item)
        if item.is_dir():
            LoptionR(item)
        else:
            pass


def LoptionF(directory):
    #The function used for '-f' command.
    for item in directory.iterdir():
        if item.is_file():
            print(item)
        else:
            pass


def LoptionS(directory, fileN):
    #The function used for '-s' command.
    for item in directory.iterdir():
        items = item.parts
        if items[-1] == fileN:
            print(item)
        else:
            pass


def LoptionE(directory, fileN):
    #The fucntion used for '-e' command.
    for item in directory.iterdir():
        types = item.name
        extension = types.split('.')
        if extension[-1] == fileN:
            print(item)


def LoptionRS(directory, fileN):
    #The function used for '-s' command if '-r' command is used.
    for item in directory.iterdir():
        items = item.parts
        if items[-1] == fileN:
            print(item)
        if item.is_dir():
            LoptionRS(item, fileN)
        else:
            pass


def LoptionRE(directory, fileN):
    #The function used for '-e' command if '-r' command is used.
    for item in directory.iterdir():
        types = item.name
        extension = types.split('.')
        if extension[-1] == fileN:
            print(item)
        if item.is_dir():
            LoptionRE(item, fileN)
        else:
            pass

def LoptionRF(directory):
    #The function used for '-f' command if '-r' command is used.
    for item in directory.iterdir():
        if item.is_file():
            print(item)
        elif item.is_dir():
            LoptionRF(item)
        else:
            pass

        
if __name__ == '__main__':
    from pathlib import Path
    filefinder()

        
