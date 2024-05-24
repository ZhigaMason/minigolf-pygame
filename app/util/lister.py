import util.config as cfg

def parse_ascii_std_in() -> dict:
    mem = dict()
    for j in range(cfg.GRID_SIZE[1]):
        line = input()
        for i in range(cfg.GRID_SIZE[0]):
            char = line[i]
            if not char in mem:
                mem[char] = []
            mem[char] += [(i, j)]
    return mem

def parse_ascii_file(f) -> dict:
    mem = dict()
    for j in range(cfg.GRID_SIZE[1]):
        line = f.readline()
        for i in range(cfg.GRID_SIZE[0]):
            char = line[i]
            if not char in mem:
                mem[char] = []
            mem[char] += [(i, j)]
    return mem

if __name__ == '__main__':
    mem = parse_ascii_std_in()
    for char in mem:
        print(f'"{char}"', mem[char])
