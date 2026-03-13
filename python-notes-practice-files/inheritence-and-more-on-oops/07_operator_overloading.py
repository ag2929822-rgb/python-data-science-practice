class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num): # we can do this any operators like add,sub,mul,truediv etc
        return self.n + num.n
    

n = Number(1)
m = Number(2)

print ( n + m) 
      