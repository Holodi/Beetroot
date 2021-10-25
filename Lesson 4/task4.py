#The math quiz program

from random import randint

x = (randint(1, 1000))
y = (randint(1, 1000))

answer = int(input(f'Привіт! Будь ласка допоможи мені вирішити рівняння. Скільки буде, {x}+{y}:'))
if answer == x+y:
    print('Правильно!')
else:
    print(f'Неправильно, правильна відповідь {x+y}')



