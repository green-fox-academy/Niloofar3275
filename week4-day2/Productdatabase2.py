products2 = {"Eggs" : 200 , "Milk" : 200 , "Fish" : 400 , "Apples" : 150 , "Bread" :	50 , "Chicken" : 550}


below = 201
  
 
print ("The products2 : " + str(products2)) 
  
count = 0
for k,v in products2.items(): 
    if v < below : 
        print(k)
    else: 
        print("")    

below2 = 150
  
 
print ("The products2 : " + str(products2)) 
  
count = 0
for k,v in products2.items(): 
    if v > below2 : 
        print(k,v)
    else: 
        print("")    
          
  
 
