# pyinstaller --add-data 'assets;./assets'--icon=assets/icons/icon.ico -F -w main.py

import pygame
from scripts.app import App


def main():
    pygame.init()

    app = App()
    app.run()


if __name__ == "__main__":
    main()
