"""
    Obstacles for the player
"""
from random import randint
from enum import Enum
import pygame
from jwet.pixel_runner.parameters import Dimension, GraphicAssets


class ObstacleType(Enum):
    """allowed types of obstacles"""

    SNAIL = {"y_position": Dimension.GROUND_LEVEL}
    FLY = {"y_position": Dimension.FLYING_LEVEL}


class Obstacle(pygame.sprite.Sprite):
    """Obstacles to evade"""

    def __init__(self, obstacle_type: ObstacleType):
        """initialize"""
        super().__init__()
        image_1 = pygame.image.load(
            GraphicAssets[obstacle_type]["1"].value
        ).convert_alpha()
        image_2 = pygame.image.load(
            GraphicAssets[obstacle_type]["2"].value
        ).convert_alpha()
        self.frames = [image_1, image_2]
        y_pos = obstacle_type.value["y_position"]
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        """cycle thru images to simulate animation"""
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        """update the obstacle"""
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        """remove the obstacle when completely off the screen"""
        if self.rect.x <= -100:
            self.kill()
