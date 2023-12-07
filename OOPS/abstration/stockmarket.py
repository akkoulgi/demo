#The following program demonstrates Abstration in Python.

from abc import ABC,abstractmethod

#This is an abstract class containing abstract/empty methods
class groww(ABC):
    @abstractmethod
    def rules(self): #Abstract method
        pass

    @abstractmethod
    def trading(self):
        pass
    @abstractmethod
    def mutualfunds(self):
        pass


class zerodha(ABC):
    @abstractmethod
    def rules(self):
        pass
    @abstractmethod
    def trading(self):
        pass

    @abstractmethod
    def mutualfunds(self):
        pass


#In this class, we are providing implementation for the abstract method
# rules nad trading
class sebi(groww,zerodha):
    def rules(self):
        print("Rules are followed by groww,zerodha set by sebi")

    def trading(self):
        print("trading are allowed to users using sebi rules")

    def mutualfunds(self):
        print("Mutual funds rules and activities are followed using sebi rules")


obj1 =sebi()
obj1.rules()
obj1.mutualfunds()
obj1.trading()


# here we achieved abstration through abstract methods.Method over riding  and through Multiple Inheritance
# Multiple Inheritance - one child class inheriting from 2 parents.





