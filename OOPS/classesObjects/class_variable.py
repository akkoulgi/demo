
class orange:
    a=10
    b=20
    def show(self):
        #print(a,b)  we cannot directly use class variables in methods of class.
        print(self.a,self.b)



obj1 =orange() #object created for orange class
obj1.show()

