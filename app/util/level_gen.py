from .lister import parse_ascii_file
from gui.cell.floors import Grass, Ice, Sand
from gui.cell.walls import Wall, SilentWall

def generate_level(f, lvl):
    mem = parse_ascii_file(f)
    for char in mem:
        match(char):
            case '_':
                lvl.set_cells_by_type(Grass, mem[char])
            case '+':
                lvl.set_cells_by_type(Ice, mem[char])
            case '-':
                lvl.set_cells_by_type(Sand, mem[char])
            case 'X':
                lvl.set_cells_by_type(Wall, mem[char])
            case 'H':
                lvl.set_cells_by_type(SilentWall, mem[char])

if __name__ == '__main__':
    filename = input()
    with open(filename, 'r') as f:
        mem = parse_ascii_file(f)
        print(mem)
