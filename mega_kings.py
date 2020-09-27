import random

import arcade

from engine.game import *
from engine.math import distance
from engine.npc import NPC, ATTACK_DISTANCE

SCREEN_TITLE = "Mega Kings"
NPC_COUNT = 5


class MegaKingsGame(MyGame):
    def __init__(self):
        super().__init__(SCREEN_TITLE)

    def setup(self):
        super().setup(NPC("bossBrolder", hp=6000))
        for i in range(NPC_COUNT):
            npc = NPC("kingkrool", hp=2)
            npc.center_x = random.randint(0, SCREEN_WIDTH)
            npc.center_y = random.randint(0, SCREEN_HEIGHT)
            self.npcs.append(npc)
        npc = NPC("dryBowser", hp=30)
        npc.center_x = SCREEN_WIDTH
        npc.center_y = SCREEN_HEIGHT
        self.npcs.append(npc)
        self.do_attack = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        super().on_update(delta_time)
        if self.do_attack:
            self.do_attack = False
            self.player.attack(self.npcs)

        for npc in self.npcs:
            if npc.fainted():
                npc.change_x = 0
                npc.change_x = 0
                npc.remove_from_sprite_lists()
                continue
            if self.player.fainted():
                npc.change_x += 1 if npc.center_x < self.player.center_x else -1
                npc.change_y += 1 if npc.center_y < self.player.center_y else -1
            else:
                npc.change_x = 1 if npc.center_x < self.player.center_x else -1
                npc.change_y = 1 if npc.center_y < self.player.center_y else -1
            if distance(npc, self.player) < ATTACK_DISTANCE:
                npc.attack([self.player])

    def on_key_press(self, key, modifiers):
        super().on_key_press(key, modifiers)
        if key == arcade.key.A:
            self.do_attack = True


def main():
    """ Main method """
    window = MegaKingsGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
