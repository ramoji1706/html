input = "Google"
input = input.lower()

count = {}
for char in input:
    if char not in  count:
        count[char] = 1
    else:
        count[char]+=1
print(count)