#The Guessing Game.
import random

guesses_made = 0

name = input('Hello! What is you name:')

print(name + ' lats play game')

x = (random.randint(1, 10))

while guesses_made < 3:
    y = int(input('Please choose your number:'))
    guesses_made += 1
    if y > x:
        print('Your number is greater')
    if y < x:
        print('Your number is less')
    if y == x:
        print('You win!')
        break
else:
    print('You lose. Be lucky next time:)')
