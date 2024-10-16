#35 Convert the total string in to upper case. Without using upper() function.

s = input()


new = ""
for each in s:
    upperChar = chr((ord(each)-32))
    new += upperChar
print(new)