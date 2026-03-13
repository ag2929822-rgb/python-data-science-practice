f = open("file.txt")
print(f.read())
f.close()

# This same thing can be done by using the with statement

with open("file.txt") as  f:
       print(f.read())

# You dont need to close the file