from random import randint

def guess_the_number(name):
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    number = randint(1, 20)
    attempts = 0

    while True:
        print('Take a guess.')
        guess = int(input())
        attempts += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print(f'Good job, {name}! You guessed my number in {attempts} guesses!')
            break  # Останавливает программу после правильного ответа

print("Hello! What is your name?")
name = input()
guess_the_number(name)

