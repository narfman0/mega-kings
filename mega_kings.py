import random

import arcade

from engine.game import *
from engine.math import distance
from engine.npc import NPC

SCREEN_TITLE = "Mega Kings"
NPC_COUNT = 5
ATTACK_DISTANCE = 100


class MegaKingsGame(MyGame):
    def __init__(self):
        super().__init__(SCREEN_TITLE)

    def setup(self):
        super().setup(NPC("kingkrool", hp=6000))
        for i in range(NPC_COUNT):
            npc = NPC("dragonBlack" if i % NPC_COUNT != 0 else "dragonRed", hp=2)
            npc.center_x = random.randint(0, SCREEN_WIDTH)
            npc.center_y = random.randint(0, SCREEN_HEIGHT)
            self.npcs.append(npc)

    def on_update(self, delta_time):
        """ Movement and game logic """
        super().on_update(delta_time)
        if self.player.attacking:
            self.player.attacking = False
            for npc in self.npcs:
                if distance(npc, self.player) < ATTACK_DISTANCE:
                    self.player.attack(npc)
        fainted = []
        for npc in self.npcs:
            if npc.fainted():
                npc.change_x = 0
                npc.change_x = 0
                fainted.append(npc)
                continue
            if self.player.fainted():
                npc.change_x += 1 if npc.center_x < self.player.center_x else -1
                npc.change_y += 1 if npc.center_y < self.player.center_y else -1
            else:
                npc.change_x = 1 if npc.center_x < self.player.center_x else -1
                npc.change_y = 1 if npc.center_y < self.player.center_y else -1
            if distance(npc, self.player) < ATTACK_DISTANCE:
                npc.attack(self.player)
        for fainted_npc in fainted:
            self.npcs.remove(fainted_npc)

    def on_key_press(self, key, modifiers):
        super().on_key_press(key, modifiers)
        if not self.player.fainted():
            if key == arcade.key.A:
                self.player.attacking = True


def main():
    """ Main method """
    window = MegaKingsGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
