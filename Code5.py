import random


loop = "y"

while loop == "y":

    GeneratedNumber = random.randrange(1, 20)
    UserGuess = input("Please enter your number: ")

    try:
        UserGuess = int(UserGuess)
        if UserGuess == GeneratedNumber:
            print("You are correct!")
        else:
            print("You are incorrect!")
    except:
        print("Please enter a number...")

        
    loop = input("Play Again? y/n = ")
    loop = loop.lower()

    while loop != "y" and loop != "n":
        print("That's not a valid answwer. Please enter y/n")
        loop = input("Play Again? y/n = ")
        loop = loop.lower()

    if loop == "n":
        print("Please come play with us again soon!")