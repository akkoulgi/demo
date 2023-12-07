str = "the_good_the_bad_and_the_ugly"

print(len(str))

#Slicing example

print(str[0:8])

# In slicing, if we give 0:8 , then it will
# slice away all the elements except the first 8 elements

print(str[0:12])
print(str[0:16])

#Alternate slicing
print(str[0:16:2])

#explanation - Step 1 - First it will fetch the forst 16 elements and slice the rest
#Step 2 - the next :2 will slice the alternate elements from the str[0:16]
