import config as cfg

mem = dict()
for j in range(cfg.GRID_SIZE[1]):
    line = input()
    for i in range(cfg.GRID_SIZE[0]):
        char = line[i]
        if not char in mem:
            mem[char] = []
        mem[char] += [(i, j)]

for char in mem:
    print(f'"{char}"', mem[char])
