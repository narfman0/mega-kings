"""
Platformer Game
"""
import random

import arcade

from engine.game import *

SCREEN_TITLE = "Mega Kings"
NPC_COUNT = 5


class MegaKingsGame(MyGame):
    def __init__(self):
        super().__init__(SCREEN_TITLE, "images/npcs/dragonGreen256.png")
        for i in range(NPC_COUNT):
            img_path = "images/npcs/dragonBlack256.png" if i % NPC_COUNT != 0 else "images/npcs/dragonRed.png"
            npc = arcade.Sprite(img_path, CHARACTER_SCALING)
            npc.center_x = random.randint(0, SCREEN_WIDTH)
            npc.center_y = random.randint(0, SCREEN_HEIGHT)
            self.npcs.append(npc)

    def on_update(self, delta_time):
        """ Movement and game logic """
        super().on_update(delta_time)
        for npc in self.npcs:
            npc.change_x += 1 if npc.center_x < self.player_sprite.center_x else -1
            npc.change_y += 1 if npc.center_y < self.player_sprite.center_y else -1


def main():
    """ Main method """
    window = MegaKingsGame()
    arcade.run()


if __name__ == "__main__":
    main()
