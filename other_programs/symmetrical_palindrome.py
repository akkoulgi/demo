s="okiokil"

# To check whether string is symmetrical or not.
flag=0

length = len(s)

if length%2==1:
    flag=1

#to check whether string is symmetricl or not

#First we need to check whether the string length is even or odd.
n = len(s)

mid=n//2
#if n%2:
#    mid= n/2  # if it is even then we increment the mid value to 1
#else:
    #mid=n//2

start1=0
start2=mid

while(start1<mid and start2<n):
    if(s[start1]==s[start2] and length%2==0):
        start1=start1+1
        start2=start2+1
    else:
        flag=1
        break





if flag==1:
    print("The string is not symmetrical")
else:
    print("The string is symmetrical")
