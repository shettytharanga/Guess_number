import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        print(f"guess a number between 1 and {x} : ")
        guess = int(input())
        if guess < random_number:
            print("sorry, your guess is too low !" )
        elif guess > random_number:
            print("sorry, your guess is too high !")
    print(f"yayy ! congrats , you have guesses the number {random_number} correctly !! ")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could also be high because low = high .
        feedback = input(f"is the {guess} too high (H), too low (L) or correct (C) ?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"yaaayy !! the computer has guessed the number {guess} correctly. ! ")

computer_guess(90)