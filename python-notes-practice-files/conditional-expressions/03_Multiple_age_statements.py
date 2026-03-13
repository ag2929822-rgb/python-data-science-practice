age = int(input("Enter the age:"))

#if statement No.1
if(age%2==0):
    print("a is even")

# If statement No.1 ends here

#if statement No.2
if(age>18):
    print("You are above the age limit")
    print("You are an adult")

elif(age<0):
    print("You are entering an negative age that is invalid")

elif(age==0):
    print("You are entering an age 0 that is not valid")

else:
    print("You are below the age limit")
    print("You are an child")
    # These are the conditionals loops in python 
#if statement No.2 ends here

    print("End of the program")