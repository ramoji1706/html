#35. Show the below menu to the user until and until user select quit and display corresponding os message

#'''
#Menu:
#1. windows
#2. Linux
#3. Mac
#4. quit

while 1:
    print("menu")
    options = "#Menu:\n1. windows\n2. Linux\n3. Mac\n4.quit"
    opt = int(input(options))

    if (opt == 1):
        print("windows")
    elif (opt == 2):
        print("linux")
    elif (opt == 3):
        print("Mac")
    elif (opt == 4):
        print("quit")
        break        


    