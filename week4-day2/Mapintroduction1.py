x= {}
print(x)
x = {'97':"a" , "98":"b" , "99":"c" , "65":"A" , "66":"B",  "67":"C"}
print(x)
        
y = {'68':"D"}
print(y)


x = {'97':"a" , "98":"b" , "99":"c" , "65":"A" , "66":"B",  "67":"C"}
y.update(x)
print(y)

print(*x.items(), sep='\n')

x = {'97':"a" , "98":"b" , "99":"c" , "65":"A" , "66":"B",  "67":"C"}
for i in x:
        print(i)
print( "99 :"   +  "c") 

del x["97"]
print(x)

print(x["100"])

x.clear()
print('x = ', x)
  


