import pygame

class HomeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font('monospace'), 24)  # Load monospace font

    def show_welcome_message(self):
        welcome_text = self.font.render("Welcome to LLEMagnetSim", True, (255, 255, 255))
        self.screen.blit(welcome_text, (50, 50))
        pygame.display.flip()

    def fade_to_magnetar_display(self):
        # Implement fade effect here
        pass
import pygame
import csv

class MagnetarDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font('monospace'), 24)  # Load monospace font

    def load_data(self, data_source):
        with open(data_source, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.data = list(reader)

    def render(self):
        self.screen.fill((0, 0, 0))
        y = 50
        for row in self.data:
            text = self.font.render(', '.join(row), True, (255, 255, 255))
            self.screen.blit(text, (50, y))
            y += 30
        pygame.display.flip()
