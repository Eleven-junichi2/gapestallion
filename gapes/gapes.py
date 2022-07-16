import pygame

import manager_scene


pygame.init()

clock = pygame.time.Clock()

scene_manager = manager_scene.SceneManager()


def run(fps=60):
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            scene_manager.draw()
        clock.tick(fps)
    pygame.quit()
