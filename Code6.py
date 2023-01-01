"""
Haging man game words game
 _____
|     |
|     O
|    /|\    
|    / \ You Lost!

"""

stickman = (" _____", "|     |",  "|     O", "|    /|\   ", "|    / \ You lost!")
loop = "y"


while loop == "y":
    word = input("Game master, please write the word: ")

    question = ["_"] * len(word)
    tries = len(stickman)
    count = 0
    
    while tries > 0:
        PlayerAnswer = input("Player, please write your letter: ")
        i = 0
        draw = 0
        draw2 = 4
        check = 0
        for letter in word:
            if PlayerAnswer == letter:
                question[i] = letter
                i += 1
                check += 1
                count += 1
            else:
                i += 1
        print(question)
        
        if check == 0:
            print("Incorrect!")
            tries -= 1
            draw2 -= tries
            while draw <= draw2:
                print(stickman[draw])
                draw += 1
        
        if count == len(word):
            print("You win!")
            break


    loop = input("Try again? y/n ")
    loop = loop.lower()

print("Come play with us soon!")
