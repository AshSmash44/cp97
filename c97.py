import random
answer = random.ranint(1,9)
chances = 0

print("This is a number guessing game where you can guess numbers")

while chances < 5:
    guessingGame = int(input("guess a number between 1 and 9: "))
    if guessingGame == answer:
        print("Congratulations, you guessed the guessing game answer!")
        break
    elif guessingGame > answer:
        print("you guessed too high, guess again", guessingGame)
    elif guessingGame < answer:
        print("you guessed too low, guess again", guessingGame)
    chances += 1
if chances >= 5:
    print("the answer was ", answer)
    print("you lost the game, please restart the code to try again")
