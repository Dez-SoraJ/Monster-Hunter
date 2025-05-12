import pygame
import sys
from tkinter import Tk, filedialog
from main1 import Game  # Import the Game class

pygame.init()

# Define constants outside the class
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HDCLR = (225, 50, 125)

try:
    background_image = pygame.image.load(r"C:\Users\ADMIN\Desktop\Monster Hunter\bg2.jpg")
    background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    print("Background image loaded successfully.")
except pygame.error as e:
    print(f"Error loading background image: {e}")
    sys.exit(1)

font = pygame.font.Font(r"C:\Users\ADMIN\Desktop\Monster Hunter\graphics\fonts\PixeloidSans.ttf", 48)
font2 = pygame.font.Font(r"C:\Users\ADMIN\Desktop\Monster Hunter\graphics\fonts\dogicapixel.otf", 70)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Hunter")
menu_options = ["Start Game", "Load Game", "Save Game", "Exit"]
selected_option = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main_menu():
    global selected_option
    clock = pygame.time.Clock()
    while True:
        screen.blit(background_image, (0, 0))  
        draw_text("Monster Hunter", font2, HDCLR, screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4)
        for idx, option in enumerate(menu_options):
            color = WHITE if idx == selected_option else BLACK
            draw_text(option, font, color, screen, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + idx * 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        start_game()
                    elif selected_option == 1:
                        load_game()
                    elif selected_option == 2:
                        save_game()
                    elif selected_option == 3:
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

def start_game():
    game = Game()
    game.run()

def load_game():
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Save File",
        filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))
    if not file_path:
        return
    game = Game()
    if game.load_game_state(file_path):
        game.run()
    else:
        print("Failed to load game state.")

def save_game():
    Tk().withdraw()  
    file_path = filedialog.asksaveasfilename(
        title="Save Game", defaultextension=".json", filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))
    if not file_path:
        return
    game = Game()
    game.save_game_state(file_path)

if __name__ == "__main__":
    main_menu()
