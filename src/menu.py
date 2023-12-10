"""src/menu.py"""
from panda3d.core import *
from .utils import *


class Menu:
    def __init__(self):
        self.menu_node = self.aspect2d.attachNewNode('menu_node')
        self.menu_node.stash()
        self.save_node = self.aspect2d.attachNewNode('save_node')
        self.save_node.stash()
        self.load_node = self.aspect2d.attachNewNode('load_node')
        self.load_node.stash()

        menu_cm = CardMaker('menu_card')
        menu_cm.setFrame(-1.5, 1.5, -1, 1)
        self.menu_background_node = self.render2d.attachNewNode(menu_cm.generate())
        self.menu_background_node.setTransparency(1)
        self.menu_background_node.setColor(0, 0, 0, 0.5)
        self.menu_background_node.stash()

        self.button_model = self.loader.loadModel('models/button_maps')
        self.frame_texture = self.loader.loadTexture('textures/buttons/button_up.png')

        # Menu Screen
        self.resume_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='ゲームに戻る',
            font=self.font,
            pos=(0, 0, 0.4),
            command=self.toggle_menu
        )
        self.save_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='ゲームをセーブ',
            font=self.font,
            pos=(0, 0, 0.24),
            command=self.toggle_save
        )
        self.load_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='ゲームをロード',
            font=self.font,
            pos=(0, 0, 0.08),
            command=self.toggle_load
        )
        self.server_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='サーバーを開始',
            font=self.font,
            pos=(0, 0, -0.08),
            command=self.open_server
        )
        self.join_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='サーバーに接続',
            font=self.font,
            pos=(0, 0, -0.24),
            command=self.join_server
        )
        self.exit_button = DrawMappedButton(
            parent=self.menu_node,
            model=self.button_model,
            text='ゲームを終了',
            font=self.font,
            pos=(0, 0, -0.4),
            command=exit
        )

        # Save Screen
        self.save_input_field = DrawEntry(
            parent=self.save_node,
            frame_texture=self.frame_texture,
            initial_text='My World',
            font=self.font,
            pos=(-0.6, 0, 0.1),
            command=self.save_world,
        )
        self.save_text = DrawLabel(
            parent=self.save_node,
            text='セーブする「ワールドの名前」を入力',
            font=self.font,
            pos=(0, 0, 0.35),
            scale=0.075
        )
        self.save_notification_text = DrawLabel(
            parent=self.save_node,
            text='',
            font=self.font,
            pos=(0, 0, -0.45),
            scale=0.06
        )
        self.save_button = DrawMappedButton(
            parent=self.save_node,
            model=self.button_model,
            text='セーブする',
            font=self.font,
            pos=(0, 0, -0.1),
            command=self.save_world
        )
        self.save_back_button = DrawMappedButton(
            parent=self.save_node,
            model=self.button_model,
            text='メニューに戻る',
            font=self.font,
            pos=(0, 0, -0.25),
            command=self.toggle_save
        )

        # Load Screen
        self.load_list = DrawScrolledList(
            parent=self.load_node,
            model=self.button_model,
            frame_texture=self.frame_texture,
            pos=(-0.45, 5, -0.25),
            scale=1.25,
            num_items_visible=3,
            item_height=0.15,
        )
        self.load_text = DrawLabel(
            parent=self.load_node,
            text='ロードする「ワールドの名前」を選ぶ',
            font=self.font,
            pos=(0, 0, 0.55),
            scale=0.075
        )
        self.load_notification_text = DrawLabel(
            parent=self.load_node,
            text='',
            font=self.font,
            pos=(0, 0, -0.7),
            scale=0.075
        )
        self.load_back_button = DrawMappedButton(
            parent=self.load_node,
            model=self.button_model,
            text='メニューに戻る',
            font=self.font,
            pos=(0, 0, -0.5),
            command=self.toggle_load
        )

        # ユーザー操作
        self.accept('q', self.toggle_menu)

    def toggle_menu(self):
        if self.menu_node.isStashed():
            self.menu_node.unstash()
            self.menu_background_node.unstash()
        else:
            self.menu_node.stash()
            self.menu_background_node.stash()

    def toggle_save(self):
        if self.save_node.isStashed():
            self.menu_node.stash()
            self.save_node.unstash()
            self.save_notification_text.setText('')
        else:
            self.menu_node.unstash()
            self.save_node.stash()

    def toggle_load(self):
        if self.load_node.isStashed():
            self.menu_node.stash()
            self.load_node.unstash()
            self.load_notification_text.setText('')
        else:
            self.menu_node.unstash()
            self.load_node.stash()

    def save_world(self):
        pass

    def load_world(self):
        pass
            
    def open_server(self):
        pass
            
    def join_server(self):
        pass