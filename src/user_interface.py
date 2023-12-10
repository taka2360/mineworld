"""src/user_interface.py"""
from math import *
from time import *
from panda3d.core import *
from .utils import DrawImage, DrawText


class UserInterface:
    hotbar_blocks = [
        ['stone', ['0-1']],
        ['grass_block', ['0-3', '0-0', '0-2']],
        ['dirt', ['0-2']],
        ['white_wool', ['4-0']],
        ['blue_wool', ['11-1']],
        ['red_wool', ['8-1']],
        ['glass', ['3-1']],
        ['gold_block', ['1-7']],
        # ['diamond_block', ['1-8']],
        # ['emerald_block', ['1-9']],
        ['bricks', ['0-7']],
    ]

    def __init__(self):
        self.selected_hotbar_num = 0
        self.selected_block = UserInterface.hotbar_blocks[0]

        # draw hotbar
        for i, block in enumerate(UserInterface.hotbar_blocks):
            block_image_name = block[1][0]
            image = DrawImage(
                parent=self.a2dBottomCenter,
                image=f'textures/{block_image_name}.png',
                scale=(16 / 164, 1, 16 / 164),
                pos=((i - 4) * 0.22, 0, 20 / 164)
            )
            self.set(f'bar{i + 1}', image)
        self.hotbar = DrawImage(
            parent=self.a2dBottomCenter,
            image='images/hotbar1.png',
            scale=(1, 1, 20 / 164),
            pos=(0, 0, 20 / 164)
        )
        # text window
        how_to_use = \
            '移動: W A S D\n' \
            'アイテム選択: 123456789\n' \
            'ブロックを置く: 左クリック\n' \
            'ブロックを壊す: 右クリック\n' \
            'カメラの切り替え: T\n' \
            '操作説明を表示/非表示: X'
        self.text_window = DrawText(
            parent=self.a2dTopLeft,
            text=how_to_use,
            font=self.font,
        )

        # console window
        wellcome_text = 'Welcome to Mineworld!'
        self.console_window = DrawText(
            parent=self.a2dTopLeft,
            text=wellcome_text,
            font=self.font,
            pos=(0.05, -1.5)
        )
        self.console_window.start_time = time()  # 実行した時間を start_time に記録

        # select hotbar
        self.accept('1', self.select_hotbar, [1])
        self.accept('2', self.select_hotbar, [2])
        self.accept('3', self.select_hotbar, [3])
        self.accept('4', self.select_hotbar, [4])
        self.accept('5', self.select_hotbar, [5])
        self.accept('6', self.select_hotbar, [6])
        self.accept('7', self.select_hotbar, [7])
        self.accept('8', self.select_hotbar, [8])
        self.accept('9', self.select_hotbar, [9])

        # テキストウインドウを表示/ 非表示
        self.accept('x', self.toggle_text_window)

        # スクリーンを更新
        self.taskMgr.add(self.screen_update, "screen_update")

        # スプラッシュスクリーン
        self.splash_screen_node = self.aspect2d.attachNewNode("splash_screen_node")
        self.splash_image = DrawImage(
            parent=self.splash_screen_node,
            image='images/loading.png',
            scale=(3 / 2, 1, 1),
            pos=(0, 0, 0),
        )

        """
        loading_text = 'creating a new world...'
        loading_text = '新しい世界を創造しています...'
        self.loading_text = DrawText(
            parent=self.splash_screen_node,
            text=loading_text,
            font=self.font,
            pos=(-.2, -.5, 0),
            scale=0.1,
        )"""
        self.taskMgr.doMethodLater(3, self.close_splash_screen, "close_splash_screen")

    def select_hotbar(self, i):
        self.selected_hotbar_num = i - 1
        self.selected_block = UserInterface.hotbar_blocks[i - 1]
        self.hotbar.setImage(f'images/hotbar{i}.png')
        self.hotbar.setTransparency(TransparencyAttrib.M_alpha)

    def toggle_text_window(self):
        if self.text_window.isHidden():
            self.text_window.show()
        else:
            self.text_window.hide()

    def screen_update(self, task):
        # 3秒でコンソールの文字を消す
        if self.console_window.getText() and \
                self.console_window.start_time and time() - self.console_window.start_time > 3:
            self.console_window.setText('')
        return task.cont

    def screen_update(self, task):
        # 3秒でコンソールの文字を消す
        if self.console_window.getText() and \
                self.console_window.start_time and time() - self.console_window.start_time > 3:
            self.console_window.setText('')
        # デバッグモード
        if self.mode == 'debug':
            position = self.player.position
            direction = self.player.direction
            velocity = self.player.velocity
            text =  f'player x: {round(position[0], 1)}\n' \
                    f'player y: {round(position[1], 1)}\n' \
                    f'player z: {round(position[2], 1)}\n' \
                    f'player heading: {int(direction[0])}\n' \
                    f'player pitch: {int(direction[1])}\n' \
                    f'player roll: {int(direction[2])}\n' \
                    f'player velocity x: {round(velocity[0], 1)}\n' \
                    f'player velocity y: {round(velocity[1], 1)}\n' \
                    f'player velocity z: {round(velocity[2], 1)}\n'
            self.text_window.setText(text)
        return task.cont

    def close_splash_screen(self, task):
        self.splash_screen_node.detachNode()
        self.console_window.start_time = time()  # 実行した時間を start_time に記録
        #return task.done