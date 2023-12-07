g1=10
g2=90 # these are Global variables

class moolya:
    c1=78
    c2=22 #c1 and c2 are class variables.

    def show(self):
        l1=25
        l2=60
        print("local variables are ",l1,l2) #accessing loval variables directly
        print("Global vaariables are",g1,g2) #accessing gloal variables directly
        print("Class variables are",self.c1,self.c2) # accessing class variables using self


obj1=moolya()
obj1.show()










