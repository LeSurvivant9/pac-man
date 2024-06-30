import pygame

from spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self,  scale: int, pos: tuple[int, int], *sprite_groups: pygame.sprite.Group):
        super().__init__(*sprite_groups)
        self.sprites: SpriteSheet = SpriteSheet("pac-man_sprites.png")
        self.image: pygame.Surface = self.sprites.get_image(0, 16, 16, scale / 2)
        pos = (pos[0], pos[1] - self.image.get_height() // 2)
        self.rect: pygame.FRect = self.image.get_frect(center=pos)
        self.direction: pygame.Vector2 = pygame.Vector2()
        self.directions: dict[str: bool] = {
            "up": False,
            "left": False,
            "down": False,
            "right": False
        }
        self.speed: float = 0.1

    def update(self, delta_time: float):
        keys = pygame.key.get_pressed()
        direction_keys = {
            "up": [pygame.K_UP, pygame.K_z],
            "left": [pygame.K_LEFT, pygame.K_q],
            "down": [pygame.K_DOWN, pygame.K_s],
            "right": [pygame.K_RIGHT, pygame.K_d]
        }

        for direction, key_list in direction_keys.items():
            if any(keys[key] for key in key_list):
                self.directions = {k: (k == direction) for k in self.directions}
                break

        self.direction.x = int(self.directions["right"]) - int(self.directions["left"])
        self.direction.y = int(self.directions["down"]) - int(self.directions["up"])
        self.rect.center += self.direction * self.speed * delta_time
