import random
import time

def guessing_game():
    number = random.randint(1, 100)
    tracktime = time.time()
    while True:
        try:
            guess = int(input('Guess a number between 1 and 100 : '))
        except ValueError:
            print('Please enter a valid number')
            continue
        if guess < number:
            print('Too low')
        elif guess > number:
            print("Too high")
        else:
            timediff = time.time() - tracktime
            print("You guessed it! It took you " + str(timediff) + " seconds.")
            break

guessing_game()
