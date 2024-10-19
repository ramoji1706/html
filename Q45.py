#45. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This should continue until and until user gives a correct number or want to quit in the middle.
#Get a hidden number by using random.randint(1,100)
import random

randomNumber = random.randint(1,100)

result = True
while result:
    user = int(input("number:"))    
    if(user == randomNumber):
        print("YES")
        result = False
    elif (user == 0):
        print("quit")
        break
    elif (user>randomNumber):
        print("Higher")
        
    elif (user<randomNumber):
        print("Lower")
    