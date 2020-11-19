def bunnyEars2(bunnies):
    if bunnies == 0: 
        return bunnies
    return bunnyEars2(bunnies - 1) + 3 - (bunnies % 2)

   