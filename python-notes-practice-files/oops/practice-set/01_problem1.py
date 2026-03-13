class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,salary,pincode):
       self.name= name
       self.salary= salary
       self.pincode= pincode

p = Programmer ("Anurag",100000,440008)
print(p.name,p.salary,p.pincode)

p = Programmer ("Harry",2000000,1212)
print(p.name,p.salary,p.pincode)