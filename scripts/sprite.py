class Sprite:
    def __init__(self, image, center):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center

    def render(self,scene, offset_y):
        rect = self.rect.move(0, - offset_y)
        scene.blit(self.image, rect)
    
    def collide(self,other_rect):
        return self.rect.colliderect(other_rect)