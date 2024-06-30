import pygame

from colors import Colors
from level import Level
from player import Player


class Game:
    def __init__(self):
        self.scale: int = 4
        self.screen: pygame.Surface = pygame.display.set_mode((224 * self.scale, 248 * self.scale))
        pygame.display.set_caption("Pac-Man")
        self.is_running: bool = True
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.player_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.map_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.FPS: int = 60
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.delta_time: float = self.clock.tick(self.FPS)
        self.level: Level = Level(self.scale, self.all_sprites, self.map_sprites)
        self.player: Player = Player(self.scale, (14 * 8 * self.scale, 18 * 8 * self.scale), self.all_sprites,
                                     self.player_sprites)

    def detect_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def detect_collision(self):
        if coll := pygame.sprite.groupcollide(self.level.all_collisions, self.player_sprites, False, False):
            pass

    def update(self):
        self.detect_collision()
        self.screen.fill(Colors.RED)
        self.all_sprites.update(self.delta_time)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.delta_time = self.clock.tick(self.FPS)
            self.detect_events()
            self.update()
            # print(pygame.sprite.coll(self.player_sprites, self.level.all_collisions, False, False))
