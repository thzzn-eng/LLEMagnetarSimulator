import pygame

class MagnetarDetail:
    def __init__(self, screen, magnetar):
        self.screen = screen
        self.magnetar = magnetar
        self.font = pygame.font.Font("path/to/your/custom_font.ttf", 24)  # Use a custom font
        self.return_button = pygame.Rect(10, 10, 100, 40)  # Define the return button rectangle

    def render(self):
        self.screen.fill((0, 0, 0, 0))  # Fill the screen with transparent color
        pygame.draw.rect(self.screen, (255, 0, 0), self.return_button, border_radius=10)  # Draw the return button
        return_text = self.font.render("Return", True, (255, 255, 255))
        self.screen.blit(return_text, (20, 20))

        y_offset = 70
        for key, value in self.magnetar.items():
            display_value = value if value else "N/A"
            text = self.font.render(f"{key}: {display_value}", True, (255, 255, 255))
            self.screen.blit(text, (50, y_offset))
            y_offset += 30
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.return_button.collidepoint(event.pos):
                return 'back'
        return None
