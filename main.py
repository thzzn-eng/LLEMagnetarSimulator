import pygame
from home_screen import HomeScreen
from magnetar_display import MagnetarDisplay

def main():
    # Initialize Pygame
    pygame.init()

    # Get the screen dimensions
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h

    # Set the margin (1 inch = 96 pixels, adjust as needed)
    margin = 96

    # Set up the screen with the margin
    screen = pygame.display.set_mode((screen_width - 2 * margin, screen_height - 2 * margin))
    pygame.display.set_caption("Magnetar Simulator")

    # Load background image
    background_image = pygame.image.load("path/to/your/background_image.jpg")
    background_image = pygame.transform.scale(background_image, (screen_width - 2 * margin, screen_height - 2 * margin))

    # Initialize the home screen
    home_screen = HomeScreen(screen)
    home_screen.show_welcome_message()

    # Main event loop
    running = True
    show_home_screen = True
    magnetar_display = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and show_home_screen:
                    # Transition to the magnetar display with fade effect
                    home_screen.fade_to_magnetar_display()
                    magnetar_display = MagnetarDisplay(screen)
                    data_source = "c:/Users/Isaac O.D. Chance/llemagnetarsimulator/magnetar-simulator/src/TabO1.csv"  # Path to your CSV file
                    magnetar_display.load_data(data_source)
                    show_home_screen = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

            if magnetar_display:
                result = magnetar_display.handle_event(event)
                if result == 'back':
                    show_home_screen = True
                    magnetar_display = None

        if magnetar_display:
            screen.blit(background_image, (0, 0))  # Draw the background image
            magnetar_display.render()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
