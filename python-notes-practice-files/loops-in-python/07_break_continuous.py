for i in range(100):
    print(i)
    if( i == 34):
      break # Exit the Loop right
    print(i)


for i in range(100):
    print(i)
    if( i == 34):
      continue # skip this iteration
    print(i)


for i in range (0,80): 
    print(i)     
# this will print 0,1,2 and 3 
    if (i == 3):
        break 


for i in range(4): 
   print("printing") 
   if i == 2:   # if i is 2, the iteration is skipped  
    continue 
print(i) 