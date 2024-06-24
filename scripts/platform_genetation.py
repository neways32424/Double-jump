from random import randint

import pygame
from scripts.function import load_image 
from scripts.constants import display_size
from scripts.platform import Platform, MovingPlatform
from scripts.constants import create_platform_event

class PlatformGeneration:
    def __init__(self, step) -> None:
        self.step = step 

    def create_start_configurations(self):
        platform = Platform(
            load_image('assets', 'images', 'platform.png'),
            [display_size[0] / 2, display_size[1] - 50],
        )
        event = pygame.Event(create_platform_event, {'platform': platform})
        pygame.event.post(event)

        for y in range(display_size[1], 0 , -self.step): 
            self.create_platform(y)

    def create_platform(self, center_y):
        r = randint(0, 100)
        if r > 77:
            image = load_image('assets', 'images', 'moving-platform.png')
        else:
            image = load_image('assets', 'images', 'platform.png')

        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)
        if r > 77:
            speed = randint(10, 50) / 10
            platform = MovingPlatform(image, [center_x, center_y], speed)
        else:
            platform = Platform(image, [center_x, center_y])

        event = pygame.Event(create_platform_event, {'platform': platform})
        pygame.event.post(event)

    def update(self, offset_y, platforms):
        if platforms and platforms[-1].rect.centery - offset_y >= self.step:
            self.create_platform(offset_y)
            platforms.remove(platforms[0])
