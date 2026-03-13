with open("log.txt","r") as f:
    lines = f.readlines()

lineno = 1

for line in lines:

  if("Python" in line):
     print(f"Yes the Python is present in the content. Line no.{lineno}")
     break
  
  lineno +=1

else:
      print("No the Python is not present in the content")
    