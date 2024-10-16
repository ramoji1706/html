#WAP to check given string contains numbers or not. it should consider float numbers also.
import re

s = input("string: ")
pattern = r'\d+(\.\d+)?'

if re.search(pattern,s):
    print(True)
else:
    print(False)    