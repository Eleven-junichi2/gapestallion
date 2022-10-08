import pygame

from . import manager_scene


pygame.init()

clock = pygame.time.Clock()

scene_manager = manager_scene.SceneManager()


def init(window_size=(1200, 800), caption=""):
    pygame.display.set_mode((window_size[0], window_size[1]))
    pygame.display.set_caption(caption)


def run(fps=60):
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            scene_manager.draw()
        clock.tick(fps)
    pygame.quit()
