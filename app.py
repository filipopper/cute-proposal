import pygame
import time
import random
from ui.window import Window
from ui.button import Button
import webbrowser

pygame.display.set_caption("hola wawita")

pygame.init()

window = Window()

button_width = 120
button_height = 60
button_spacing = 20

yes_button = Button("Sí", (window.width // 2 - button_spacing - button_width, 200),
                    color=(0, 255, 0), width=button_width, height=button_height, border_radius=10)

no_button = Button("No", (window.width // 2 + button_spacing, 200),
                   color=(255, 0, 0), width=button_width, height=button_height, border_radius=10)

title_font = pygame.font.Font(None, 48)
title_surface = title_font.render("¿Puedo ser tu novio?", True, (0, 0, 0))
title_rect = title_surface.get_rect(center=(window.width // 2, 100))

wait_font = pygame.font.Font(None, 36)
wait_surface = wait_font.render("Gracias mi amor, te amo mucho <3", True, (0, 0, 0))
wait_rect = wait_surface.get_rect(center=(window.width // 2, window.height // 2))

image = pygame.image.load("assets/flores.png")
image = pygame.transform.scale(image, (200, 200))
image_rect = image.get_rect(center=(window.width // 2, window.height // 2 + 100))

youtube_video_url = "https://www.youtube.com/watch?v=46Ls-XqSVT4"

current_screen = "buttons"
start_time = None
flower_display_time = 3
video_opened = False

def open_youtube_video():
    webbrowser.open(youtube_video_url)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "buttons":
                if yes_button.rect.collidepoint(event.pos):
                    current_screen = "waiting"
                    start_time = time.time()
                elif no_button.rect.collidepoint(event.pos):
                    no_button.move_randomly()

    yes_button.update()
    no_button.update()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if current_screen == "buttons" and abs(mouse_x - no_button.rect.centerx) < 50 and abs(mouse_y - no_button.rect.centery) < 50:
        no_button.move_randomly()

    window.screen.fill((255, 255, 255))
    
    if current_screen == "buttons":
        window.screen.blit(title_surface, title_rect)
        yes_button.draw(window.screen)
        no_button.draw(window.screen)
    elif current_screen == "waiting":
        window.screen.blit(wait_surface, wait_rect)
        if start_time is not None and time.time() - start_time >= 4:
            current_screen = "showing_flowers"
            start_time = time.time()
    elif current_screen == "showing_flowers":
        flower_x = window.width // 2 - image.get_width() // 2
        flower_y = window.height // 2 - image.get_height() // 2
        window.screen.blit(image, (flower_x, flower_y))
        
        if start_time is not None and time.time() - start_time >= flower_display_time:
            current_screen = "video_opened"
            start_time = time.time()
            open_youtube_video()

    if current_screen == "video_opened":
        pygame.quit()
        exit()
    
    pygame.display.update()