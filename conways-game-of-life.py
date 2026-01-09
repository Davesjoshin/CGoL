import pygame
import numpy as np
import random

# Settings
COL_BACKGROUND = (10, 10, 40)
COL_ALIVE = (255, 255, 215)
COL_GRID = (30, 30, 60)
GRID_WIDTH = 100
GRID_HEIGHT = 100
CELL_SIZE = 4

# Speed (ms)
GAME_SPEED = 100

# Random starting grid
def build_random_grid():
    return np.random.randint(0, 2, (GRID_HEIGHT, GRID_WIDTH))

# Apply classic GoL rules
def update(surface, current, cell_size):
    next_grid = np.zeros(current.shape, dtype=int)

    for row, column in np.ndindex(current.shape):
        neighbors = np.sum(current[row-1:row+2, column-1:column+2]) - current[row, column]

        # Life finds a way (0.1% survival/birth no matter what)
        if random.random() < 0.001:
            next_grid[row, column] = 1

        else:
            # Classic rules
            if current[row, column] == 1 and neighbors in (2, 3):
                next_grid[row, column] = 1
            elif current[row, column] == 0 and neighbors == 3:
                next_grid[row, column] = 1

        color = COL_ALIVE if next_grid[row, column] == 1 else COL_BACKGROUND
        pygame.draw.rect(
            surface,
            color,
            (column * cell_size, row * cell_size, cell_size - 1, cell_size - 1)
        )

    return next_grid

def main():
    pygame.init()
    surface = pygame.display.set_mode(
        (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
    )
    pygame.display.set_caption("Conway's Game of Life")

    cells = build_random_grid()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(COL_GRID)
        cells = update(surface, cells, CELL_SIZE)
        pygame.display.flip()
        clock.tick(1000 // GAME_SPEED)

    pygame.quit()

if __name__ == "__main__":
    main()
