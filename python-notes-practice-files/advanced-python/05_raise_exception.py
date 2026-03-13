a = int(input("Enter a 1st Number :"))
b = int(input("Enter a 2nd Number :"))


if ( b == 0 ):
    raise ZeroDivisionError("Hey our program is not meant to divide the numbers by zero")

else:
    print(f"The division of a/b is {a/b}")