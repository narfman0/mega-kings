"""
Platformer Game
"""
import random

import arcade

from engine.game import *
from engine.math import distance

SCREEN_TITLE = "Unicorns and Rainbows"
NPC_COUNT = 1
PLANT_COUNT = NPC_COUNT + 1


class UnicornsAndRainbowsGame(MyGame):
    def __init__(self):
        super().__init__(SCREEN_TITLE, "images/npcs/pinkUnicornFlying256.png")
        for i in range(NPC_COUNT):
            unicorn_sprite = arcade.Sprite("images/npcs/pinkUnicornFlying256.png", CHARACTER_SCALING)
            unicorn_sprite.center_x = random.randint(0, SCREEN_WIDTH)
            unicorn_sprite.center_y = random.randint(0, SCREEN_HEIGHT)
            self.npcs.append(unicorn_sprite)
        for i in range(PLANT_COUNT):
            sprite = arcade.Sprite("images/terrain/redFlower.png", CHARACTER_SCALING)
            sprite.center_x = random.randint(0, SCREEN_WIDTH)
            sprite.center_y = random.randint(0, SCREEN_HEIGHT)
            self.terrain.append(sprite)

    def on_update(self, delta_time):
        """ Movement and game logic """
        super().on_update(delta_time)
        for npc in self.npcs:
            # npc.change_y = 1 if npc.center_y < self.player_sprite.center_y else -1
            # npc.change_x = 1 if npc.center_x < self.player_sprite.center_x else -1
            min_distance = -1
            closest_x = SCREEN_WIDTH
            closest_y = SCREEN_WIDTH
            for flower in self.terrain:
                current_distance = distance(flower, npc)
                if min_distance == -1 or current_distance < min_distance:
                    min_distance = current_distance
                    closest_x = flower.center_x
                    closest_y = flower.center_y
            npc.change_y = 1 if npc.center_y < closest_x else -1
            npc.change_x = 1 if npc.center_x < closest_y else -1


def main():
    """ Main method """
    window = UnicornsAndRainbowsGame()
    arcade.run()


if __name__ == "__main__":
    main()
