class student:
    def __init__(self,roll,name,marks): # These are the Local variables defined for the constructor
        self.roll=roll #self.roll will create a class variable with name roll
        self.name=name
        self.total=marks


    def displayinfo(self):
        print"Student details are",self.roll,self.name,self.total

# creating an object
s1 = student(1,"akshay",90) #this will invoke the constructor
s1.displayinfo()
print(s1.total)
print(s1.name)
print(s1.roll)



