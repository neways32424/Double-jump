import pygame
import os
import sys

def load_image(*paths):

    path = get_path(*paths)
    image = pygame.image.load(path).convert()
    image.set_colorkey((0, 0, 0))
    return image
base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname('main.py')))

def get_path(*paths):

    path = os.path.join(base_path, *paths)
    return path

    
    