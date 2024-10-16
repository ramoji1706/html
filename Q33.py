#33. WAP to replace last n occurrence of give string.
#For example:”apple,orange,apple,grape,orange,apple,apple,orange”
#source: “apple”
#last occurrences: 2
#replace with: APPLE
#output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”

input = "apple,orange,apple,grape,orange,apple,apple,orange"
source = "apple"
last_occurrences= 2
input = input.split(",")
length = len(input)

newList = []
count = 0
revList = input[::-1]
for i in range(length):
    if revList[i] == source:
        revList[i] = source.upper()
        count +=1
    if count == last_occurrences:
        break
revList = revList[::-1]
print(",".join(revList))