s1={"chetan","Jaiprakash","jyotiprakash","Tanuja","chandbasha"}
s2={"chandbasha","Krishnakumar","Rishit","Tanuja"}
s3 = {"chandbasha","akshay"}

# Here Intersection update will update the value of s1 with the common elements
#of s2 and s3

#Symmetric difference it will remove the commom elements between s1 and s2 and return the
#Unique elements

r1 = s1.symmetric_difference(s2)

print("symmetric difference",r1)

#s1.intersection_update(s2,s3)

print(s1)

#s3 = s1.union(s2)

print(s3)
print(set(s3))

#s4= s1.intersection(s2)
#s5 =s1.intersection_update(s2)

# Intersection update - It will update the first set with the common elements  and remove
# rest of the elements

#print("s1 updated ",s1)
#print("s2 is",s2)
#print(s4)

#print(s5)

