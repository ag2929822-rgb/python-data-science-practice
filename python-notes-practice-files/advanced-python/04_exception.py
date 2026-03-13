try:
    n = int(input("Hey,Enter a Number :"))
    print(n)

except ValueError as v: # These types of commands are used for error handling
    print("Hey Anurag")
    print(v)

except Exception as e:
    print(e)

print("Thank You!")