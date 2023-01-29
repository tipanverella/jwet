"""
   Player class, i.e. the ego of the game
"""
import pygame
from jwet.pixel_runner.parameters import GraphicAssets, Dimension, AudioAssets


class Player(pygame.sprite.Sprite):
    """Ego of the game"""

    def __init__(self):
        """initialize"""
        super().__init__()
        player_walk_1 = pygame.image.load(
            GraphicAssets.PLAYER.value["walk_1"]
        ).convert_alpha()
        player_walk_2 = pygame.image.load(
            GraphicAssets.PLAYER.value["walk_2"]
        ).convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            GraphicAssets.PLAYER.value["jump"]
        ).convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(
            midbottom=Dimension.PLAYER_STARTING_POSITION.value
        )
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound(AudioAssets.JUMP.value)
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        """space bar makes the player jump"""
        keys = pygame.key.get_pressed()
        if (
            keys[pygame.constants.K_SPACE]
            and self.rect.bottom >= Dimension.GROUND_LEVEL.value
        ):
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        """makes the player come back to the ground"""
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= Dimension.GROUND_LEVEL.value:
            self.rect.bottom = Dimension.GROUND_LEVEL.value

    def animation_state(self):
        """picks the correct image depending on the player action"""
        if self.rect.bottom < Dimension.GROUND_LEVEL.value:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        """updates the player"""
        self.player_input()
        self.apply_gravity()
        self.animation_state()
