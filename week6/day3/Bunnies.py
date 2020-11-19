def bunnyEars(bunnies):
    if bunnies == 0: 
        return bunnies
    return bunnyEars(bunnies - 1) + 2

number_of_bunnies = 5
result =  bunnyEars(number_of_bunnies) 
