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

class DrawText(OnscreenText):
    def __init__(self, parent=None, text='', font=None, scale=0.07, pos=(0.05, -0.1), fg=(0, 0, 0, 1), bg=(0, 0, 0, 0.1)):
        super().__init__(
            parent=parent,
            text=text,
            align=TextNode.ALeft,
            pos=pos,
            scale=scale,
            font=font,
            fg=fg,
            bg=bg,
            mayChange=True,
        )
        self.start_time = None

class DrawMappedButton(DirectButton):
    def __init__(self, parent=None, model=None, text='', font=None, pos=(0, 0, 0), command=None, extra_args=[]):
        super().__init__(
            parent=parent,
            geom=(
                model.find('**/button_up'), model.find('**/button_press'),
                model.find('**/button_over'), model.find('**/button_disabled')
            ),
            text=text,
            text_font=font,
            pos=pos,
            command=command,
            scale=0.5,
            text_fg=(1, 1, 1, 1),
            text_scale=0.1,
            text_pos=(0, -0.04),
            relief=None,
            extraArgs=extra_args
        )
        self.initialiseoptions(DrawMappedButton)  # 全ての初期化メソッドを呼び出す


class DrawLabel(DirectLabel):
    def __init__(self, parent=None, text='', font=None, pos=(0, 0, 0), scale=0.05):
        super().__init__(
            parent=parent,
            text=text,
            text_font=font,
            pos=pos,
            scale=scale,
            text_fg=(1, 1, 1, 1),
            frameColor=(0, 0, 0, 0),
        )
        self.initialiseoptions(DrawLabel)  # 全ての初期化メソッドを呼び出す


class DrawEntry(DirectEntry):
    def __init__(self, parent=None, frame_texture=None, initial_text='', font=None, pos=(0, 0, 0), command=None):
        super().__init__(
            parent=parent,
            frameTexture=frame_texture,
            initialText=initial_text,
            text_font=font,
            pos=pos,
            command=command,
            scale=.15,
            numLines=1,
            focus=1,
            text_fg=(1, 1, 1, 1),
            text_scale=0.75,
        )
        self.initialiseoptions(DrawEntry)  # 全ての初期化メソッドを呼び出す

class DrawScrolledList(DirectScrolledList):
    def __init__(self, parent=None, model=None, frame_texture=None, pos=(0, 0, 0), scale=1, num_items_visible=1, item_height=0.1):
        super().__init__(
            parent=parent,

            decButton_pos=(0.35, 0, 0.53),
            decButton_geom=(
                model.find('**/button_up'), model.find('**/button_press'),
                model.find('**/button_over'), model.find('**/button_disabled')
            ),
            decButton_text="Up",
            decButton_scale=0.06,

            incButton_pos=(0.35, 0, -0.02),
            incButton_geom=(
                model.find('**/button_up'), model.find('**/button_press'),
                model.find('**/button_over'), model.find('**/button_disabled')
            ),
            incButton_text="down",
            incButton_scale=0.06,

            frameTexture=frame_texture,
            frameSize=(-0.5, 1.25, -0.05, 0.59),
            pos=pos,
            scale=scale,
            numItemsVisible=num_items_visible,
            forceHeight=item_height,
            #itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )
        self.initialiseoptions(DrawScrolledList)  # 全ての初期化メソッドを呼び出す