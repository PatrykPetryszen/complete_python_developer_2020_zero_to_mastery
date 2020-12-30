from random import randint
import sys

answer = randint(1, 10)

while True:
    try:
        guess = int(input('guess a number 1-10:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('I said 1-10')
    except ValueError:
        print('please enter a number')
        continue
