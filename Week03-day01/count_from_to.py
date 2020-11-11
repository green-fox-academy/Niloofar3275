a = input("Please write 5 integers in a row : \n")
first = int(a)
b = input()
second = int(b)
if second <= first :
    print("The second number should be bigger")
else:
    for i in range(first,second):
        print(i)