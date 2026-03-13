class Employee:
  language = "Python" #This is an classs attributes
  Salary = 100000  #This is an classs attributes
 
  @staticmethod
  def greet():
    print("Good Morning")

  def getInfo(self):
    print(f"The language is {self.language}. The Salary is {self.Salary}")


Anurag = Employee()  #These are object  (instance ) attributes

Anurag.language="Java"  #These are object  (instance ) attributes


Anurag.greet()
# anurag.getInfo()
Employee.getInfo(Anurag)

