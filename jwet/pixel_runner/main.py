import pygame
from jwet.pixel_runner.parameters import Dimension, Color

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "Snail", "Snail", "Snail"])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, Dimension.GROUND_LEVEL.value))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        screen.fill(Color.SCREEN_FILL.value)
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(
            f"Your score: {score}", False, Color.GAME_NAME_MESSAGE.value
        )
        score_message_rect = score_message.get_rect(
            center=Dimension.GAME_MESSAGE_POSITION.value
        )
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(Dimension.GAME_CLOCK_SPEED.value)
