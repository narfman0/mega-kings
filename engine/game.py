"""
Platformer Game
"""
import random

import arcade

from engine.npc import NPC

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 25

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH / 3
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH / 3
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT / 4
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT / 4

PLAYER_START_X = SCREEN_WIDTH / 2
PLAYER_START_Y = SCREEN_HEIGHT / 2

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, screen_title):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, screen_title)
        # Graphical stuff
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self, player_sprite):
        # Separate variable that holds the player sprite
        self.npcs = arcade.SpriteList()
        self.terrain = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = player_sprite
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

        # Physics
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.terrain)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        self.npcs.draw()
        self.terrain.draw()
        if not self.player_sprite.fainted():
            self.player_sprite.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"x: {self.player_sprite.center_x} y: {self.player_sprite.center_y} hp: {self.player_sprite.current_hp}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if not self.player_sprite.fainted():
            if key == arcade.key.UP:
                self.moving_up = True
            if key == arcade.key.LEFT:
                self.moving_left = True
            if key == arcade.key.RIGHT:
                self.moving_right = True
            if key == arcade.key.DOWN:
                self.moving_down = True
        if key == arcade.key.R:
            self.setup()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP:
            self.moving_up = False
        if key == arcade.key.LEFT:
            self.moving_left = False
        if key == arcade.key.RIGHT:
            self.moving_right = False
        if key == arcade.key.DOWN:
            self.moving_down = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        if self.moving_up:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.moving_down:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        else:
            self.player_sprite.change_y = 0
        if self.moving_left:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.moving_right:
            self.player_sprite.change_x = MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0
        self.npcs.update()
        self.physics_engine.update()
