import random
lives = 6


words = ["lantern", "gravel", "whisper", "cactus", "orbit", "velvet", "harbor", "pickle", "thunder", "marble", "compass", "feather", "tundra", "saffron", "ripple", "anchor", "lemon", "shadow", "circuit", "meadow", "biscuit", "glacier", "tangle", "copper", "puzzle", "willow", "ember", "canyon", "mirror", "sparrow", "blanket", "quartz", "hammock", "trumpet", "nectar", "drizzle", "fossil", "jigsaw", "pepper", "lagoon", "ribbon", "cobweb", "monsoon", "thimble", "pendulum", "walnut", "horizon", "kettle", "mosaic", "plume"]
word = random.choice(words)

guessed = ["_"] * len(word)


def again():
    playagain = input("Would you like to play again? (y/n) ").lower().strip()
    if playagain == "y":
        play()
    elif playagain == "n":
        exit()
    else:
        print("Invalid choice, try again. ")
        again()


def play():
    global lives, word, guessed
    lives = 6
    word = random.choice(words)
    guessed = ["_"] * len(word)
    print("Welcome to hangman.")
    print("You have 6 lives.")
    print("The word is " + str(len(word)) + " letters long.")
    print("Good luck!")
    print(" ".join(guessed))

    while lives > 0:
        guess = input("Guess a letter: ")
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print(" ".join(guessed))
        else:
            lives -= 1
            print("Wrong! You have " + str(lives) + " lives left.")
            if lives == 0:
                print("You lose! The word was " + word + ".")
                again()
                break
        if "_" not in guessed:
            print("You win!")
            again()
            break

play()