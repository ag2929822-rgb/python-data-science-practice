class demo:
    a = 4

o = demo() 
print(o.a) # this prints the class attribute because the instance attribute is not present

o.a = 0     # instance attribute is set
print (o.a)  # this prints the instance attribute becuase the instance attribute is present

print(demo.a) # prints the class attribute

# hence the class atttribute does not changes