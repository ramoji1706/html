#40.take a string from the user and check contains at least one chars or not?

user = input("string:")

result = False

for each in user:
    if (ord(each) >=65 and ord(each)<=90) or (ord(each) >=97 and ord(each)<=122) or (each in "0123456789"):
        result = True
        break
print(result)
