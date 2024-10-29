#57. Take a string from the user and find out how many digits are there, how many special symbols are there, 
# how many small letters are there, how many caps are there.

string = input("string:")

digit_count = 0
special_char_count = 0
small_letter_count = 0
caps_count = 0
special = '!@#$%^&*{}[]+=-_()|\><?/`'
for each in string:
    if each.isdigit():
        digit_count +=1
    if each.isalpha():
        if each.islower():
            small_letter_count +=1
        else:
            caps_count +=1
    if  each in special:
        special_char_count +=1
print("number of digits: ", digit_count)
print("number of special characters: ", special_char_count)
print("number of small letters: ", small_letter_count)
print("number of caps: ", caps_count)