"""
    Module that has functions to parse text into dictionary, that level generator can use
"""
import util.config as cfg

def parse_ascii_std_in() -> dict:
    """ Parses text from standard input, is used CLI """
    mem = {}
    for j in range(cfg.GRID_SIZE[1]):
        line = input()
        for i in range(cfg.GRID_SIZE[0]):
            char = line[i]
            if not char in mem:
                mem[char] = []
            mem[char] += [(i, j)]
    return mem

def parse_ascii_file(f) -> dict:
    """ Parses text from given file """
    mem = {}
    for j in range(cfg.GRID_SIZE[1]):
        line = f.readline()
        for i in range(cfg.GRID_SIZE[0]):
            char = line[i]
            if not char in mem:
                mem[char] = []
            mem[char] += [(i, j)]
    return mem

if __name__ == '__main__':
    d = parse_ascii_std_in()
    for c, l in d.items():
        print(f'"{c}"', l)
