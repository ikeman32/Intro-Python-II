import os

def sys_clear():
    if os.uname().sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')