#61. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.
#62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba
#63.Input:abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^
#64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^
#Only numbers has to reverse.

Input= "abc123,#$45def6%$^789$%^"

alpha=[]
special = []
digits = []
for char in Input:
    if char.isdigit():
        digits.append(char)
    elif  char.isalpha():
        alpha.append(char)
    else:
        special.append(char)
alpha.reverse()
digits.reverse()

Output = ''.join(special)+ ''.join(digits)+ ''.join(alpha)
print(Output)