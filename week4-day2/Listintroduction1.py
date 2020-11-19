names = list()
print(len(names))
print(str(names))


  

test_str = "Wiliiam"
  
 
print("The original list : " + str(names)) 
  
print("The original string : " + str(test_str)) 
  

names += [test_str] 
  
print("The list after appending is : " + str(names)) 


test_str1 = "John"
names += [test_str1]
print("The list after appending is : " + str(names)) 


test_str2 = "Amanda"
names += [test_str2]
print("The list after appending is : " + str(names)) 
print(len(names))
print(names[2])

print(names)
test_str = "1. Wiliiam"
test_str1 = "2. John"
test_str2 = "3. Amanda"
print(test_str)
print(test_str1)
print(test_str2)
test_str1 = " "

test_str4 = "Wiliiam\n"
test_str5 = "Amanda"
newnames = " ".join((test_str4 , test_str5 ))
print(newnames)

names = ['Wiliiam', 'Amanda']
print('Original List:', names)

names.reverse()
for i in names:
    print(i)
print('Updated List:', names)




names = ['Wiliiam', 'Amanda']
for i in names:
    y = names.remove(i)
print(y)


