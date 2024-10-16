#23. operating systems:
#	1.windows
#	3.mac
#Enter an option:

#If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
#If the user enters 2 then show "Goto second floor and buy adroid mobiles"
#If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
#If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"

user = int(input("Enter floor No:"))

if(user == 1):
    print("Goto first floor and buy windows laptop or mobile")
elif(user == 2):
    print("Goto second floor and buy adroid mobiles")    
elif(user == 3):
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")
