"""
Platformer Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Mega Kings"

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

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # Separate variable that holds the player sprite
        self.player_sprite = None
        self.npcs = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Keep track of the score
        self.score = 0

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("images/npcs/dragonGreen256.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

        for i in range(5):
            img_path = "images/npcs/dragonBlack256.png" if i % 5 != 0 else "images/npcs/dragonRed.png"
            npc = arcade.Sprite(img_path, CHARACTER_SCALING)
            npc.center_x = random.randint(0, SCREEN_WIDTH)
            npc.center_y = random.randint(0, SCREEN_HEIGHT)
            self.npcs.append(npc)

        # Graphical stuff
        arcade.set_background_color(arcade.color.AMAZON)

        # Physics
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        self.npcs.draw()
        self.player_sprite.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score} x: {self.player_sprite.center_x} y: {self.player_sprite.center_y}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        if key == arcade.key.V:
            self.complete_level()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        for npc in self.npcs:
            npc.change_x += 1 if npc.center_x < self.player_sprite.center_x else -1
            npc.change_y += 1 if npc.center_y < self.player_sprite.center_y else -1
        self.npcs.update()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def distance(sprite1, sprite2):
    return math.sqrt((sprite1.center_x - sprite2.center_x)**2 + (sprite1.center_y - sprite2.center_y)**2)


def main():
    """ Main method """
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
