import os.path

import pygame

from colors import Colors


class SpriteSheet:
    def __init__(self, image: str):
        self.sheet: pygame.Surface = pygame.image.load(os.path.join("data", "spritesheets", image)).convert_alpha()

    def get_image(
            self,
            frame: int,
            width: int,
            height: int,
            scale: float = 1.0,
            color: tuple[int, int, int] = Colors.BLACK,
    ) -> pygame.Surface:
        image: pygame.Surface = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
