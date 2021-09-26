
import os
import time

def options():   # show all opetions 

    while True:
        try:
            userChoice1 = int(input('1) Display All Files \n2) Create New File \n3) Delete File\n4) Read File \n5) Write File\n6) Set Password \n7) Exit \n\nS1 > '))
        except:
            print('\n[!] Invaild input !\n[ Hint1 : Enter integer value ]\n[ Hint2 : Choose the option according to your stage ]\n')
        else:
            conditions(userChoice1)   # check condition 

def afterExe():

    print('\n_______________________________________________________________________________________\n')
    print('[Secondary] Stage  : Choose from given options : [99-7]  \n')

    while True:
        try:
            userChoice1 = int(input('99) Main Menu \n7) Exit\n\nS2 >> '))  # Main menu \ Exit 
        except:
            print('\n[!] Invaild input !\n[ Hint1 : Enter integer value ]\n[ Hint2 : Choose from given options : [99-7] ]\n\n\n\n\n')  # if input != int
        else:
            if userChoice1==99:  
                print('\n_______________________________________________________________________________________\n')
                print('\n[Primary] Stage : Choose from given options : [1-2-3-4-5-6-7-99] \n\n')

                options()  # show all options
            elif userChoice1==7:
                conditions(userChoice1)     # terminate 
            else:
                print('\n[!] invaild input !\n[ Hint : Choose 99 or 7 ]\n ')   # if input == int but not not from given options

def conditions(userChoice1):   # check user's choice !
    
    if userChoice1 == 1:
        showFiles()
        print()
        afterExe()

    elif userChoice1 == 2:
        user_file_name = input('\n[+] Enter Your File Name : ')
        file_extension = input('[+] File Extension ( without dot [.] ) : ')
        file_name = user_file_name + '.'+file_extension
        createFile(file_name)
        afterExe()

    elif userChoice1 == 3:
        file_name = input('\n[+] File Name ( with extension ) : ')
        deleteFile(file_name)
        afterExe()
        pass

    elif userChoice1 == 4:
        file_name = input('\n[+] File Name : ')
        reading(file_name)
        afterExe()

    elif userChoice1 == 5:
        file_name = input('\n[+] Enter Your File Name : ')
        write(file_name)
        afterExe()

    elif userChoice1 == 6:
        print('\n[#] Available Soon')
        afterExe()
        pass

    elif userChoice1 ==7:

        print('\n[ツ] I will look forward to seeing you again soon !\n\n')
        time.sleep(1)
        exit()

    elif userChoice1 == 99:
        options()

    else:
        print('\n[!] Invaild Input !\n')


def showFiles():   #  display all files 
    print(f'\n-------------------- File Names --------------------\n')
    Files = os.listdir()
    for file in Files:
        print(file , end = '   ')

def write(file_name):  # writing file
    
    if file_name in os.listdir():
        with open(file_name,'a') as wf:
            information = input('\n\n[+] Write a statement... \n>> ')
            wf.write( information + '\n' )
        print('\n[!] File updating...')
        time.sleep(1)
        print(f'\n[+] {file_name} updated successfully.')

    else:
        print('\n[-] File does not exist...')
        ans = input('\n[+] If you want to create a new file Enter "y" | if not then press "n" : ')
        if ans.lower()=='y':
            exe = input(f'[.] Enter extesion for {file_name} file ( without dot ): ')
            file_name = file_name+'.'+exe
            print(f'--- Creating a new file : {file_name} ')
            time.sleep(1)
            with open(file_name,'a') as wf:
                information = input('\n\n[+] Write a statement... \n>> ')
                wf.write('\n' + information)
            print('\n[..] Up and Running...')
            time.sleep(1)
            print(f'\n[+] {file_name} Added.')

def reading(File_name):  # reading file
    if File_name in os.listdir():
        with open(File_name,'r') as rf:
            print(f'\n-------------------- {File_name} Data --------------------\n\n{rf.read()}')
    else:
        print('\n[-] File does Not exists !')

def createFile(file_name):  # creating file 

    if file_name in os.listdir():
        print(f'\n[!] {file_name} is already exists !')
        ans = input('\n[+] if you want to create file name with other name press "y" or if not then press "n" : ')
        if ans.lower()=='y':
            time.sleep(1)
            user_file_name = input('\n[+] Enter File Name : ')
            file_extension = input('\n[+] File Extension( without dot [.] ) : ')
            file_name = user_file_name + '.'+ file_extension
            createFile(file_name)
            time.sleep(1)
            # print('\nFile Created successfully !')
        else:
            pass

    else:
        with open(file_name,'w') as nF:
            pass
        time.sleep(1)
        print('\n[+] File created Sucessfully !')

def deleteFile(file_name):  # delete file 
    if file_name in os.listdir():
        os.remove(os.getcwd() + '/' + file_name)
        if file_name not in os.listdir():
            print(f'\n[!] Removing {file_name}')
            time.sleep(1)
            print('\n[+] File deleted Successfully !')
        else:
            print('\n[!] someting went wrong !')
    else:
        print('\n[-] File does not exist !')

def passWord():  # set password (after creating !)
    pass


if __name__=='__main__':
    
    time.sleep(0.5)
    print('\n\n          ...   𝑊  𝑒 𝑙 𝑐 𝑜 𝑚  𝑒  𝑡 𝑜   𝐹 𝐻 - 𝑃 𝑟 𝑜 𝑗 𝑒 𝑐 𝑡   ...    ')
    time.sleep(1)

    print('''
    
     _____   _   _      ____                     _                 _   
    |  ___| | | | |    |  _ \   _ __    ___     (_)   ___    ___  | |_ 
    | |_    | |_| |    | |_) | | '__|  / _ \    | |  / _ \  / __| | __|
    |  _|   |  _  |    |  __/  | |    | (_) |   | | |  __/ | (__  | |_ 
    |_|     |_| |_|    |_|     |_|     \___/   _/ |  \___|  \___|  \__|
                                              |__/                       By Yash Jivani
    
    ''')
    print('[Primary] Stage : Choose from given options : [1-2-3-4-5-6-7] \n')
    try:
        userChoice1 = int(input('1) Display All Files \n2) Create New File \n3) Delete File\n4) Read File \n5) Write File\n6) Set Password\t  ( Available soon )\n7) Exit\n\nS1 > '))
    except:
        print('[!] Invaild input !')
        print('[ Hint1 : Enter integer value ]\n[ Hint2 : Choose from given options! ]')
    else: 
        conditions(userChoice1)
    