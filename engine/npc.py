import arcade

import random

class NPC(arcade.Sprite):
    def __init__(self, player_sprite_path, scaling_factor, hp=1, attack=10, defense=10):
        super().__init__(player_sprite_path, scaling_factor)
        self.hp = hp
        self.current_hp = hp
        self.defense = defense
        self.attack = attack
        self.attacking = False
    
    def fainted(self):
        return self.current_hp <= 0