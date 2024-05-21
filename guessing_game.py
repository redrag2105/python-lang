import random

def main():
    level = get_level()
    random_number = random.randint(1, level)
    guess = 0
    while guess != random_number:
        guess = get_guess()
        message = check_guess(guess, random_number)
        print(message)
        if message == "Just right!":
            break

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and 10 >= int(level) >= 1:
            return int(level)

def get_guess():
    while True:
        guess = input("Guess: ")
        if 1 <= int(guess) <= 10 and guess.isdigit():
            return int(guess)

def check_guess(guess, random_number):
    if guess < random_number:
        return "Too small!"
    elif guess > random_number:
        return "Too large!"
    else:
        return "Just right!"

main()
