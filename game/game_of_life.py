import pygame
import numpy as np


class GameOfLife:
    def __init__(self, width=800, height=600, n_cells_x=40, n_cells_y=30):
        pygame.init()
        self.width, self.height = width, height
        self.n_cells_x, self.n_cells_y = n_cells_x, n_cells_y
        self.cell_width = width // n_cells_x
        self.cell_height = height // n_cells_y

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (128, 128, 128)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        # Pygame setup
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

        # Buttons
        self.button_width, self.button_height = 100, 50
        self.next_button = pygame.Rect(10, self.height - self.button_height - 10, self.button_width, self.button_height)
        self.start_stop_button = pygame.Rect(self.next_button.right + 10, self.height - self.button_height - 10,
                                             self.button_width, self.button_height)
        self.save_button = pygame.Rect(self.start_stop_button.right + 10, self.height - self.button_height - 10,
                                       self.button_width, self.button_height)
        self.load_button = pygame.Rect(self.save_button.right + 10, self.height - self.button_height - 10,
                                       self.button_width, self.button_height)

        # Game state
        self.game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])
        self.running = False  # Real-time mode flag

    def draw_button(self, rect, text, color):
        pygame.draw.rect(self.screen, color, rect)
        font = pygame.font.Font(None, 24)
        label = font.render(text, True, self.black)
        label_rect = label.get_rect(center=rect.center)
        self.screen.blit(label, label_rect)

    def draw_grid(self):
        for y in range(0, self.height, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, self.gray, cell, 1)

    def draw_cells(self):
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if self.game_state[x, y] == 1:
                    pygame.draw.rect(self.screen, self.black, cell)

    def next_generation(self):
        self.check_full_or_empty()
        new_state = np.copy(self.game_state)
        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                n_neighbors = self.count_neighbors(x, y)
                if self.game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.game_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1
        self.game_state = new_state

    def count_neighbors(self, x, y):
        neighbors = sum(
            self.game_state[(x + dx) % self.n_cells_x, (y + dy) % self.n_cells_y]
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if dx != 0 or dy != 0
        )
        return neighbors

    def check_full_or_empty(self):
        total_alive = np.sum(self.game_state)
        if total_alive == 0 or total_alive == self.n_cells_x * self.n_cells_y:
            # Change a few random cells to the opposite state
            for _ in range(10):  # Arbitrary number of changes
                x, y = np.random.randint(0, self.n_cells_x), np.random.randint(0, self.n_cells_y)
                self.game_state[x, y] = 1 - self.game_state[x, y]

    def save_state(self, filename="game_state.txt"):
        np.savetxt(filename, self.game_state, fmt='%d')
        print(f"Game state saved to {filename}")

    def load_state(self, filename="game_state.txt"):
        try:
            self.game_state = np.loadtxt(filename, dtype=int)
            print(f"Game state loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Unable to load state.")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_button.collidepoint(event.pos):
                    self.next_generation()
                elif self.start_stop_button.collidepoint(event.pos):
                    self.running = not self.running
                elif self.save_button.collidepoint(event.pos):
                    self.save_state()
                elif self.load_button.collidepoint(event.pos):
                    self.load_state()
                else:
                    x, y = event.pos[0] // self.cell_width, event.pos[1] // self.cell_height
                    self.game_state[x, y] = not self.game_state[x, y]
        return True

    def run(self):
        running = True
        while running:
            self.screen.fill(self.white)
            self.draw_grid()
            self.draw_cells()
            self.draw_button(self.next_button, "Next", self.green)
            self.draw_button(self.start_stop_button, "Start" if not self.running else "Stop", self.red)
            self.draw_button(self.save_button, "Save", self.blue)
            self.draw_button(self.load_button, "Load", self.blue)
            pygame.display.flip()

            if self.running:
                self.next_generation()

            running = self.handle_input()
            self.clock.tick(10)  # Limit FPS to 10

        pygame.quit()


if __name__ == "__main__":
    game = GameOfLife()
    game.run()
