class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printfullname(self):
        print(self.firstname,self.lastname)


#creating an object of person class to initialize the variables of firstname,
# last name and printing them

obj=Person("akshay","koulgi")
#printing using direct print statement
#print(obj.lastname,obj.firstname)
#printing using printfullname() defined in person class
obj.printfullname()

#Using Inheritance to access the properties of child class
#Inheritance is used
class student(Person):
    pass


x=student("anil","kumble")
x.printfullname()
x.printfullname()

class third:

    y=student("karan","singh")
    print("printing from a third class , creating an object of student class")
    y.printfullname()



