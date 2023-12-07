try:
    number = int(input("enter a number"))
    print(number)


except ValueError:
    print("Wrong data type, please enter the correct data type of integer")

finally:
    print("execution resumes after exception handling")
