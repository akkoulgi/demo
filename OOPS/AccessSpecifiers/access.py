class orange:
    a=10 # public variable
    _b=20 # Protected variable
    __c= 30 # Private variable

    print(a,_b,__c)

    def add(self):
        self.__c=self.a+self._b
        print("trying to print private variable inside class",self.__c)

obj1=orange()
obj1.add()

print(obj1.a)
print(obj1._b)
#print("trying to print private variable outside class",obj1.__c)

class orange2(orange):
    def display(self):
        print("public variable of another class",self.a)
        print("protected variable",self._b)
        # print("private variable",self.__c) # trying to access private variable inside another class


obj2=orange2()
obj2.display()
print(orange2.a)
print(orange2._b)
# print(orange2.__c)

#Conclusion -
# Public Members can be accessed anywhere - inside, outside class
#Protected members can be accessed inside class and in inherited classes only.
# private members can be accessed only inside the class
# Private members can not be accessed outside the class even in inherited classes




