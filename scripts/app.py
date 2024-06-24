import pygame
from scripts.function import load_image
from scripts.game import Game
from scripts.constants import display_size
from scripts.constants import create_platform_event

class App:

    def __init__(self):
        self.working = True
        self.FPS = 60
        self.scene = pygame.display.set_mode(display_size)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("DoodleJump")
        pygame.display.set_icon(load_image("assets", "icons", "icon.ico"))
        self.game = Game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.working = False
            elif event.type == pygame.KEYDOWN:
                self.game.process_key_down_event(event.key)
            elif event.type == pygame.KEYUP:
                self.game.process_key_up_event(event.key)

            elif event.type == create_platform_event:
                self.game.platforms.append(event.platform)

    def update(self):
        self.game.update_objects()

    def render(self):
        self.scene.fill((0, 0, 0))
        self.game.render_objects(self.scene)
        pygame.display.update()

    def run(self):
        while self.working:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)
