import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_RADIUS = 10

# Speeds
PADDLE_SPEED = 5
BALL_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Paddles
player1 = pygame.Rect(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - PADDLE_WIDTH - 10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Scores
player1_score, player2_score = 0, 0

# Font
font = pygame.font.Font(None, 36)

def main():
    global ball_dx, ball_dy, player1_score, player2_score

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += PADDLE_SPEED
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += PADDLE_SPEED

        # Move ball
        ball.x += ball_dx
        ball.y += ball_dy

        # Ball collision with top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy

        # Ball collision with paddles
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dx = -ball_dx

        # Ball out of bounds
        if ball.left <= 0:
            player2_score += 1
            reset_ball()
        if ball.right >= WIDTH:
            player1_score += 1
            reset_ball()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Display scores
        player1_text = font.render(str(player1_score), True, WHITE)
        player2_text = font.render(str(player2_score), True, WHITE)
        screen.blit(player1_text, (WIDTH // 4, 20))
        screen.blit(player2_text, (3 * WIDTH // 4, 20))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

def reset_ball():
    global ball_dx, ball_dy
    ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

if __name__ == "__main__":
    main()
