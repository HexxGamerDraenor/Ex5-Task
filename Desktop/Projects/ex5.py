beerBottles = 99

for beerBottles in range(99, -1, -1):
    print(beerBottles + "bottles of beer on the wall, " + beerBottles + "bottles of beer." + "\nTake one down, pass it around, " + beerBottles + "bottles of beer on the wall")
    if(beerBottles == 0):
        print ("Safety net for beer bottles being 0")
