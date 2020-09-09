import arcade

import random

class NPC(arcade.Sprite):
    def __init__(self, player_sprite_path, scaling_factor, hp=1, attack_stat=1, defense_stat=0):
        super().__init__(player_sprite_path, scaling_factor)
        self.hp = hp
        self.current_hp = hp
        self.defense_stat = defense_stat
        self.attack_stat = attack_stat
        self.attacking = False

    def attack(self, opponent):
        opponent.current_hp = max(0, opponent.current_hp - (self.attack_stat - opponent.defense_stat))
    
    def fainted(self):
        return self.current_hp <= 0