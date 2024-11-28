import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_COLOR = (50, 50, 50)
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
COMPUTER_COLOR = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Fonts
FONT = pygame.font.Font(None, 100)
SMALL_FONT = pygame.font.Font(None, 40)

# Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

# Game variables
current_player = "X"  # Player X starts
game_over = False


def draw_grid():
    """Draw the Tic-Tac-Toe grid."""
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH / 3, 0), (SCREEN_WIDTH / 3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, LINE_COLOR, (2 * SCREEN_WIDTH / 3, 0), (2 * SCREEN_WIDTH / 3, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, SCREEN_HEIGHT / 3), (SCREEN_WIDTH, SCREEN_HEIGHT / 3), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SCREEN_HEIGHT / 3), (SCREEN_WIDTH, 2 * SCREEN_HEIGHT / 3), 5)


def draw_board():
    """Draw the current board state."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text = FONT.render("X", True, PLAYER_COLOR)
                screen.blit(text, (col * SCREEN_WIDTH / 3 + 50, row * SCREEN_HEIGHT / 3 + 25))
            elif board[row][col] == "O":
                text = FONT.render("O", True, COMPUTER_COLOR)
                screen.blit(text, (col * SCREEN_WIDTH / 3 + 50, row * SCREEN_HEIGHT / 3 + 25))


def check_winner():
    """Check if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None


def computer_move():
    """Make a move for the computer (O)."""
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"


# Game loop
while True:
    draw_grid()
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN and current_player == "X":
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // (SCREEN_HEIGHT // 3)
            col = mouse_x // (SCREEN_WIDTH // 3)

            if board[row][col] == " ":
                board[row][col] = "X"
                winner = check_winner()
                if winner:
                    game_over = True
                else:
                    current_player = "O"
                    computer_move()
                    winner = check_winner()
                    if winner:
                        game_over = True
                    current_player = "X"

    if game_over:
        winner = check_winner()
        if winner == "Draw":
            text = SMALL_FONT.render("It's a draw!", True, LINE_COLOR)
        else:
            text = SMALL_FONT.render(f"{winner} wins!", True, LINE_COLOR)
        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
