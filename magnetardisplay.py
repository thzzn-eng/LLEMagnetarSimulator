import pygame
from utils.data_loader import load_data

class MagnetarDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.magnetars = []
        self.scroll_y = 0  # Initial scroll position
        self.buttons = []
        self.detail_view = None
        self.return_button = pygame.Rect(10, 10, 100, 40)  # Define the return button rectangle

    def load_data(self, data_source):
        self.magnetars = load_data(data_source)
        print(f"Loaded {len(self.magnetars)} magnetars")  # Debugging statement
        self.create_buttons()

    def create_buttons(self):
        font = pygame.font.Font("path/to/your/custom_font.ttf", 24)  # Use a custom font
        y_offset = 50
        self.buttons = []
        row_width = self.screen.get_width() - 100  # Total width available for buttons in a row

        for i, magnetar in enumerate(self.magnetars):
            text = font.render(magnetar['Name'], True, (255, 255, 255))
            button_rect = text.get_rect()
            button_rect.topleft = (0, y_offset)
            self.buttons.append((button_rect, magnetar))

            if (i + 1) % 3 == 0 or i == len(self.magnetars) - 1:
                # Center the buttons in the current row
                total_width = sum(button.width for button, _ in self.buttons[-3:])
                x_offset = (row_width - total_width) // 2 + 50
                for button_rect, _ in self.buttons[-3:]:
                    button_rect.x = x_offset
                    x_offset += button_rect.width + 50
                y_offset += 40

    def render(self):
        if self.detail_view:
            self.detail_view.render()
        else:
            print("Rendering magnetars...")  # Debugging statement
            self.screen.fill((0, 0, 0, 0))  # Fill the screen with transparent color
            font = pygame.font.Font("path/to/your/custom_font.ttf", 24)  # Use a custom font
            
            # Create a surface to render all magnetars
            content_height = ((len(self.magnetars) + 2) // 3) * 40 + 50
            content_surface = pygame.Surface((self.screen.get_width(), content_height), pygame.SRCALPHA)
            content_surface.fill((0, 0, 0, 0))  # Fill the content surface with transparent color

            for button_rect, magnetar in self.buttons:
                text = font.render(magnetar['Name'], True, (255, 255, 255))
                content_surface.blit(text, button_rect.topleft)

            # Blit the content surface onto the screen with scrolling
            self.screen.blit(content_surface, (0, -self.scroll_y))

            # Draw the return button
            pygame.draw.rect(self.screen, (255, 0, 0), self.return_button, border_radius=10)
            return_text = font.render("Return", True, (255, 255, 255))
            self.screen.blit(return_text, (20, 20))

            pygame.display.flip()

    def handle_event(self, event):
        if self.detail_view:
            result = self.detail_view.handle_event(event)
            if result == 'back':
                self.detail_view = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    self.scroll_y = max(0, self.scroll_y - 40)
                elif event.button == 5:  # Scroll down
                    self.scroll_y += 40
                elif event.button == 1:  # Left click
                    mouse_pos = event.pos
                    if self.return_button.collidepoint(mouse_pos):
                        return 'back'
                    for button_rect, magnetar in self.buttons:
                        if button_rect.collidepoint(mouse_pos[0], mouse_pos[1] + self.scroll_y):
                            print(f"Button {magnetar['Name']} clicked")
                            from magnetar_detail import MagnetarDetail
                            self.detail_view = MagnetarDetail(self.screen, magnetar)
        return None
