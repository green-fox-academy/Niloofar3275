# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")