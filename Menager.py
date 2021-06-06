import os
directory = os.getcwd()
print('ci torviamo in', directory)
inp = input()
if (inp == '/makedir'):
    print('come vuoi chiamare la cartella?')
    r = input()
    str(r)
    try:
        os.mkdir(r)
        print('cartella creata!')
    except:
        print('si è verificato un errore')
elif (inp == '/delete'):
    print('che cosa vuoi eliminare?')
    r = input()
    str(r)
    try:
        os.remove(r)
        print('File eliminato con successo!')
    except:
        print('File non trovato!')
elif (inp == '/rename'):
    r = input('Quale file vuoi rinominare?\n')
    str(r)
    ri = input('e con quale nome lo vuoi cambiare?\n')
    str(ri)
    try:
        os.rename(r, ri)
        print('File rinominato con successo!')
    except:
        print('Si è verificato un errore.... Riprova!')

elif (inp == '/removedir'):
    r = input('Quale cartella vuoi eliminare?\n')
    str(r)
    try:
        os.rmdir(r)
        print('File rinominato con successo!')
    except:
        print('Cartella non trovata')

elif (inp == '/where'):
   print(directory)

elif(inp == '/moveto'):
    r = input('Dove vuoi andare?')
    try:
        os.chdir(r)
    except:
        print('directory non trovata!')

elif (inp == '/what'):
    print(os.listdir())

else:
    print('comando sconosciuto')