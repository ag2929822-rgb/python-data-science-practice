Human = ["Anurag",29,28,"Harry",0.7,"Vit Pune","Pune",True]
Human.append("Sexy") # The List 1st Method append
print(Human)


Numbers = [1,6,5,4,8,3,0] 
Numbers.sort() # 2nd Method that sorts the list is ordered form
print(Numbers)

Numbers.reverse() #3rd Methods reverse the list in ordered form
print(Numbers)

Human.insert(1,"Nagpur")
print(Human)

Human.pop(0)
Numbers.pop(3)
value = Numbers.pop(2)
print(Human)
print(Numbers)
print(value)

Human.remove(True)
print(Human)