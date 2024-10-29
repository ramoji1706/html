# l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even numbers are there and 
# how many odd numbers are there and how many positive numbers are there and how many negative numbers are there and 
# how many prime numbers are there and how many perfect numbers are there and how many Armstrong numbers are there and 
# how many palindrome numbers are there.


l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
even_count=0
odd_count=0
positive_count=0
negative_count=0
prime_count=0
perfect_count=0
armstrong_count=0
palindrome_count=0

for i in l:
    if i%2==0:# checking even numbers
        even_count+=1
    if i %2 == 1:#  checking odd numbers

        odd_count+=1
    if i>0:#  checking positive numbers

        positive_count+=1
    if  i<0:#   checking negative numbers

        negative_count+=1
    if  i>1: # checking prime numbers
        count = 0
        for j in range(2,i):
            if (i % j) == 0:
                count+=1
        if count == 0:
            prime_count+=1
    if str(i) == str(i)[::-1]:
        palindrome_count+=1
    if i**(1/2) == int(i**(1/2)):
        perfect_count+=1
    if  len(str(i)) == 3 and i**(1/3) == int(i**(1/3)):
        armstrong_count+=1
print(even_count)
print(odd_count)
print(positive_count)  
print(negative_count)
print(prime_count)
print(perfect_count)
print(armstrong_count)
print(palindrome_count)