"""src/player.py"""
from math import *
from panda3d.core import *
from direct.showbase.ShowBaseGlobal import globalClock
from .player_model import PlayerModel
from .camera import Camera
from .target import Target  # 追記


class Player(PlayerModel, Camera, Target):  # 追記
    heading_angular_velocity = 15000
    pitch_angular_velocity = 5000
    max_pitch_angle = 60
    speed = 10
    eye_height = 1.6  # 追記

    # コンストラクタ
    def __init__(self, base):
        self.base = base
        PlayerModel.__init__(self)
        Camera.__init__(self)
        Target.__init__(self)  # 追記


        self.position = Point3(0, 0, 0)
        self.direction = VBase3(0, 0, 0)
        self.velocity = Vec3(0, 0, 0)
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        self.target_position = None  # 追記

        # キー操作を保存
        self.key_map = {
            'w': 0,
            'a': 0,
            's': 0,
            'd': 0,
        }

        # ユーザーのキー操作
        base.accept('w', self.update_key_map, ["w", 1])
        base.accept('a', self.update_key_map, ["a", 1])
        base.accept('s', self.update_key_map, ["s", 1])
        base.accept('d', self.update_key_map, ["d", 1])
        base.accept('w-up', self.update_key_map, ["w", 0])
        base.accept('a-up', self.update_key_map, ["a", 0])
        base.accept('s-up', self.update_key_map, ["s", 0])
        base.accept('d-up', self.update_key_map, ["d", 0])
        base.accept('mouse1', self.player_remove_block)  # 追記
        base.accept('mouse3', self.player_add_block)  # 追記

        # プレイヤーのアップデート
        base.taskMgr.add(self.player_update, "player_update")

    def update_direction(self):
        if self.base.mouseWatcherNode.hasMouse() and self.base.inventory_node.isStashed() and self.base.menu_background_node.isStashed():
            dt = globalClock.getDt()
            x, y = self.base.mouseWatcherNode.getMouse()
            dx = x - self.mouse_pos_x
            dy = y - self.mouse_pos_y
            if dx or dy:
                heading = self.direction.x - dx * Player.heading_angular_velocity * dt
                pitch = self.direction.y + dy * Player.pitch_angular_velocity * dt
                if pitch < -Player.max_pitch_angle:
                    pitch = -Player.max_pitch_angle
                elif pitch > Player.max_pitch_angle:
                    pitch = Player.max_pitch_angle
                self.direction = VBase3(heading, pitch, 0)
                self.mouse_pos_x = x
                self.mouse_pos_y = y

    def update_key_map(self, key_name, key_state):
        self.key_map[key_name] = key_state

    def update_velocity(self):
        key_map = self.key_map

        if key_map['w'] or key_map['a'] or key_map['s'] or key_map['d']:
            heading = self.direction.x
            if key_map['w'] and key_map['a']:
                angle = 135
            elif key_map['a'] and key_map['s']:
                angle = 225
            elif key_map['s'] and key_map['d']:
                angle = 315
            elif key_map['d'] and key_map['w']:
                angle = 45
            elif key_map['w']:
                angle = 90
            elif key_map['a']:
                angle = 180
            elif key_map['s']:
                angle = 270
            else:  # key_map['d']
                angle = 0
            self.velocity = \
                Vec3(
                    cos(radians(angle + heading)),
                    sin(radians(angle + heading)),
                    0
                ) * Player.speed
        else:
            self.velocity = Vec3(0, 0, 0)

    def update_position(self):
        self.update_velocity()
        dt = globalClock.getDt()
        self.position = self.position + self.velocity * dt
        # print(self.position)

    def draw(self):
        self.base.player_node.setH(self.direction.x)
        self.base.player_head_node.setP(self.direction.y)
        self.base.player_node.setPos(self.position)

    def player_update(self, task):
        self.update_direction()
        self.update_position()
        self.draw()
        return task.cont

    def player_add_block(self):
        block_id = self.base.hotbar_blocks[self.base.selected_hotbar_num][0]
        if self.target_position and \
                not self.base.block.is_block_at(self.target_position):
            self.base.block.add_block(
                self.target_position.x,
                self.target_position.y,
                self.target_position.z,
                block_id
            )

    def player_remove_block(self):
        if self.target_position and \
                self.base.block.is_block_at(self.target_position):
            self.base.block.remove_block(
                self.target_position.x,
                self.target_position.y,
                self.target_position.z
            )