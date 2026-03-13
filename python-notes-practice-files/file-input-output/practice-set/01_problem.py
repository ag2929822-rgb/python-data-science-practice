f = open("poems.txt")
data = f.read()

if("Twinkle" in data):
    print("Yes the poems.txt file contains Twinkle Twinkle ")
else:
    print("No the poems.txt file does not contains Twinkle Twinkle ")

f.close()
