"""src/utils.py"""
from direct.gui.DirectGui import *
from panda3d.core import *


class DrawImage(OnscreenImage):
    def __init__(self, parent=None, image=None, scale=(1, 1, 1), pos=(0, 0, 0)):
        super().__init__(
            parent=parent,
            image=image,
            pos=pos,
            scale=scale,
        )
        self.setName(image)
        self.setTransparency(TransparencyAttrib.M_alpha)