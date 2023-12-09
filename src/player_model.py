"""src/player_model.py"""
from panda3d.core import *


class PlayerModel:
    def __init__(self):

        # player model
        self.base.player_node = self.base.render.attachNewNode(PandaNode('player_node'))
        # head
        self.player_head_model = self.base.loader.loadModel('models/player_head')
        self.player_head_model.setScale(0.8)
        self.player_head_model.setH(180)
        self.player_head_model.setPos(0.4, 0.4, 0)
        self.base.player_head_node = self.base.player_node.attachNewNode(PandaNode('player_head_node'))
        self.base.player_head_node.setPos(0, 0, 1.2)
        self.player_head_model.reparentTo(self.base.player_head_node)
        # body
        self.player_body_model = self.base.loader.loadModel('models/player_body')
        self.player_body_model.setScale(0.8)
        self.player_body_model.setH(180)
        self.player_body_model.setPos(0.4, 0.4, 0)
        self.base.player_body_node = self.base.player_node.attachNewNode(PandaNode('player_body_node'))
        self.base.player_body_node.setPos(0, 0, 0.4)
        self.player_body_model.reparentTo(self.base.player_body_node)
        # right_hand
        self.player_right_hand_model = self.base.loader.loadModel('models/player_hand')
        self.player_right_hand_model.setScale(0.3, 0.3, 0.8)
        self.player_right_hand_model.setH(180)
        self.player_right_hand_model.setPos(0.15, 0.15, -0.7)
        self.base.player_right_hand_node = self.base.player_node.attachNewNode(PandaNode('player_right_hand_node'))
        self.base.player_right_hand_node.setPos(0.55, 0, 1.1)
        self.base.player_right_hand_node.setR(-20)
        self.base.player_right_hand_node.setP(90)
        self.player_right_hand_model.reparentTo(self.base.player_right_hand_node)
        # left_hand
        self.player_left_hand_model = self.base.loader.loadModel('models/player_hand')
        self.player_left_hand_model.setScale(0.3, 0.3, 0.8)
        self.player_left_hand_model.setH(180)
        self.player_left_hand_model.setPos(0.15, 0.15, -0.7)
        self.base.player_left_hand_node = self.base.player_node.attachNewNode(PandaNode('player_left_hand_node'))
        self.base.player_left_hand_node.setPos(-0.55, 0, 1.1)
        self.base.player_left_hand_node.setR(20)
        self.base.player_left_hand_node.setP(90)
        self.player_left_hand_model.reparentTo(self.base.player_left_hand_node)
        # right_leg
        self.player_right_leg_model = self.base.loader.loadModel('models/player_leg')
        self.player_right_leg_model.setScale(0.3, 0.3, 0.4)
        self.player_right_leg_model.setH(180)
        self.player_right_leg_model.setPos(0.15, 0.15, -0.4)
        self.base.player_right_leg_node = self.base.player_node.attachNewNode(PandaNode('player_right_leg_node'))
        self.base.player_right_leg_node.setPos(0.25, 0, 0.4)
        self.player_right_leg_model.reparentTo(self.base.player_right_leg_node)
        # left_leg
        self.player_left_leg_model = self.base.loader.loadModel('models/player_leg')
        self.player_left_leg_model.setScale(0.3, 0.3, 0.4)
        self.player_left_leg_model.setH(180)
        self.player_left_leg_model.setPos(0.15, 0.15, -0.4)
        self.base.player_left_leg_node = self.base.player_node.attachNewNode(PandaNode('player_left_leg_node'))
        self.base.player_left_leg_node.setPos(-0.25, 0, 0.4)
        self.player_left_leg_model.reparentTo(self.base.player_left_leg_node)
