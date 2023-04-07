# Number guessing game
# Higher or Lower
# Range
import random
level = 0

print("WELCOME TO THE NUMBER GUESSER")

print("EASY mode generates a random number from 1 - 100.")
print("HARD mode generates a random number from 1 - 1000.")
easy_or_hard = input("Would you like to choose EASY or HARD Mode: ")
print("You have chosen " + easy_or_hard.upper() + " Mode.")

while True:
            if easy_or_hard == "Easy" or easy_or_hard == "easy" or easy_or_hard == "EASY": 
                level = random.randint(1, 100)
                break

            elif easy_or_hard == "Hard" or easy_or_hard == "hard" or easy_or_hard == "HARD": 
                level = random.randint(1, 1000)
                break
            
            else:
                print("Choose Easy or Hard.")
                continue



guess = int(input("Choose a random number: "))

while True:
    if guess > level:
        print("The number is LOWER.")
        guess = int(input("Choose a random number: "))
        continue
    elif guess < level:
        print("The number is HIGHER.")
        guess = int(input("Choose a random number: "))
        continue
    else:
        print("You found the number!!!")
        break


