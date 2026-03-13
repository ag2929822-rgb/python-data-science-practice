class Employee: # Parent class
    a = 1

class Programmer(Employee): # child class1
    b = 2

class Manager(Programmer): # child class2
    c = 3

o = Employee() 
print(o.a) # Prints a = 1 at a output
# print(o.b) # Gives an error cause Employee class does not contains attribute b

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)
