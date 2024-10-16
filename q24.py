#24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.

age = int(input("age:"))

if (age >=0 and age <=1):
    print("baby")
if (age >1 and age <=2):
    print("Toddler")
if (age >=5 and age <=12):
    print("Child")
if (age >=13 and age <=19):
    print("Teenager")
if (age >=20 and age <60):
    print("Adult")
if (age >=60):
    print("Old codger")

