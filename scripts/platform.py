from scripts.sprite import Sprite
from scripts.constants import display_size

class Platform(Sprite):
    def __init__(self, image, coords):
        super().__init__(image, coords)

    def update(self):
        pass

class  MovingPlatform(Platform):
    def __init__(self, image, coords, speed):
        super().__init__(image, coords)

        self.speed = speed 

    def update(self):
        self.rect
        if self.rect.left < 0:
            self.speed = abs(self.speed)
        if self.rect.right  > display_size[0]:
            self.speed = -abs(self.speed)
        self.rect.x += self.speed