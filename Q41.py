#41. take a string from the user and check contains at least one capital letter or not?

user = input("string:")

result = False

for each in user:
    if (ord(each) >=65 and ord(each)<=90):
        result = True
        break
print(result)
