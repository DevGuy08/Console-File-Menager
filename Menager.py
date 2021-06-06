import os
directory = os.getcwd()
print('''we're currently  in''', directory)
while True:
    inp = input()
    if (inp == '/makedir'):
        print('how do you wanna name the folder?\n')
        r = input()
        str(r)
        try:
            os.mkdir(r)
            print('folder created!')
        except:
            print('an error occurred')
    elif (inp == '/delete'):
        print('which file do you wanna delete?\n')
        r = input()
        str(r)
        try:
            os.remove(r)
            print('file eliminated successfully!')
        except:
            print('impossible find the file!')
    elif (inp == '/rename'):
        r = input('which file do you wanna delete?\n')
        str(r)
        ri = input('and what name do you want to change it to?\n')
        str(ri)
        try:
            os.rename(r, ri)
            print('file renamed successfully!')
        except:
            print('an error occurred')

    elif (inp == '/removedir'):
        r = input('which file do you wanna delete?\n')
        str(r)
        try:
            os.rmdir(r)
            print('folder eliminated successfully!')
        except:
            print('impossible find the folder')

    elif (inp == '/where'):
       print(directory)

    elif(inp == '/moveto'):
        r = input('Where do you want to go?\n')
        try:
            os.chdir(r)
        except:
            print('directory inexistent')

    elif (inp == '/what'):
        print(os.listdir())

    else:
        print('unknow command')
