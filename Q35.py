#35 Convert the total string in to lower case. Without using lower() function.

s = input()


new = ""
for each in s:
    lowerChar = chr((ord(each)+32))
    new += lowerChar
print(new)