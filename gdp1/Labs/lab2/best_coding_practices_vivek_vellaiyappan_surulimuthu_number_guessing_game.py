'''
Questions:
- aim was to reduce the lines of code; but ended up with more lines because of explanation quotes
- best practices!
'''

# importing random library package to generate random numbers
import random

# generating a random number in 1 through 129 range as secret number to be guessed out
secret_number = random.randrange(1, 129)
print("Secret_number: ", secret_number)
guess = 0
guesses = []
quit_status = False

'''
Condition:
- quit program if user press 'q'
- quit program if user guess exceeds 7
'''
# handling above conditions
while guess != secret_number:

    if quit_status is True or len(guesses) >= 7:
        break

    # defensive programming here; handle any type of inputs and proceed accordingly in any situations
    try:
        query = (input("Guess a number 1 to 128: "))
        if query == 'q':
            quit_status = True
            break
        guess = int(query)
        # guesses.append(guess)
    except Exception as e:
        print("Error occurred: ", e, end=" ")
        quit_status = True
        break

    guesses.append(guess)

    # Using ternary operator to reduce the lines of code
    print("Too low.") if guess < secret_number else (print("Too high.") if guess > secret_number else print("Correct!"))

    '''
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print("Correct!")
    '''

# if user quits; do not show the guesses report
if not quit_status:
    print("\nYour guesses: ", end=' ')
    for val in guesses:
        print(val, end=' ')