


class onebhk:
    rate=10000
    address="marathahalli"
    color="blue"

    def housedetails(self):
        print("House is 1 bhk")


class twobhk(onebhk):
    # overrides attributes in 1bhk
    rate=130000
    address="whitefield"
    color = "red"

    def housedetails(self):
        print("house is 2bhk")

    def floor(self):
        print("house in second floor")


class threebhk(twobhk):
    rate=25000
    address="vijaynagar"
    color="white"
    def housedetails(self):
        print("the house is 3 bhk")

#Creating an object for threebhk

obj1=threebhk()
obj1.housedetails()  #By creating an object and accessing the overridden implementation
obj1.floor()
print(obj1.rate)
print(obj1.color)
print(obj1.address)





