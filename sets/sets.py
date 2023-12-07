#Sets properties
#1) It stores Heterogenous data
#2)Sets are Mutable
#3) No Duplicate values are allowed
#4)Unordered Data collection - Index of Sets keeps on changing and is not fixed
#5)membership operator can be used.
#6) Sets are also stored in curly braces




s={1,2,3,4,5,6,7}

#Membership operator 'in'
#Membership operators are operators used to validate the membership of a value.
#: The 'in' operator is used to check if a value exists in a sequence or not


print(3 in s)

s.add(9)

print(s)

s.remove(9)

print(s)

p =s.pop()

print("popped ele is",p)

s.pop()

print(s)
