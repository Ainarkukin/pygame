import pygame

class Pablo:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("image/Pablo.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen.rect.bottom
    def blitme(self):
        self.screen.blit(self.image, self.rect)