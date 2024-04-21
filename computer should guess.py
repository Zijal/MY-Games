import random

print('Chose a number and I try to guess it ;)')
TheNum = input('please enter ur number: ')

a = 1
b = 100
hads = random.randint(a, b)

print('My guess is : ', hads)

check = input('Is the guess T: true, B: bigger or S: smaller? ')
while check != 'T':
    if check == 'B':
        b = hads
        hads = random.randint(a, hads)
        print('My guess is : ', hads)

    elif check == 'S':
        a = hads
        hads = random.randint(hads, b)
        print('My guess is : ', hads)
    check = input('Is the guess T: true, B: bigger or S: smaller? ')


print('I got itttt!!!')


