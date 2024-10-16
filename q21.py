#21. Take age and gender from the user and decide whether he is eligible for 	marriage in India or not.
#Age criteria: men age>24, women>21

age = int(input("age:"))
gender = input("gender:")

if((age>24 and gender=="men") or (age>21 and gender=="women")):
    print("Eligible")

else:
    print("Not Eligible")