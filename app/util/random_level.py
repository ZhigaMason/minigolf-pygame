import random

GRID_SIZE = 40, 30
ary = ['X', 'H', '-', '_']
def rand_char():
    return ary[random.randint(0, 3)]

print('X' * GRID_SIZE[0])
for i in range(1, GRID_SIZE[1] - 1):
    print('X', end='')
    for j in range(1, GRID_SIZE[0] - 1):
        print( rand_char() if i % 2 == 0 == j % 2 else '+' , end='')
    print('X')

print('X' * GRID_SIZE[0])
