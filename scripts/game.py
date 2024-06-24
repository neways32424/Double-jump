import pygame
from scripts.constants import display_size
from scripts.function import load_image, get_path
from scripts.player import Player
from scripts.platform_genetation import PlatformGeneration


class Game:
    def __init__(self):
        self.background = load_image("assets", "images", "background.png")
        self.platforms = [
            
        ]
        self.player = Player(
            load_image("assets", "images", "player.png"),
            (240, 600),
            20,
            10,
            0.75,
        )
        self.jump_sound = pygame.mixer.Sound(
            get_path("assets", "sounds", "jump.mp3")
        )
        self.falling_sound = pygame.mixer.Sound(
            get_path("assets", "sounds", "falling.mp3")
        )
        self.offset_y = 0
        self.platform_generation = PlatformGeneration(200)
        self.platform_generation.create_start_configurations()

        self.font = pygame.Font(get_path('assets', 'fonts', 'pixel.ttf'),32)
        self.score = 0
        self.losed = False
        pygame.mixer_music.load(get_path('assets', 'music', 'caves.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)
                                         

    def render_objects(self, scene):
        scene.blit(self.background, (0, 0))
        for platform in self.platforms:
            platform.render(scene, self.offset_y)
        self.player.render(scene, self.offset_y)
        if self.losed:
            score_text = self.font.render(
                "Ваш счёт" + str(self.score), True, (0, 0, 0)
            )
            hint_text = self.font.render(
                "Нажмите любую клавишу", True, (0, 0, 0)
            )
            text_rect = score_text.get_rect(
                centerx=display_size[0] / 2,
                centery=display_size[1] / 2 - 25
            )
            hint_rect = hint_text.get_rect(
            centerx=display_size[0] / 2,
            centery=display_size[1] / 2 + 25 
            )
            scene.blit(score_text, text_rect)
            scene.blit(hint_text, hint_rect)
        else:
            text_image = self.font.render(str(self.score), True, (0,0,0))
            text_rect = text_image.get_rect(centerx = display_size[0] / 2,top = 10 )
            scene.blit(text_image, text_rect)
        
    def process_key_down_event(self, key):
        if self.losed:
            self.losed = False
            self.offset_y = 0
            self.score = 0 
            self.platforms =[]

            self.platform_generation.create_start_configurations()
            self.player.reset((240, 600))
        elif key == pygame.K_a:
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True

    def process_key_up_event(self, key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        if key == pygame.K_d:
            self.player.is_walking_right = False

    def update_objects(self):
        prev_losed = self.losed
        self.losed = self.player.rect.top - self.offset_y >= display_size[1]

        if self.losed:
            if not prev_losed:
                self.falling_sound.play()
            return
        

        for platform in self.platforms:
            platform.update()
            if self.player.collide(platform.rect):
                self.player.on_platform = True
                self.jump_sound.play()
        self.player.update()

        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
            self.score = abs(round(self.offset_y / 10))
            
        self.platform_generation.update(self.offset_y, self.platforms)
