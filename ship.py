import pygame

class Ship():
    def __init__(self, game_settings, screen):

        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("alien.bmp/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
       # self.center_y = float(self.rect.centery)
        self.rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.car_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.car_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.game_settings.car_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.game_settings.car_speed_factor
        self.rect.centerx = self.center
    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def ship_cemter(self):
        self.center = self.screen_rect.centerx