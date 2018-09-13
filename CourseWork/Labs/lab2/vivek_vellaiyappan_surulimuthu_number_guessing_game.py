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
        print("Quitting the program...")
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


'''
Program Output of vivek_vellaiyappan_surulimuthu_number_guessing_game.py file:
For Valid Input:
Case 1: getting correct guess at last 7th guess
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  123
Guess a number 1 to 128: 1
Too low.
Guess a number 1 to 128: 2
Too low.
Guess a number 1 to 128: 4
Too low.
Guess a number 1 to 128: 5
Too low.
Guess a number 1 to 128: 6
Too low.
Guess a number 1 to 128: 34
Too low.
Guess a number 1 to 128: 45
Too low.

Your guesses:  1 2 4 5 6 34 45 
Process finished with exit code 0


Case 2: getting correct guess before exceeding guess limit
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  91
Guess a number 1 to 128: 1
Too low.
Guess a number 1 to 128: 91
Correct!

Your guesses:  1 91 
Process finished with exit code 0


Case 3: quitting the program in the middle of the game
C:\Developer\Python36\python.exe E:/kevDev/ProjectWorks/SnakeGame/gdp1/Labs/lab2/vivek_vellaiyappan_surulimuthu_number_guessing_game.py
Secret_number:  72
Guess a number 1 to 128: 1
Too low.
Guess a number 1 to 128: 2
Too low.
Guess a number 1 to 128: q
Quitting the program...

Process finished with exit code 0
'''