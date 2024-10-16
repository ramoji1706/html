#22. Take an age  and gender from the user: and mention that what he/she can 	do in india.
# conditions
#1. Theatre: 5 for men 7 for women
    #2. Voting system: 18 for men and women
#	3. Marriage in india: 23 for men and for women >21
#	4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women
#		5. For driving licence: (min:18, max:60) for men and women
#	Eligibility:
#		1. theatre
#			2.  Voting system
#			3.  Marriage in india
#			4.  For govt obs
#			5. For driving licence:
#	Enter an option:
#		Gender:
#			1. men
#			2. women
#	Enter an option:
#Enter an age of person:

gender = input("gender:")
age = int(input("age:"))

if(gender == "men" and age >=7):
    print("Elgible for Theatre")
if(gender == "men" and age >=18):   
    print("Eligible for Voting system")
if(gender == "men" and age >=21):   
    print("Eligible Marriage in india system")
if(gender == "men" and (age >=18 and age <=34)):   
    print("Eligible for govt jobs system")
if(gender == "men" and (age >=18 and age <=60)):   
    print("Eligible for driving licence system")


if(gender == "women" and age >=5):
    print("Elgible for Theatre")
if(gender == "women" and age >=18):   
    print("Eligible for Voting system")
if(gender == "women" and age >=23):   
    print("Eligible Marriage in india system")
if(gender == "women" and (age >=18 and age <=32)):   
    print("Eligible for govt jobs system")
if(gender == "women" and (age >=18 and age <=60)):   
    print("Eligible for driving licence system")
