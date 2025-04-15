from ursina import *
from Engine import World
from InputControl import Player

class MinecraftGame:
    def __init__(self):
        self.app = Ursina()
        self.setup_window()
        self.setup_sky()
        
        self.world = World()
        self.player = Player(self.world)
        
        self.world.generate_terrain()
    
    def setup_window(self):
        window.title = 'Python Minecraft with Ursina'
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True
    
    def setup_sky(self):
        Sky()
        
    def run(self):
        self.app.run()
