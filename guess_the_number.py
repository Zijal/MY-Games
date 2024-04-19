import random
The_Number = random.randint(1, 99)

print(The_Number)

hads = int(input('Please enter ur guess: '))

while The_Number != hads:
    if The_Number > hads:
        print('chosen number is BIGGER!')

    elif The_Number < hads:
        print('chosen number is SMALLER')

    hads = int(input('please enter ur guess: '))


print('GOOD JOB!!! U GOT IT :)))')
