#  4.take four number from the user (variables name it as x1,x2,x3,x4)
#Do the below operations
#(x1+x2)*2, (x3+x4)*3
#variance
#standard deviation: sqrt(variance):  User math module. Math.sqrt(variance)
#Regression
#y=mx+b
          #m=1.23
          #b=0.045
          #find out y
          #y=m*(x1+x2+x3+x4)+b
#Find the average of four numbers
#Find the sum of four numbers


import math

x1 = int(input("x1"))
x2 = int(input("x2"))
x3 = int(input("x3"))
x4 = int(input("x4"))

avg_of_four_numbers = (x1+x2+x3+x4)/4
sum_of_four_numers = x1+x2+x3+x4


operation =  (x1+x2)*2, (x3+x4)*3
variance = ((1-avg_of_four_numbers)**2 + (2-avg_of_four_numbers)**2 + (x3-avg_of_four_numbers)**2 + (x4 - avg_of_four_numbers)**2)/4
standard_deviation = math.sqrt(variance)

m = 1.23
b = 0.045

y = m*(x1+x2+x3+x4)+b
print(operation)
print(y)

print(variance)
print(standard_deviation)

print(avg_of_four_numbers)
print(sum_of_four_numers)