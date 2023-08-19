import pygame

class Window:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def run(self):
        pass  # Puedes añadir el bucle principal de la ventana aquí
