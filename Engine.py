from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np
import random

class Voxel(Button):
    def __init__(self, position=(0,0,0), block_type='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=block_type,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.lime,
        )
        self.block_type = block_type

class World(Entity):
    def __init__(self):
        super().__init__()
        self.block_types = {
            'grass': 'grass',
            'stone': 'stone',
            'dirt': 'dirt',
            'brick': 'brick'
        }
        self.blocks = {}
        
    def add_block(self, position, block_type='grass'):
        self.blocks[position] = Voxel(position=position, block_type=block_type)
        
    def remove_block(self, position):
        if position in self.blocks:
            destroy(self.blocks[position])
            del self.blocks[position]
    
    def generate_terrain(self):
        for x in range(-8, 8):
            for z in range(-8, 8):
                self.add_block((x, 0, z), 'grass')
                if random.random() > 0.8:
                    self.add_block((x, 1, z), 'stone')