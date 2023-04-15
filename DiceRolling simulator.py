import random


def dice_rolling_simulator():
    numofdice= int(input("Enter the number of dice:\n"))
    sidesofdice=int(input("enter the number of sides the dice has:\n"))
    
    print("\nDice rolling in process....\n")

    for i in range(numofdice):
        roll = random.randint(1,sidesofdice)
        print(f" Die {i+1} rolled: {roll}")

        print("\ndone rolling the dice\n")

dice_rolling_simulator()
