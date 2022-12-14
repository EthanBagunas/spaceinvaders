import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_s:
            self.ship.moving_down = True
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_s:
            self.ship.moving_down = False
        if event.key == pygame.K_d:
            self.ship.moving_right = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()
        pygame.display.flip()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
