import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], surf: pygame.Surface, *sprite_groups: pygame.sprite.Group):
        super().__init__(*sprite_groups)
        self.image: pygame.Surface = surf
        self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
