import arcade

UPDATES_PER_FRAME = 7

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1


def load_texture_pair(filename):
    """ Load a texture pair, with the second being a mirror image. """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
    ]


class AnimatedSprite(arcade.Sprite):
    def __init__(self, sprite_name, animation_name_frames_tuples=[("idle", 1)]):
        """ sprite_name folder containing sprite, e.g. kingkrool
        animation_name_frames_tuples tuple of animation_name,number of frames, e.g. [("idle", 4)]
        """
        super().__init__()
        self.sprite_name = sprite_name

        # Default to face-right
        self.character_face_direction = RIGHT_FACING

        # Used for flipping between image sequences
        self.current_animation_name = "idle"
        self.current_frame = 0

        # Load textures
        self.animation_name_texture_pairs = {}
        for animation_name, frames in animation_name_frames_tuples:
            self.animation_name_texture_pairs[animation_name] = []
            animation_textures = self.animation_name_texture_pairs[animation_name]
            for i in range(frames):
                animation_textures.append(
                    load_texture_pair(
                        f"images/npcs/{sprite_name}/{animation_name}{i}.png"
                    )
                )
        self.texture = self.animation_name_texture_pairs[self.current_animation_name][
            0
        ][self.character_face_direction]

    def update(self):
        super().update()
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Animation
        self.current_frame += 1
        current_animation = self.animation_name_texture_pairs[
            self.current_animation_name
        ]
        if self.current_frame // UPDATES_PER_FRAME >= len(current_animation):
            self.current_frame = 0
        self.texture = current_animation[self.current_frame // UPDATES_PER_FRAME][
            self.character_face_direction
        ]

    def set_animation(self, animation_name):
        if not self.has_animation(animation_name):
            print(f"Animation {animation_name} not in sprite {self.sprite_name}")
            return
        if self.current_animation_name == animation_name:
            print(f"Animation {animation_name} already active")
        self.current_animation_name = animation_name
        self.current_frame = 0

    def has_animation(self, animation_name):
        return animation_name in self.animation_name_texture_pairs
