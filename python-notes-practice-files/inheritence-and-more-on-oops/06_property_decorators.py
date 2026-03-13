class Employee:
    a = 1
  
    @classmethod

    def show(cls):
        print(f"The class attribute is : {cls.a}")

    @property
    def name(self):
        print (f"{self.fname} , {self.lname}")

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


o = Employee()
o.a=28

o.name = "Anurag Gupta"
print(o.fname,o.lname)

o.show()

# def of incapsualtion - The multiple working components linke objects , functions  are packed into one class or unit .
# def of abstraction - It means we have hided the implimentation deatails of the code from the user