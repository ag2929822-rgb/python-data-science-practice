class Employee:
  language = "Java" #This is an classs attributes
  Salary = 100000  #This is an classs attributes
 
  def __init__(self,name,language,Salary): # dunder method which is automatically called
    print("I am creating an object")
    self.name = name
    self.language =language
    self.Salary = Salary

  @staticmethod
  def greet():
    print("Good Morning")

  def getInfo(self):
    print(f"The language is {self.language}. The Salary is {self.Salary}")


Anurag = Employee("Anurag","Python",100000)  #These are object  (instance ) attributes
# Anurag.name= "Anurag"
print(Anurag.name,Anurag.Salary,Anurag.language)

