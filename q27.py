#27. take a number from the user and check whether it is prime?

number = int(input("number:"))

count = 0
for i in range(2,number):
    for j in range(number % i == 0):
        count += 1
if count == 0:
    print("It is prime")
else:
    print("It is not  prime")
