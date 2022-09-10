import pygame


class Ship:
    def __init__(self, ai): # see page 233 suppose to be ai_game same as next two lines
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        self.image = pygame.image.load("rocket2.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_up = False
        self.moving_left = False
        self.moving_down = False
        self.moving_right = False

    def update(self):
        if self.moving_up:
            self.rect.y += -1
        if self.moving_down:
            self.rect.y += 1

        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.x += 1
        if self.moving_left and self.rect.left < self.screen_rect.right and self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.rect.x += -1

    def blit(self):
        self.screen.blit(self.image, self.rect)