
#Defining set a
a={0,1,2,3,6}


for i in a:
    if i%2==0:
        print(i)


#List comprehension
evenlist=[i for i in a if i%2==0]
oddlist=[i for i in a if i%2==1]


print("oddlist ",oddlist)
print("even list ",evenlist)

#Difference in java and python for print statement
# IN java, to print the elements from we use a[i]
#But in python we just use i to print the elements