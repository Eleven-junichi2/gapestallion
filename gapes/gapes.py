import pygame

from gapes import manager_scene


pygame.init()

clock = pygame.time.Clock()

scene_manager = manager_scene.SceneManager()


def init(window_size=(1200, 800), caption=""):
    global screen
    screen = pygame.display.set_mode((window_size[0], window_size[1]))
    pygame.display.set_caption(caption)


def run(fps=60):
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
        if scene_manager.is_empty():
            gameloop = False
        scene = scene_manager.get_scene()
        scene_manager.update()
        scene_after_update = scene_manager.get_scene()
        # draw if the scene has changed
        if scene_after_update is scene:
            screen.fill((0, 0, 0))
            scene_manager.draw()
            pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
