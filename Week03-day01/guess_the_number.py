num=int(input("Please write a number to start : "))
count_of_guesses = 0
while num <= 10:
    user_guess = int(input("Guess: \n"))
    count_of_guesses += 1

    if user_guess < num:
        print("The stored number is higher")
    elif user_guess > num:
        print("The stried number is lower")
    else:
        print("You found the number :", num)
        break
else:
    print("Sorry you lost the game")