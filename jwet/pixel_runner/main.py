import sys
import pygame
from jwet.pixel_runner.parameters import Dimension, Color
from jwet.pixel_runner.game import Game


def main():
    """program to run the game"""
    pygame.init()
    screen = pygame.display.set_mode(Dimension.DISPLAY_SIZE.value)
    clock = pygame.time.Clock()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(Color.SCREEN_FILL_NOTHING.value)
        pygame.display.flip()
        game.run()
        clock.tick(Dimension.GAME_CLOCK_SPEED.value)


if __name__ == "__main__":
    main()
