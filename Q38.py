#38.take a string from the user and check contains at least one digit or not?

s = "abc1cd"

result = False
for each in s:
    if each in "0123456789":
        result = True
        break
print(result)        