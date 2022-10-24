import random

# random number being selected
num = random.randint(0, 100)


# rules of the game
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# list to store the guesses
guesses = [0]

# while loop for execution of the game
while True:

    guess = int(input("I'm thinking of a number between 1 and 100 \n What is your Guess? \n"))

    # num should be less than 100 and more than 1
    if guess < 1 or guess > 100:
        print("Out of Bounds! try again\n")
        continue

    # if user guesses the num it tells how many guesses user took
    if guess == num:
        print(f'CONGRATULATIONS, You Guessed the number and it only took you {len(guesses)} GUESSES!!')
        break

    # when guess is incorrect add guess to the list
    guesses.append(guess)

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')