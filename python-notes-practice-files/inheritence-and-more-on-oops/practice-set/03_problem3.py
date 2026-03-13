class Employee:
    salary = 500
    increament = 20

    @property
    def salaryAfterIncreament(self):
        return (self.salary + self.salary * (self.increament/100))
    
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,salary):
        self.increament = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryAfterIncreament)
e.salaryAfterIncreament = 550.0
print(e.increament)