"""src/inventory.py"""
from panda3d.core import *
from direct.gui.DirectGui import *
from .utils import *


class Inventory:
    inventory_blocks = [
        ['stone', ['0-1']],
        ['grass_block', ['0-3', '0-0', '0-2']],
        ['dirt', ['0-2']],
        ['cobblestone', ['1-0']],
        ['oak_planks', ['0-4']],
        ['bedrock', ['1-1']],
        ['water', ['3-22']],
        ['lava', ['3-21']],
        ['sand', ['1-2']],
        ['oak_log', ['1-4', '1-5']],
        ['oak_leaves', ['3-4']],
        ['glass', ['3-1']],
        ['white_wool', ['4-0']],
        ['orange_wool', ['13-2']],
        ['magenta_wool', ['12-2']],
        ['light_blue_wool', ['13-1']],
        ['yellow_wool', ['10-2']],
        ['lime_wool', ['9-2']],
        ['pink_wool', ['8-2']],
        ['gray_wool', ['7-2']],
        ['light_gray_wool', ['14-1']],
        ['cyan_wool', ['11-2']],
        ['purple_wool', ['12-1']],
        ['blue_wool', ['11-1']],
        ['brown_wool', ['10-1']],
        ['green_wool', ['9-1']],
        ['red_wool', ['8-1']],
        ['black_wool', ['7-1']],
        ['gold_block', ['1-7']],
        ['iron_block', ['1-6']],
        ['diamond_block', ['1-8']],
        ['emerald_block', ['1-9']],
        ['lapis_block', ['9-0']],
        ['bricks', ['0-7']],
        ['tnt', ['0-8', '0-9', '0-10']],
        ['bookshelf', ['2-3', '0-4']],
        ['furnace', ['2-12', '2-13', '3-14']],
        ['burning_furnace', ['3-13', '2-13', '3-14']],
        ['piston', ['6-12', '6-11', '6-13']],
        ['snow', ['4-2']],
        ['ice', ['4-3']],
        ['cactus', ['4-5', '4-6']],
        ['jack_o_lantern', ['7-8', '7-6', '6-6']],
        ['chest', ['6-19', '6-18', '6-17']],
    ]

    def __init__(self):
        self.inventory_node = self.aspect2d.attachNewNode("inventory_node")

        # background
        cm = CardMaker('inventory_card')
        cm.setFrame(-1.5, 1.5, -1, 1)
        self.inventory_background = self.inventory_node.attachNewNode(cm.generate())
        self.inventory_background.setTransparency(1)
        self.inventory_background.setColor(0, 0, 0, 0.5)

        # frame
        self.frame = DrawImage(
            parent=self.inventory_node,
            image='images\inventory.png',
            scale=(11 / 9, 11 / 9, 74 * 11 / 200 / 9),
            pos=(0, 0, 0),
        )

        # buttons
        for i, block in enumerate(Inventory.inventory_blocks):
            block_image_name = block[1][0]
            row_num = i // 11
            column_num = i % 11
            button = DirectButton(
                image=f'textures/{block_image_name}.png',
                parent=self.inventory_node,
                scale=(16 / 164, 1, 16 / 164),
                pos=((column_num - 5) * 0.22, 0, - 0.11 - (row_num - 2) * 0.22),
                relief=None,  # ボタンを持ち上げて表示しない
                command=self.select_inventory_block,
                extraArgs=[i],
            )
            button.setTransparency(TransparencyAttrib.MAlpha)
        # インベントリを非表示
        self.inventory_node.stash()

        # インベントリを表示
        self.accept('e', self.toggle_inventory)

    def toggle_inventory(self):
        if self.inventory_node.isStashed():
            self.inventory_node.unstash()
        else:
            self.inventory_node.stash()

    def select_inventory_block(self, i):
        selected_block = Inventory.inventory_blocks[i]
        block_image_name = selected_block[1][0]
        hotbar_num = self.selected_hotbar_num
        self.hotbar_blocks[hotbar_num] = selected_block
        bar_num = hotbar_num + 1
        bar_image = self.get(f'bar{bar_num}')
        bar_image.setImage(
            f'textures/{block_image_name}.png'
        )
        bar_image.setTransparency(TransparencyAttrib.M_alpha)