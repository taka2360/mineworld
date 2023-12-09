"""src/block.py"""
from math import *
from panda3d.core import *


class Block:
    def __init__(self, base, ground_size):
        self.base = base
        self.ground_size = ground_size
        self.block_dictionary = {}

        # グラウンドを作成
        self.set_flat_world()

    def add_block_dictionary(self, x, y, z, block_id):
        key = f'{floor(x)}_{floor(y)}_{floor(z)}'
        self.block_dictionary[key] = block_id

    def add_block_model(self, x, y, z, block_id):
        key = f'{floor(x)}_{floor(y)}_{floor(z)}'
        self.base.set(key, self.base.render.attachNewNode(PandaNode(key)))
        placeholder = self.base.get(key)
        placeholder.setPos(floor(x), floor(y), floor(z))
        block = self.base.loader.loadModel(f'models/{block_id}')
        block.reparentTo(placeholder)

    def add_block(self, x, y, z, block_id):
        self.add_block_dictionary(x, y, z, block_id)
        self.add_block_model(x, y, z, block_id)

    def remove_block_dictionary(self, x, y, z):
        key = f'{floor(x)}_{floor(y)}_{floor(z)}'
        if key in self.block_dictionary:
            del self.block_dictionary[key]

    def remove_block_model(self, x, y, z):
        key = f'{floor(x)}_{floor(y)}_{floor(z)}'
        placeholder = self.base.get(key)
        if placeholder:
            placeholder.removeNode()

    def remove_block(self, x, y, z):
        self.remove_block_dictionary(x, y, z)
        self.remove_block_model(x, y, z)

    def set_flat_world(self):
        ground_size = self.ground_size
        for i in range(ground_size):
            for j in range(ground_size):
                x = i - ground_size // 2
                y = j - ground_size // 2
                z = -1
                self.add_block(x, y, z, 'grass_block')

    def is_block_at(self, position):
        x, y, z = [floor(value) for value in position]
        key = f'{x}_{y}_{z}'
        return key in self.block_dictionary

    def can_add_or_remove_block_at(self, position):
        diff_positions = [
            Point3(1, 0, 0),
            Point3(0, 1, 0),
            Point3(0, 0, 1),
            Point3(-1, 0, 0),
            Point3(0, -1, 0),
            Point3(0, 0, -1),
        ]

        for diff_position in diff_positions:
            x, y, z = [floor(value) for value in position + diff_position]
            key = f'{x}_{y}_{z}'
            if key in self.block_dictionary:
                return True
        else:
            return False