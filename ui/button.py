import pygame
import random

class Button:
    def __init__(self, text, position, color=(0, 0, 0), width=100, height=50, border_radius=0):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(None, 36)
        self.color = color
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def update(self):
        pass  # Puedes añadir actualizaciones al botón aquí

    def move_randomly(self):
        # Mueve el botón a una posición aleatoria en la pantalla
        self.rect.x = random.randint(0, 540)  # Limita el rango para mantener el botón visible
        self.rect.y = random.randint(0, 430)
