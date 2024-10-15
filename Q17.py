first = int(input("enter first number"))
second = int(input("enter second number"))

while 1:
    print("Menu")
    options = "1.add\n2.sub\n3.mul\n4.div\n5.quit"
    opt = int(input(options))

    if opt==1:
        print(first+second)
    elif opt == 2:
        print(first-second)
    elif opt == 3:
        print(first*second)
    elif opt == 4:
        print(first/second)
    elif opt == 5:
        break