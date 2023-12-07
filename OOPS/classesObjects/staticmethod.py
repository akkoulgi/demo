

class moolya:
    def freshers(self,n1,n2):
        print("freshers of moolya",n1,n2)

    @staticmethod
    def experienced(self,n1,n2):
        print("Experienced candidates of moolya",self,n1,n2)


obj1 =moolya() #creating an object of moolya class.

obj1.freshers(9,10)
obj1.experienced(90,10,100) #accessing static method through object obj1.

moolya.experienced(10,20,20)


