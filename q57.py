#Take numbers from the user and find out min, maximum, sum, average

a = int(input('a:'))
b = int(input('a:'))

while  True:
    print('menu:')
    options = '1.minimum/n2.maximum/n3.sum/n4.average/nselect option:'
    opt = int(input(options))
    if opt == 1:
        print(min(a, b))
    elif  opt == 2:
        print(max(a, b))
    elif  opt == 3:
        print(a + b)
    elif   opt == 4:
        print((a + b) / 2)