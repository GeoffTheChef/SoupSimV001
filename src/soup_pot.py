import pygame

class SOUP_POT(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(200, 200, 200, 200)  # Changed to pygame.Rect for proper handling
        self.color = pygame.Color("black")

    def update(self, mousePos):
        # Fixed method name from 'colidepoints' to 'collidepoint'
        if self.rect.collidepoint(mousePos):
            print("Ingredient List")

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
