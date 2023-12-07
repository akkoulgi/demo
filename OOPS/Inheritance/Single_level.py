#The following program demonstrates single level Inheritance

class moolya:
    a=1
    b=2

    def display(self):
        print("Parent class display")

class moolyaed(moolya):
    c=10
    d=90
    def training(self):
        print("moolyaed students")

obj1 =moolyaed()

obj1.display() # Accessing parent class methods from child class objects.
print(obj1.a) # Accessing parent class variables from child class object.







