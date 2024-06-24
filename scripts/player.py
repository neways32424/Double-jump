from scripts.sprite import Sprite
from scripts.constants import display_size
import pygame


class Player(Sprite):
    def __init__(self, image, center, jump, speed, gravity):
        super().__init__(image, center)
        self.original_image = image.copy()
        self.jump = jump
        self.speed = speed
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False
        self.velocity_y = 0
        self.on_platform = False

    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect.y += self.velocity_y

        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.rect.x -= self.speed
                self.image = pygame.transform.flip(self.original_image, True, False)
            else:
                self.rect.x += self.speed
                self.image = self.original_image.copy()

        if self.on_platform:
            self.velocity_y = - self.jump
            self.on_platform = False
        
        if self.rect.right < 0:
            self.rect.left = display_size[0]
        if self.rect.left > display_size[0]:
            self.rect.right = 0

    def collide(self, other_rect):
        rect = pygame.Rect(self.rect.bottomleft,(self.rect.width, 20 ))
        return self.velocity_y > 0 and other_rect.colliderect(rect)
    def reset(self, coords):
        super().__init__(self.original_image, coords)
        self.is_walking_left = False
        self.is_walking_right = False
        self.velocity_y = 0
