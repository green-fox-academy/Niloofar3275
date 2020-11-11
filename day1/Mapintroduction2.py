
x = {"978-1-60309-452-8" : "A Letter to Jo" ,  "978-1-60309-459-7" : "Lupus" , "978-1-60309-444-3" :"Red Panda and Moon Bear" ,"978-1-60309-461-0" : "The Lab"}

for k,v in x.items(): 
    print(str(v) + " (ISBN: " + str(k) + ")")
print(*x.items(), sep='\n')




del x["978-1-60309-444-3"]
print(x)


del x["978-1-60309-461-0"]
print(x)


x = {"978-1-60309-452-8" : "A Letter to Jo" ,  "978-1-60309-459-7" : "Lupus" , "978-1-60309-444-3" :"Red Panda and Moon Bear" ,"978-1-60309-461-0" : "The Lab"}
print(x)
y = {"978-1-60309-453-5" : "Why Did We Trust Him?" ,"978-1-60309-450-4" : "They Called Us Enemy"}
x.update(y)
print(x)

print(x["478-0-61159-424-8"])

print(x["978-1-60309-453-5"])