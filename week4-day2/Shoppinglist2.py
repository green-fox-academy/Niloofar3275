Shoppinglist2 = {"Milk" : 1.07 , "Rice" : 1.59 , "Eggs" : 3.14 , "Cheese" :	12.60 , "Chicken Breasts" :	9.40 , "Apples" : 2.31 , "Tomato" :	2.58 , "Potato" : 1.75 , "Onion" : 1.10}

Boblist = {"Milk" : 3 , "Rice" : 2 ,"Eggs" : 2 , "Cheese" : 1 , "Chicken Breasts" :	4 ,"Apples" : 1 , "Tomato" : 2 , "Potato" : 1}

Aliceshoppinglist = {"Rice" : 1 , "Eggs" : 5 , "Chicken Breasts" : 2 , "Apples" : 1 , "Tomato" : 10}


total = 0
for key in Boblist:
        key = (Shoppinglist2[key] * Boblist[key])
        print(key) 
        total = key + total
print(total)

total = 0
for key in Aliceshoppinglist:
        key = (Shoppinglist2[key] * Boblist[key])
        print(key) 
        total = key + total
print(total)


def who_buys_more(product_name):
  
    if (product_name in Aliceshoppinglist.keys() and product_name in Boblist.keys()):
        if (Aliceshoppinglist[product_name] > Boblist[product_name]):
            return "Alice"
        elif (Aliceshoppinglist[product_name] < Boblist[product_name]):
            return "Bob"
        else:
            return "Tie"

print("Who buys more rice?", who_buys_more("Rice"))  
print("Who buys more potato?", who_buys_more("Potato"))

if (len(Aliceshoppinglist) > len(Boblist)):
    print("Alice buys more distinct products")
else:
    print("Bob buys more distinct products")

if (sum(Aliceshoppinglist.values()) > sum(Boblist.values())):
    print("Alice buys more products")
else:
    print("Bob buys more products")
    
    