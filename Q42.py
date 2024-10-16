#42.take a string from the user and check contains at least one small letter or not?

user = input("string:")

result = False

for each in user:
    if (ord(each) >=97 and ord(each)<=122):
        result = True
        break
print(result)
