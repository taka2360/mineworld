"""main.py"""
from math import *
from src import MC


class Game(MC):
    def __init__(self):
        # MCを継承する
        MC.__init__(self, ground_size=32)


game = Game()
game.run()