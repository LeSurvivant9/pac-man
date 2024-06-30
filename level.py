import os

import pygame
import pytmx

from tile import Tile


class Collision(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], surf: pygame.Surface, *sprite_groups: pygame.sprite.Group):
        super().__init__(*sprite_groups)
        self.image: pygame.Surface = surf
        self.rect: pygame.Rect = self.image.get_rect(topleft=pos)


class Level:
    def __init__(self, scale: int, *sprite_groups: pygame.sprite.Group):
        self.all_collisions: pygame.sprite.Group = pygame.sprite.Group()

        tmx_data: pytmx.TiledMap = pytmx.util_pygame.load_pygame(os.path.join("data", "tmx", "map.tmx"))
        for layer in tmx_data.visible_layers:
            if hasattr(layer, "data"):
                for x, y, surf in layer.tiles():
                    surf: pygame.Surface
                    pos = (x * 8 * scale, y * 8 * scale)
                    surf = pygame.transform.scale(surf, (8 * scale, 8 * scale))
                    Tile(pos, surf, *sprite_groups)

        for obj in tmx_data.objects:
            if obj.type == "Collision":
                surf = pygame.Surface((obj.width * scale, obj.height * scale))
                pos = (obj.x * scale, obj.y * scale)
                Collision(pos, surf, self.all_collisions)
