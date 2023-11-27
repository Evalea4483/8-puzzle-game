import pygame
import sys
import random


# puzzle sizes
PUZZLE_DIM = 3
TILE_SIZE = 100
WINDOW_SIZE = PUZZLE_DIM * TILE_SIZE

# game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initial cnfiguration
INITIAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# set font
pygame.font.init()
font = pygame.font.Font(None, 36)

# initialization
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

pygame.display.set_caption("8-Puzzle")

# shuffle configuration

random.shuffle(INITIAL_STATE)

# draw the puzzle board
def draw_puzzle(state):
    for i, number in enumerate(state):
        if number != 0:
            row, col = divmod(i, PUZZLE_DIM)
            x, y = col * TILE_SIZE, row * TILE_SIZE
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
            text = font.render(str(number), True, WHITE)
            text_rect = text.get_rect(center=(x + TILE_SIZE / 2, y + TILE_SIZE / 2))
            screen.blit(text, text_rect)

# blank tile
def get_blank_tile_index(state):
    return state.index(0)

# game loop
running = True
while running:
    screen.fill(WHITE)
    draw_puzzle(INITIAL_STATE)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            blank_index = get_blank_tile_index(INITIAL_STATE)
            if event.key == pygame.K_UP and blank_index >= PUZZLE_DIM:
                INITIAL_STATE[blank_index], INITIAL_STATE[blank_index - PUZZLE_DIM] = INITIAL_STATE[blank_index - PUZZLE_DIM], INITIAL_STATE[blank_index]
            elif event.key == pygame.K_DOWN and blank_index < PUZZLE_DIM * (PUZZLE_DIM - 1):
                INITIAL_STATE[blank_index], INITIAL_STATE[blank_index + PUZZLE_DIM] =  INITIAL_STATE[blank_index + PUZZLE_DIM], INITIAL_STATE[blank_index]
            elif event.key == pygame.K_LEFT and blank_index % PUZZLE_DIM != 0:
                INITIAL_STATE[blank_index], INITIAL_STATE[blank_index - 1] = INITIAL_STATE[blank_index - 1], INITIAL_STATE[blank_index]
            elif event.key == pygame.K_RIGHT and (blank_index + 1) % PUZZLE_DIM != 0:
                INITIAL_STATE[blank_index], INITIAL_STATE[blank_index + 1] = INITIAL_STATE[blank_index + 1], INITIAL_STATE[blank_index]

        if INITIAL_STATE == list(range(1, PUZZLE_DIM * PUZZLE_DIM)) + [0]:
            print("Wow, you solved it!")
            running = False

pygame.quit()
sys.exit()
