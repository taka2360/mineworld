"""11_01_main.py"""
from math import *
from src import MC


class Game(MC):
    def __init__(self):
        # MCを継承する
        MC.__init__(self, ground_size=32, mode='debug')  # 追記

        # 座標軸
        self.axis = self.loader.loadModel('models/zup-axis')
        self.axis.setPos(0, 0, 0)
        self.axis.setScale(1.5)
        self.axis.reparentTo(self.render)

        # 壁
        for i in range(5):
            for j in range(3):
                self.block.add_block(i, 5, j, 'gold_block')


game = Game()
game.run()