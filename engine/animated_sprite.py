"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import os

CHARACTER_SCALING = 1

MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 7

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename),
        # TODO(narfman0): flipped_horizontally=True
    ]


class AnimatedSprite(arcade.Sprite):
    def __init__(self, sprite_name, animation_name_frames_tuples=[("idle", 1)]):
        """ sprite_name folder containing sprite, e.g. kingkrool
        animation_name_frames_tuples tuple of animation_name,number of frames, e.g. [("idle", 4)]
        """

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.current_frame = 0

        self.current_animation_name = "idle"

        # Track out state
        self.scale = CHARACTER_SCALING

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # Load textures
        self.animation_name_texture_pairs = {}
        for animation_name, frames in animation_name_frames_tuples:
            self.animation_name_texture_pairs[animation_name] = []
            animation_textures = self.animation_name_texture_pairs[animation_name]
            for i in range(frames):
                animation_textures.append(load_texture_pair(f"images/npcs/{sprite_name}/{animation_name}{i}.png"))

    def update_animation(self, delta_time: float = 1/60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Idle
        if self.change_x == 0 and self.change_y == 0 and self.current_animation_name != "idle":
            self.current_animation_name = "idle"
            self.current_frame = 0

        # Animation
        self.current_frame += 1
        current_animation = self.animation_name_texture_pairs[self.current_animation_name]
        if self.current_frame // UPDATES_PER_FRAME >= len(current_animation):
            self.current_frame = 0
        self.texture = current_animation[self.current_frame // UPDATES_PER_FRAME][self.character_face_direction]