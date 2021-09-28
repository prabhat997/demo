import random

n=(random.randint(1,10))
guess_count = 0
guess_limit=4
print('you have 5 chances:')
while (guess_limit<=4):
    guess_number=int(input('guess the number:\n'))
    guess_limit -= 1
    if guess_number > n:
          print('insert lower number')

    elif guess_number < n:
        print('insert higher number')
    elif guess_limit == 0:
        print('out')
    else:
        print('correct')
        break
    print(f'you have {guess_limit} chances')

