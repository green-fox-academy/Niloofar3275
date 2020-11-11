# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

num1=int(input("Please write the number of chickens the farmer has ="))
num2=int(input("Please write the number of pigs owned by the farmer ="))
legs_num1=num1 * 2
legs_num2=num2 * 4

legs_animals= legs_num1 + legs_num2
print("The number of legs all the animals have is:", legs_animals)
