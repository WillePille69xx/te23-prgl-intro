from random import randint

guess = 0
answer = randint(1, 10)

while guess /= answer:
guess = int(input("guess a number between 1 and 10: "))
if guess > answer:
    print("You guessed to high!")
elif guess < answer:
    print("You guessed to low!")
else:
    print("You won!")

