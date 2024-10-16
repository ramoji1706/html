#44. Determine the factors of a number entered  by the user

number = int(input("number:"))

for i in range(1,number):
    if number % i ==0:
        print(i)