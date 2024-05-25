""" Generates level from given file """
from gui.cell.floors import Grass, Ice, Sand
from gui.cell.walls import Wall, SilentWall
from .lister import parse_ascii_file

def generate_level(f, lvl):
    """ Puts level from file (f) into level (level) """

    mem = parse_ascii_file(f)
    for char, l in mem.items():
        match(char):
            case '_':
                lvl.set_cells_by_type(Grass, l)
            case '+':
                lvl.set_cells_by_type(Ice, l)
            case '-':
                lvl.set_cells_by_type(Sand, l)
            case 'X':
                lvl.set_cells_by_type(Wall, l)
            case 'H':
                lvl.set_cells_by_type(SilentWall, l)

if __name__ == '__main__':
    filename = input()
    with open(filename, 'r', encoding='utf-8') as file:
        d = parse_ascii_file(file)
        print(d)
