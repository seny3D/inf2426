import random
b: int = 0
with open('input.txt', 'w') as file:
    for x in range(19):
        file.write(f'{x} {x + 1}\n')
        b += 1
    file.write(f'{b} {0}\n')

