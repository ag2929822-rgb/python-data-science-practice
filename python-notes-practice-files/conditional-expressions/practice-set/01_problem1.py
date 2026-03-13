num1= int(input("enter a number 1:"))
num2=int(input("enter a number 2:"))
num3=int(input("enter a number 3:"))
num4=int(input("enter a number 4:"))

if(num1>num2 and num1>3 and num1>num4):
    print("The Greatest Number is num1",num1)

elif(num2>num1 and num2>num3 and num2>num4):
     print("The Greatest Number is num2",num2)

elif(num3>num1 and num3>num2 and num3>num4):
     print("The Greatest Number is num3",num3)

elif(num4>num1 and num4>num2 and num4>num3):
     print("The Greatest Number is num4",num4)

# if we are using the elif in our program then is no need to write the else statement