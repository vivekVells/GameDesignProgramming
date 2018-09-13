'''
Questions:
- aim was to reduce the lines of code; but ended up with more lines because of explanation quotes
- best practices!
Output: Please refer this at the end of this program
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
            print("Quitting the program...")
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


# if user quits; do not show the guesses report
if not quit_status:
    print("\nYour guesses: ", end=' ')
    for val in guesses:
        print(val, end=' ')


''' 
Program Output:
For Valid Input:
Case 1: getting correct guess at last 7th guess
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/best_coding_practices_vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  46
Guess a number 1 to 128: 1
Too low.
Guess a number 1 to 128: 45
Too low.
Guess a number 1 to 128: 50
Too high.
Guess a number 1 to 128: 28
Too low.
Guess a number 1 to 128: 120
Too high.
Guess a number 1 to 128: 46
Correct!

Your guesses:  1 45 50 28 120 46 
Process finished with exit code 0

Case 2: getting correct guess before exceeding guess limit
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/best_coding_practices_vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  25
Guess a number 1 to 128: 20
Too low.
Guess a number 1 to 128: 26
Too high.
Guess a number 1 to 128: 25
Correct!

Your guesses:  20 26 25 
Process finished with exit code 0

Case 3: quitting the program in the middle of the game
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/best_coding_practices_vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  35
Guess a number 1 to 128: 20
Too low.
Guess a number 1 to 128: 40
Too high.
Guess a number 1 to 128: q
Quitting the program...

Process finished with exit code 0

For Invalid Input: (use defensive programming)
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/best_coding_practices_vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  10
Guess a number 1 to 128: a
Error occurred:  invalid literal for int() with base 10: 'a' 
Process finished with exit code 0
'''