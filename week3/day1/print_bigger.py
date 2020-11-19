# Write a program that asks for two numbers and prints the bigger one

a = input("Please write 2 numbers : \n")
first = int(a)
b = input()
second = int(b)
if first>second:
    bigger=first
else:
    bigger=second
print("The bigger one is : ", bigger)