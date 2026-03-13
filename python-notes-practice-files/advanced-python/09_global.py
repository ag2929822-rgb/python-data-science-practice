a = 89 # global variable

def func():
     global a # changes the global variable in to local func variable
     a = 3
     
     print(a)

func()
print(a)
