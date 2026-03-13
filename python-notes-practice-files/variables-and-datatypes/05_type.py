#Type function is used to indentify the data type
a = 31
t = type(a) # class <int> 
print(t)

# Simple Conversion of the string ( data type) into the another datatype
a = "31.2"
t = type(a) # class <int> 
print(t)


# Conversion of the type function by using the data type
a = "31.2"
b = float(a)# a but the type should be float
t = type(b) # class <int> 
print(t)