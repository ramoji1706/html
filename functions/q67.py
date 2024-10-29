#FUNCTIONS:
#65. define a function to take person details name and age are mandatory parameters and height weight are optional parameters.
# If the user willing to pass any other details(like adhar, cell, pan, passport etc..)
#  regarding him then your function should access those details.

#	65a. rewrite above assignments by functions. Can use string functions to solve the string related assignments
#65 b. write a function to check given value is even or not
#	65 c. write a function to check given value is prime or not
#	65 d. write a function to check given 2 values are  divisible or not

def  person_details(name, age, height=None, weight=None):
    return(name,age,height,weight)

res = person_details("ramoji",25)
print(res)

#65 b. write a function to check given value is even or not
def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers = [1,2,3,45,6,7,8,9]
for num in numbers:
    print(num,"is even" if check_even(num) else "is odd")
#65 c. write a function to check given value is prime or not
def check_prime(num):
    if num >1:
        for  i in range(2,num):
            if (num % i) == 0:
                return False
            else:
                return True
res = check_prime(4)
print(res)
#65 d. write a function to check given 2 values are  divisible or not
def check_divisible(num1,num2):
    if (num1%num2) ==0:
        return True
    else:
        return False
res = check_divisible(10,2)
print(res)