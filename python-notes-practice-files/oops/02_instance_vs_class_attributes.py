class Employee:
  Language = "Py" #This is an classs attributes
  Salary = 100000  #This is an classs attributes


anurag = Employee()  #These are object  (instance ) attributes

anurag.Language= "Java" # This will print only the instance attributes ("Java") not class attributes ("Python")

print(anurag.Language,anurag.Salary)
