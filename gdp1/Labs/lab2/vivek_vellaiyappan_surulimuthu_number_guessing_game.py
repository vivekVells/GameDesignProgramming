import random

secret_number = random.randrange(1, 129)
print("Secret_number: ", secret_number)
guess = 0
guesses = []
quit_status = False

while guess != secret_number:
    if quit_status is True or len(guesses) >= 7:
        break

    inp = (input("Guess a number 1 to 128: "))

    if inp == 'q':
        quit_status = True
        break

    guess = int(inp)
    guesses.append(guess)

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct!")


if not quit_status:
    print("\nYour guesses: ", end=' ')
    for val in guesses:
        print(val, end=' ')