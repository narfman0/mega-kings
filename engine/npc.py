import arcade

import random

from engine.animated_sprite import AnimatedSprite

ANIMATION_TUPLES = {
    "kingkrool": [("idle", 4), ("walk", 8)],
    "pinkie": [("idle", 2), ("walk", 9)],
}
ANIMATION_DEFAULT = [("idle", 1)]


class NPC(AnimatedSprite):
    def __init__(self, sprite_name, hp=1, attack_stat=1, defense_stat=0):
        super().__init__(
            sprite_name, ANIMATION_TUPLES.get(sprite_name, ANIMATION_DEFAULT)
        )
        self.hp = hp
        self.current_hp = hp
        self.defense_stat = defense_stat
        self.attack_stat = attack_stat
        self.attacking = False

    def attack(self, opponent):
        opponent.current_hp = max(
            0, opponent.current_hp - (self.attack_stat - opponent.defense_stat)
        )

    def fainted(self):
        return self.current_hp <= 0

    def update(self):
        super().update()
        if (
            self.has_animation("walk")
            and (self.change_x != 0 or self.change_y != 0)
            and self.current_animation_name != "walk"
        ):
            self.set_animation("walk")
        elif (
            self.change_x == 0
            and self.change_y == 0
            and self.current_animation_name != "idle"
        ):
            self.set_animation("idle")
