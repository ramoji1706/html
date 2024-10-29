#54. Take a two numbers from the user and do below menu driven operations
#1. addition
#2. multiples
#3.division
#4.sqrt
#5. pow    a**b
#6.subtraction
#After selection do the corresponding operation.
#Note: user may give int, or float numbers. You should check whether it is proper digits or not. I.e the user given string should be in the position to convert to float. Other wise show the “inproper string given” Error.
import math

a = int(input('a:'))
b= int(input('b:'))

while True:
    print('menu:')
    options = '1.additon/n2.multiples/n3.division/n4.sqrt/n5.pow/n6.subtraction'
    opt = int(input(options))
    if opt ==  1:
        print(a + b)
    elif  opt == 2:
        print(a * b)
    elif opt  == 3:
        if b != 0:
            print(a / b)
    elif  opt == 4:
        print(math.sqrt(a**b))
    elif  opt == 5:
        print(a ** b)
    elif  opt == 6:
        print(a - b)