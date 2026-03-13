with open("log.txt","r") as f:
    content = f.read()

    if("Python" in content):
     print("Yes the Python is present in the content")

    else:
       print("No the Python is not present in the content")