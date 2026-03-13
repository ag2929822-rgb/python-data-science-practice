num = int(input("Enter a NUmber : "))


for i in range(2, num):
    if(num%i == 0): 
     print("The Number is  Not Prime")
     break

else:
   print("The Number is Prime")