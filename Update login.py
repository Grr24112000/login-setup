import os 
import sys
import os.path  
from getpass import getpass


class setup:
    #signup function
    def logo():
        print('\033[1;36;49m')
        print(" ────────────────────────────────────────────────────────── ")
        print(" |                                                        | ")
        print(" |   ########    ##  #########  ##       ##      ###      | ")
        print(" |   ##     ##   ##  ##         ##       ##    ##   ##    | ")
        print(" |   ##     ###  ##  ##         ##       ##   ##     ##   | ")
        print(" |   ##     ###  ##  #########  ###########  ##########   | ")
        print(" |   ##     ###  ##         ##  ##       ##  ##      ##   | ")
        print(" |   ##     ##   ##         ##  ##       ##  ##      ##   | ")
        print(" |   ########    ##  #########  ##       ##  ##      ##   | ")
        print(" |                                                        | ")
        print(" \033[1;91m|   || Digital Information Security Helper Assistant ||  | ")
        print(" |                                                        | ")
        print(" ────────────────────────────────────────────────────────── ")
        print(" ────────────────────────────────────────────────────────── ")
        print('\033[1;36;49m')
#This is Login Funtion
    def signup():
        setup.logo()
        file1=open('/data/data/com.termux/files/home/black_angel/name.txt','a+')
        file2=open('/data/data/com.termux/files/home/black_angel/username.txt','a+')
        file3=open('/data/data/com.termux/files/home/black_angel/password.txt','a+')
        name=input('Enter your name : ')
        file1.write(name)
        username=input('Enter your Username : ')
        file2.write(username)
        password=getpass('Enter your Password : ')
        password1=getpass. d('Conforme Your Password : ')
        if(password == password1):
            file3.write(password)
            print('Data Saved Successfully !')
        else :
            setup.signup()
            
     
     
    def login():
        os.system('clear')
        setup.logo()
        file1=open('/data/data/com.termux/files/home/black_angel/name.txt','r')
        file2=open('/data/data/com.termux/files/home/black_angel/username.txt','r')
        file3=open('/data/data/com.termux/files/home/black_angel/password.txt','r')
        name=file1.read()
        usernamel=file2.read()
        passwordl=file3.read()
        username=input('Enter your Username : ')
        password=getpass('Enter your password : ')
        if(username == usernamel and password == passwordl):
            print('Welcome Mr. '+name)
            print('You have Login successfully ')
        else :
            print('wrong entry')
            setup.login()
            
if __name__=="__main__":
    if(os.path.exists('/data/data/com.termux/files/home/black_angel/name.txt' and '/data/data/com.termux/files/home/black_angel/username.txt' and '/data/data/com.termux/files/home/black_angel/password.txt')):
        setup.login()
    else :
        setup.signup()
            




