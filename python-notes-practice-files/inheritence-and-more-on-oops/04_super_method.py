class Employee: # Parent class
    def __init__(self):
        print("Consturctor of Employee")
    a = 1

class Programmer(Employee): # child class1
    def __init__(self):
        super().__init__()
        print("Consturctor of Programmer")
    b = 2

class Manager(Programmer): # child class2
    def __init__(self):
        super().__init__()
        print("Consturctor of Manager")
    c = 3

o = Employee() 
print(o.a) # Prints a = 1 at a output
# # print(o.b) # Gives an error cause Employee class does not contains attribute b

# o = Programmer()
# print(o.a,o.b)

# o = Manager()
# print(o.a,o.b,o.c)