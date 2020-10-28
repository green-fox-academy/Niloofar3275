stored_number=int(input("Please write a number to start : "))
count_of_guesses = 0
while stored_number <= 10:
    user_guess = int(input("Guess: \n"))
    count_of_guesses += 1

    if user_guess < stored_number:
        print("The stored number is higher")
    elif user_guess > stored_number:
        print("The stried number is lower")
    else:
        print("You found the number :", stored_number)
        break
else:
    print("Sorry you lost the game")