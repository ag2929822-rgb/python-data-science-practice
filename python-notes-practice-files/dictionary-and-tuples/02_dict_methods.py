d = {}
print(type(d))
name = {
    "Anurag":9.1,
    "Harry":9.9,
    "List":[1,2,3],
    10:"Lobu"
}

print(name.items()) # this print the key:value pairs
print(name.keys()) # this prints the keys of  th dict ex- "Anurag","Harry" etc
print(name.values()) # this prints the values of  th dict ex- 9.1,9.9 etc
name.update({"Jay":9,"Anurag":9}) # this updates and adds the new key; value pair
print(name)

print(name.get("Anurag1")) #prints None
print(name["Anurag1"]) #gives an error
