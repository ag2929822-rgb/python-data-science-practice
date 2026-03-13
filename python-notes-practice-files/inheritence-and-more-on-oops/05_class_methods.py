class Employee:
    a = 1
  
    @classmethod

    def show(self):
        print(f"The class attribute is : {self.a}")

o = Employee()
o.a=28
o.show()