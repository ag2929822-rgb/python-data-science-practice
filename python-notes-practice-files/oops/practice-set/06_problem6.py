from random import randint

class Train:


    def __init__(slf,TrainNo):
        slf.TrainNo= TrainNo

    def book(slf,fro,to):
        print(f"The ticket is booked train no is : {slf.TrainNo} form {fro} to {to}")

    def getStatus(slf):
        print(f"The Train No. : {slf.TrainNo} is running on time!!")

    def fare(slf,fro,to):
        print(f"The Train no. is : {slf.TrainNo} from {fro} to {to} ticket fare is {randint(1200,2000)}")
        

t = Train(129993)
t.book("Pune ","Nagpur")
t.getStatus()
t.fare("Pune ","Nagpur")

# Hence there is nothing happend when i changed the self by slf