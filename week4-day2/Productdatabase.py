products = {"Eggs" : "200" , "Milk" : "200" , "Fish" : "400" , "Apples" : "150" , "Bread" :	"50" , "Chicken" : "550"}
print("The price of Fish is :" , products["Fish"])

from collections import Counter

k = Counter(products) 
  

high = k.most_common(1)  
  
print(" most expensive product:") 
print(products, "\n") 
  
  
print("Dictionary with most expensive products:") 
print("Keys: Values") 

for i in high: 
    print(i[0]," :",i[1]," ") 

products = {"Eggs" : 200 , "Milk" : 200 , "Fish" : 400 , "Apples" : 150 , "Bread" :	50 , "Chicken" : 550}
print("The original dictionary is : " + str(products)) 
print(products.values())
total = 0
for k,v in products.items():
    total = total + v

avg = total / len(products)

 
print("average price : " + str(avg))  


  

below = 300
  
 
print ("The products : " + str(products)) 
  
count = 0
for k,v in products.items(): 
    if v < below : 
        count = count + 1
  
 
print ("The prices below than 300 : " + str(count)) 



print ("The products : " + str(products)) 
for k,v in products.items(): 
    if v == 125: 
        print(k)
    else:  
        print("there is nothing")



temp = min(products.values()) 
res = [key for key in products if products[key] == temp] 
  

print("Keys with minimum values are : " + str(res))  


