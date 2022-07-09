from pathlib import Path
import Profile
import socket
from ds_client import send

def _filefinder():
    #The main program being run.
    print("Welcome to \'Chatting with Friends\'!")
    print('___________________________')
    print("What would you like to do?:")
    print("1.Create New Profile ('C', INPUT: '-n') \n2.Load Profile ('O') \n3.Read Profile Contents ('R')\n4.Delete Profile ('D')\n5.Quit ('Q')")
    print()
    print("Note: Commands should be inputed as shown: [COMMAND] [INPUT] [[-]OPTION] [INPUT]\n(Ex:‘O [path].dsu’ or 'C [path] [-]n fileName)\n*Unless Specific Input Is Asked For.")
    print()
    command = input()
    while True:
        correct = False
        commands = command.split()
        if len(commands) == 0:
            print('ERROR: NO INPUT: Try Again!')
            command = input()
        elif len(commands) == 1:
            if commands[0] == 'Q':
                return None
            else:
                print('ERROR: Command Not Understood: Try Again!')
                command = input()
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
                                _LoptionR(p)
                            else:
                                if commands[3] == '-s':
                                    file = ''
                                    for i in range(4, len(commands)):
                                        if i != len(commands) - 1:
                                            file += commands[i] + ' '
                                        else:
                                            file += commands[i]
                                    _LoptionRS(p, file)
                                elif commands[3] == '-e':
                                    _LoptionRE(p, commands[4])
                                elif commands[3] == '-f':
                                    _LoptionRF(p)
                                else:
                                    print('ERROR: Command Not Understood: Try Again!')
                        elif commands[2] == '-f':
                            _LoptionF(p)
                        elif commands[2] == '-s':
                            file = ''
                            for i in range(3, len(commands)):
                                if i != len(commands) - 1:
                                    file += commands[i] + ' '
                                else:
                                    file += commands[i]
                            _LoptionS(p, file)
                        elif commands[2] == '-e':
                            _LoptionE(p, commands[3])
                        else:
                            print('ERROR: Command Not Understood: Try Again!')
                else:
                     print('ERROR: Command Not Understood: Try Again!')
                     
            elif command[0] == 'C':
                if len(commands) < 4:
                    print('ERROR: Command Not Understood: Try Again!')
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
                                print('ERROR: File Already Exist. Try Another')
                            else:
                                pass
                        if file_exist == False:
                            print('Create Profile: \n*Note: Once created, DSU Server, Username and Password cannot be changed!\n')
                            dsuserver = input("Enter DSU Server: ")
                            username = input("Enter Username: ")
                            password = input("Enter Password: ")
                            if len(username) == 0 or len(password) == 0 or len(dsuserver) == 0:
                                print('\nERROR: Please Provide Input for Username, Password, or Valid DSU Server')
                            else:
                                nProfile = Profile.Profile(dsuserver, username, password)
                                with open(p2 / new_file, 'w') as p:
                                    p.close()
                                nProfile = Profile.Profile(dsuserver, username, password)
                                nProfile.save_profile(str(p2 / new_file))
                            for item in p2.iterdir():
                                if item.name == new_file:
                                    print('\n',item, ' Profile Created!')
                                else:
                                    pass
                        
                        else:
                            pass
                    else:
                        print('File Path Invalid. Try Again!')
            elif command[0] == 'D':
                if len(commands) < 2:
                    print('ERROR: Command Not Understood: Try Again!')
                elif len(commands) == 2:
                    p3 = Path(commands[1])
                    file_name = p3.name.split('.')
                    if file_name[-1] == 'dsu':
                        p3.unlink(missing_ok=True)
                        print(p3, 'DELETED')
                    else:
                        print('ERROR, No File Found')
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
                        print('ERROR, No File Found')

            elif command[0] == 'R':
                if len(commands) < 2:
                    print('ERROR: Command Not Understood: Try Again!')
                elif len(commands) == 2:
                    p4 = Path(commands[1])
                    file_name = p4.name.split('.')
                    if file_name[-1] == 'dsu':
                        if p4.exists():
                            with open(p4, 'r') as f:
                                file_content = f.read()
                                if p4.stat().st_size == 0:
                                    print('EMPTY\n')
                                else:
                                    print(file_content, end='')
                                    print()
                                f.close()
                        else:
                            print('ERROR: File Does Not Exist! Try Again!')
                    else:
                        print('ERROR: Command Not Understood: Try Again!')
                        
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
                                    print()
                                f.close()
                        else:
                            print('ERROR: Command Not Understood: Try Again!')
                    else:
                        print('ERROR: Command Not Understood: Try Again!')
                else:
                    print('ERROR: Command Not Understood: Try Again!')
                    
            elif command[0] == 'O':
                if len(commands) < 2:
                    print('ERROR: Command Not Understood: Try Again!')
                elif len(commands) == 2:
                    p5 = Path(commands[1])
                    if p5.exists():
                        nProfile = Profile.Profile()
                        nProfile.load_profile(str(p5))
                        print("Profile Loaded!")
                        while True:
                            option = input("Would you like to add a post or change your bio?: \n1 = Add Post\n2 = Change Bio\n3 = Delete Post\n4 = Done\nQ = Quit Program\n")
                            if option == '1':
                                post_entry = input("Write Post:")
                                post = Profile.Post(post_entry)
                                nProfile.add_post(post)
                                nProfile.save_profile(str(p5))
                                send(server=nProfile.dsuserver, port='2021', username=nProfile.username, password=nProfile.password, message=post)
                            elif option == '2':
                                bio_1 = input('Write a bio:')
                                nProfile.bio = bio_1
                                nProfile.save_profile(str(p5))
                                send(server=nProfile.dsuserver, port='2021', username=nProfile.username, password=nProfile.password, message=None, bio=bio_1)
                            elif option == '3':
                                print(nProfile.get_posts())
                                option = input("Which Post would you like to delete?\n(Ex: To Delete First Entry = Enter '0')\n")
                                if nProfile.del_post(int(option)) == True:
                                    print("Post Deleted!")
                                    nProfile.save_profile(str(p5))
                                else:
                                    print("No Post At Indicated Index!")
                            elif option == '4':
                                break
                            elif option == 'Q':
                                return None
                            else:
                                print('ERROR: Command Not Understood: Try Again!')
                        nProfile.save_profile(str(p5))
                    else:
                        print('ERROR: File Path Does Not Exist! Try Again!')
                else:
                    pass
            else:
                print('ERROR: Command Not Understood: Try Again!')
            print('___________________________')
            print("What would you like to do?:")
            print("1.Create New Profile ('C', INPUT: '-n') \n2.Load Profile ('O') \n3.Read Profile Contents ('R')\n4.Quit ('Q')")
            print()
            print("Note: Commands should be inputed as shown: [COMMAND] [INPUT] [[-]OPTION] [INPUT]\n(Unless Specific Input Is Asked For.)")
            print("To add post or bio, Profile must be loaded first!")
    
            command = input()


def _LoptionR(directory):
    #The recursive function for '-r' command.
    for item in directory.iterdir():
        print(item)
        if item.is_dir():
            _LoptionR(item)
        else:
            pass


def _LoptionF(directory):
    #The function used for '-f' command.
    for item in directory.iterdir():
        if item.is_file():
            print(item)
        else:
            pass


def _LoptionS(directory, fileN):
    #The function used for '-s' command.
    for item in directory.iterdir():
        items = item.parts
        if items[-1] == fileN:
            print(item)
        else:
            pass


def _LoptionE(directory, fileN):
    #The fucntion used for '-e' command.
    for item in directory.iterdir():
        types = item.name
        extension = types.split('.')
        if extension[-1] == fileN:
            print(item)


def _LoptionRS(directory, fileN):
    #The function used for '-s' command if '-r' command is used.
    for item in directory.iterdir():
        items = item.parts
        if items[-1] == fileN:
            print(item)
        if item.is_dir():
            _LoptionRS(item, fileN)
        else:
            pass


def _LoptionRE(directory, fileN):
    #The function used for '-e' command if '-r' command is used.
    for item in directory.iterdir():
        types = item.name
        extension = types.split('.')
        if extension[-1] == fileN:
            print(item)
        if item.is_dir():
            _LoptionRE(item, fileN)
        else:
            pass

def _LoptionRF(directory):
    #The function used for '-f' command if '-r' command is used.
    for item in directory.iterdir():
        if item.is_file():
            print(item)
        elif item.is_dir():
            _LoptionRF(item)
        else:
            pass


if __name__ == '__main__':
    _filefinder()

    
