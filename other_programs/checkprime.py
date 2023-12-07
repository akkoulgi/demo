num1 = int(input(" Enter a number"))

# logic to check prime is to divide the given number by 2 and check whether
# it is divisibe by any number between 2 and num/2

# For example - if we have 99
# then we check if 99 is divisible by any number between
# 2 and 99/2

for i in range(2,int(num1/2)+1):
    if(num1%i==0):
        print("The number is not a prime")
        break
else:
    print("The number is  prime")
