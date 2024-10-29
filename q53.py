#51. print the number in proper mathematical way.
#	Consider that we have 6 digit numbers.
#Number format  WAP> 10 -> 000010
#		1000 ->  001000
#		 2345678  ->  2345678
#	If the number has morethan 6 digits then print as it is.

number = int(input("number:"))

if len(str(number))>=6:
    print(number)
else:
    length = len(str(number))
    zeros = '0'*  (6-length)
    print(zeros+str(number))