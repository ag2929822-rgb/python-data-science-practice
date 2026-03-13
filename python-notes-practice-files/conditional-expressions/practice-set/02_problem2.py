marks1 = int(input("Enter a Marks1 :"))
marks2 = int(input("Enter a Marks2 :"))
marks3 = int(input("Enter a Marks3 :"))

#check total percentage
total_percentage = (100*(marks1 + marks2 + marks3)/300)

if(total_percentage>=40 and marks1 >=33 and marks2>=33 and marks3>=33):
    print("You are passed good boy",total_percentage)
else:
    print("You are failed come next year",total_percentage)