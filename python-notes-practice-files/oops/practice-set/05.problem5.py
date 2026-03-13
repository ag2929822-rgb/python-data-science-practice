from random import randint

class Train:


    def __init__(self,TrainNo):
        self.TrainNo= TrainNo

    def book(self,fro,to):
        print(f"The ticket is booked train no is : {self.TrainNo} form {fro} to {to}")

    def getStatus(self):
        print(f"The Train No. : {self.TrainNo} is running on time!!")

    def fare(self,fro,to):
        print(f"The Train no. is : {self.TrainNo} from {fro} to {to} ticket fare is {randint(1200,2000)}")
        

t = Train(129993)
t.book("Pune ","Nagpur")
t.getStatus()
t.fare("Pune ","Nagpur")