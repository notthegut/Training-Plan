import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 5
SCREEN_SIZE = GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * MARGIN
BACKGROUND_COLOR = (187, 173, 160)
CELL_COLOR = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}
TEXT_COLOR = (119, 110, 101)

# Fonts
FONT = pygame.font.Font(None, 60)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("2048")

# Board initialization
def init_board():
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board


def draw_board(board):
    """Draw the 2048 board."""
    screen.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]
            color = CELL_COLOR.get(value, (60, 58, 50))
            pygame.draw.rect(
                screen,
                color,
                (
                    col * CELL_SIZE + (col + 1) * MARGIN,
                    row * CELL_SIZE + (row + 1) * MARGIN,
                    CELL_SIZE,
                    CELL_SIZE,
                ),
                0,
            )
            if value != 0:
                text = FONT.render(str(value), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(
                    col * CELL_SIZE + (col + 1) * MARGIN + CELL_SIZE / 2,
                    row * CELL_SIZE + (row + 1) * MARGIN + CELL_SIZE / 2,
                ))
                screen.blit(text, text_rect)
    pygame.display.flip()


def add_new_tile(board):
    """Add a new tile (2 or 4) to a random empty cell."""
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if board[r][c] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4


def move_left(board):
    """Move tiles left and merge."""
    moved = False
    for row in board:
        # Shift non-zero values to the left
        new_row = [value for value in row if value != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [value for value in new_row if value != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        if new_row != row:
            moved = True
        row[:] = new_row
    return moved


def rotate_board(board):
    """Rotate the board 90 degrees clockwise."""
    return [list(reversed(col)) for col in zip(*board)]


def move(board, direction):
    """Move tiles in the specified direction."""
    if direction == "left":
        return move_left(board)
    elif direction == "right":
        board = [row[::-1] for row in board]
        moved = move_left(board)
        board = [row[::-1] for row in board]
        return moved
    elif direction == "up":
        board = rotate_board(board)
        moved = move_left(board)
        board = rotate_board(rotate_board(rotate_board(board)))
        return moved
    elif direction == "down":
        board = rotate_board(rotate_board(rotate_board(board)))
        moved = move_left(board)
        board = rotate_board(board)
        return moved
    return False


def check_game_over(board):
    """Check if the game is over."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Check for any empty cells
            if board[row][col] == 0:
                return False
            # Check for any possible merges horizontally or vertically
            if col < GRID_SIZE - 1 and board[row][col] == board[row][col + 1]:
                return False
            if row < GRID_SIZE - 1 and board[row][col] == board[row + 1][col]:
                return False
    return True



# Main game loop
def main():
    board = init_board()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    direction = {
                        pygame.K_LEFT: "left",
                        pygame.K_RIGHT: "right",
                        pygame.K_UP: "up",
                        pygame.K_DOWN: "down",
                    }[event.key]
                    if move(board, direction):
                        add_new_tile(board)
                        if check_game_over(board):
                            print("Game Over!")
                            running = False

        draw_board(board)


if __name__ == "__main__":
    main()
