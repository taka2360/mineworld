"""src/mc.py"""
import sys
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from . import *


class MC(ShowBase, UserInterface):
    def __init__(self, ground_size=128):
        # ShowBaseを継承する
        ShowBase.__init__(self)
        UserInterface.__init__(self)
        # ウインドウの設定
        self.properties = WindowProperties()
        self.properties.setTitle('Mineworld')
        self.properties.setSize(600, 400)
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