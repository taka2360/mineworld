"""03_04_egg_model_viewer.py"""
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *


class App(ShowBase):
    # コンストラクタ
    def __init__(self):
        # ShowBaseを継承する
        ShowBase.__init__(self)

        # textured cube
        blocks = {
            # blocks_1
            'stone': ['0-1'],
            'dirt': ['0-2'],
            'bricks': ['0-7'],
            'cobblestone': ['1-0'],
            'bedrock': ['1-1'],
            'sand': ['1-2'],
            'iron_block': ['1-6'],
            'gold_block': ['1-7'],
            'diamond_block': ['1-8'],
            'emerald_block': ['1-9'],
            'gold_ore': ['2-0'],
            'iron_ore': ['2-1'],
            'coal_ore': ['2-2'],
            'mossy_cobblestone': ['2-4'],
            'obsidian': ['2-5'],
            'sponge': ['3-0'],
            'glass': ['3-1'],
            'diamond_ore': ['3-2'],
            'redstone_ore': ['3-3'],
            'oak_leaves': ['3-4'],
            'oak_plants': ['0-4'],
            'stone_bricks': ['3-6'],
            'lava': ['3-21'],
            'water': ['3-22'],
            'white_wool': ['4-0'],
            'mob_spawner': ['4-1'],
            'snow': ['4-2'],
            'ice': ['4-3'],
            'black_wool': ['7-1'],
            'gray_wool': ['7-2'],
            'red_wool': ['8-1'],
            'pink_wool': ['8-2'],
            'lapis_block': ['9-0'],
            'green_wool': ['9-1'],
            'lime_wool': ['9-2'],
            'lapis_ore': ['10-0'],
            'brown_wool': ['10-1'],
            'yellow_wool': ['10-2'],
            'blue_wool': ['11-1'],
            'cyan_wool': ['11-2'],
            'purple_wool': ['12-1'],
            'magenta_wool': ['12-2'],
            'spruce_planks': ['12-6'],
            'jungle_planks': ['12-7'],
            'light_blue_wool': ['13-1'],
            'orange_wool': ['13-2'],
            'birch_planks': ['13-6'],
            'light_gray_wool': ['14-1'],
            'target_block': ['target_block'],  # 追記
            # blocks_1_5
            'oak_log': ['1-4', '1-5'],
            'bookshelf': ['2-3', '0-4'],
            'crafting_table': ['3-11', '2-11'],
            'cactus': ['4-5', '4-6'],
            'jukebox': ['4-10', '4-11'],
            'spruce_log': ['7-4', '1-5'],
            'binch_log': ['7-5', '1-5'],
            'jungle_log': ['9-9', '1-5'],
            # blocks_1_5_6
            'grass_block': ['0-3', '0-0', '0-2'],
            'tnt': ['0-8', '0-9', '0-10'],
            'sticky_piston': ['6-12', '6-10', '6-13'],
            'piston': ['6-12', '6-11', '6-13'],
            # blocks_1_2_5
            'furnace': ['2-12', '2-13', '3-14'],
            'burning_furnace': ['3-13', '2-13', '3-14'],
            'chest': ['6-19', '6-18', '6-17'],
            'pumpkin': ['7-7', '7-6', '6-6'],
            'jack_o_lantern': ['7-8', '7-6', '6-6'],
            # blocks_1_2_3_4_5_6
            'player_head': ['head/1', 'head/2', 'head/3', 'head/4', 'head/5', 'head/6'],
            'player_body': ['body/1', 'body/2', 'body/3', 'body/4', 'body/5', 'body/6'],
            'player_hand': ['hand/1', 'hand/2', 'hand/3', 'hand/4', 'hand/5', 'hand/6'],
            'player_leg': ['leg/1', 'leg/2', 'leg/3', 'leg/4', 'leg/5', 'leg/6'],
        }

        for i, name in enumerate(blocks):
            self.cube = self.loader.loadModel(f'models/{name}')
            self.cube.setPos(i % 10 - 5, 30, int(i / 10) * 2 - 7)
            self.cube.reparentTo(self.render)


app = App()
app.run()