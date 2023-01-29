"""
    Game class module
"""
import pygame

from jwet.pixel_runner.parameters import FontAssets, Dimension, AudioAssets, GraphicAssets, Color
from jwet.pixel_runner.player import Player


class Game:
    def __init__(self):
        pass

    def run(self):
        pygame.display.set_caption("Pixel Runner")
        text_font = pygame.font.Font(FontAssets.TEXT.value, Dimension.FONT_SIZE.value)
        game_active = False
        start_time = 0
        score = 0
        bg_music = pygame.mixer.Sound(AudioAssets.SOUNDTRACK.value)
        bg_music.set_volume(0.10)
        bg_music.play(loops=-1)
        player = pygame.sprite.GroupSingle()
        player.add(Player())

        obstacle_group = pygame.sprite.Group()

        sky_surface = pygame.image.load(GraphicAssets.CANVAS.value["sky"]).convert()
        ground_surface = pygame.image.load(GraphicAssets.CANVAS.value["ground"]).convert()

        # Intro screen
        player_stand = pygame.image.load(GraphicAssets.PLAYER.value["stand"]).convert_alpha()
        player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
        player_stand_rect = player_stand.get_rect(
            center=Dimension.PLAYER_STARTING_POSITION.value
        )

        game_name = text_font.render("Pixel Runner", False, Color.GAME_NAME_MESSAGE.value)
        game_name_rect = game_name.get_rect(center=Dimension.GAME_NAME_POSITION.value)

        game_message = text_font.render(
            "Press space to run", False, Color.GAME_NAME_MESSAGE.value
        )
        game_message_rect = game_message.get_rect(center=Dimension.GAME_MESSAGE_POSITION.value)

        # Timer
        obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(obstacle_timer, Dimension.SPAWNING_WAIT_MILLI_SECOND.value)
