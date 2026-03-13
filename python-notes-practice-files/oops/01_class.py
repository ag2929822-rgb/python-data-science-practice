class Employee:
  Language = "Py" #This is an classs attributes
  Salary = 100000  #This is an classs attributes


anurag = Employee()  #These are object  (instance ) attributes
anurag.name= "Anurag"
print(anurag.name,anurag.Language,anurag.Salary)

harry = Employee() #These are object (instance) attributes
harry.name="Harry"
print(harry.name,harry.Salary,harry.Language )

#Here the names likes Anurag ,Harry are Object attributes and Language and Salary etc are class attributes as the directly related to class Employee()



