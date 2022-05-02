from lceb.generator import new_game
from lceb.solver import runit

if __name__ == '__main__':
    game = new_game()
    res = runit(game)
    print(game)
    print(res)
