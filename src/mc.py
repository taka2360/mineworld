"""src/mc.py"""
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from . import *


class MC(ShowBase, UserInterface, Inventory, Menu):
    def __init__(self, ground_size=128, mode='normal'):  # 追記
        self.mode = mode  # 追記
        # ShowBaseを継承する
        ShowBase.__init__(self)
        self.font = self.loader.loadFont('fonts/PixelMplus12-Regular.ttf')
        UserInterface.__init__(self)
        Inventory.__init__(self)
        Menu.__init__(self)



        # ウインドウの設定
        self.properties = WindowProperties()
        self.properties.setTitle('Pynecrafter')
        self.properties.setSize(300, 200)
        self.win.requestProperties(self.properties)
        self.setBackgroundColor(0, 1, 1)

        # ブロック
        self.block = Block(self, ground_size)

        # プレイヤー
        self.player = Player(self)


        # ゲーム終了
        self.accept('escape', exit)

    def get(self, var):
        try:
            return getattr(self, var)
        except AttributeError:
            return None

    def set(self, var, val):
        setattr(self, var, val)