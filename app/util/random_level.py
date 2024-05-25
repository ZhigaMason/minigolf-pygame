""" Generates text for 10th level """
import random

CHARS = ['X', 'H', '-', '_']
def rand_char():
    """ Returns random char for level generating """
    return CHARS[random.randint(0, 3)]
if __name__ == '__main__':
    GRID_SIZE = 40, 30

    print('X' * GRID_SIZE[0])
    for i in range(1, GRID_SIZE[1] - 1):
        print('X', end='')
        for j in range(1, GRID_SIZE[0] - 1):
            print( rand_char() if i % 2 == 0 == j % 2 else '+' , end='')
        print('X')

    print('X' * GRID_SIZE[0])
