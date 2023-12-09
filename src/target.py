"""src/target.py"""
from math import *
from panda3d.core import *


class Target:

    # コンストラクタ
    def __init__(self):
        self.target_node = self.base.render.attachNewNode(PandaNode('target_node'))
        self.target_block_model = self.base.loader.loadModel('models/target_block')
        self.target_block_model.reparentTo(self.target_node)

        self.base.taskMgr.add(self.set_target_block, "set_target_block")


    def get_target_position(self):
        x0, y0, z0 = self.position
        phi, theta, _ = self.direction
        # print(x0, y0, z0, phi, theta)
        # 方向ベクトル
        direction_vec = Vec3(
            sin(radians(90 - theta)) * cos(radians(phi + 90)),
            sin(radians(90 - theta)) * sin(radians(phi + 90)),
            cos(radians(90 - theta))
        )
    
        if not theta == 0:
            if theta < 0:
                check_heights = [1, 0]
            else:
                check_heights = [2, 3, 4, 5, 6, 7, 8]
            for check_height in check_heights:
                z = check_height
                x = x0 + (z - z0 - self.eye_height) * direction_vec.x / direction_vec.z
                y = y0 + (z - z0 - self.eye_height) * direction_vec.y / direction_vec.z
                # print(x, y)
                target_position = Point3(x, y, z)
                if (target_position - Point3(x0, y0, z0 + self.eye_height)).length() < 8 and \
                        self.base.block.can_add_or_remove_block_at(target_position):
                    return Point3(x, y, z)
            else:
                return None
        else:
            return None

    def set_target_block(self, task):
        self.target_position = self.get_target_position()
        if self.target_position:
            if self.target_node.isHidden():
                self.target_node.show()
            self.target_node.setPos(
                floor(self.target_position.x),
                floor(self.target_position.y),
                floor(self.target_position.z),
            )
        else:
            if not self.target_node.isHidden():
                self.target_node.hide()
        return task.cont