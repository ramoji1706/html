#26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or capital letter or number or special symbol
 

small_letters ="abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specials = "!@#$%^&*()_+-[]\|=,<.>/?'\|*/"

letter = input("letter:")

if letter in small_letters:
    print("small letter")
elif letter in capital_letters:
    print("capital letters")
elif letter in numbers:
    print("number")        
else:
    print("special symbol")    