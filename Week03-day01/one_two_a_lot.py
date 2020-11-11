# Write a program that reads a number form the standard input,
# If the number is zero or smaller it should print: Not enough
# If the number is one it should print: One
# If the number is two it should print: Two
# If the number is more than two it should print: A lot


num = int(input("Enter a number: "))
mod = num
if mod <= 0:
    print("Not enough")
elif mod ==1:
    print("One")
elif mod==2:
    print("Two")
elif mod > 2:
    print("A lot")