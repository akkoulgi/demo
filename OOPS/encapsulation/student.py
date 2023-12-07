class bank:
    def __init__(self,name,ifsc,account_num):
        self.name=name
        self._ifsc=ifsc
        self.__account_num=account_num



# obj1=bank("icici_akshay","89asdasd",90900212)
# print("bank details of akshay")
# print(obj1.name)
# print(obj1._ifsc)
# #print(obj1.__account_num) # cannot access private data member outside class


class branch(bank):
    pass
    #print(obj1.name)
    #print(obj1._ifsc)
    #print(obj1.__account_num)


obj2=branch("sbi","214fdsf",90)

print(obj2.name)
print(obj2._ifsc) # can access protected data member through inheritance
#print(obj2.__account_num) #cannot access private data members

