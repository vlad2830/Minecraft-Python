from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(FirstPersonController):
    def __init__(self, world):
        super().__init__()
        self.world = world
        self.cursor.visible = False
        self.gravity = 0.5
        self.jump_height = 2
        
    def input(self, key):
        super().input(key)
        
        # Добавление/удаление блоков
        if key == 'left mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                position = tuple(round(hit_info.entity.position[i]) for i in range(3))
                self.world.remove_block(position)
                
        if key == 'right mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=5)
            if hit_info.hit:
                position = tuple(round(hit_info.entity.position[i] + hit_info.normal[i]) for i in range(3))
                self.world.add_block(position)
