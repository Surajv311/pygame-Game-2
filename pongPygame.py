import pygame
whiteColor = (255, 255, 255)
blueColor = (0, 0, 255)
redColor = (255, 0, 0)
greenColor = (0, 255, 0)
blackColor = (0, 0, 0)
pygame.init()
# Initializing pygame
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong game")
# Starting coordinates of the base rectangle
baseRectangle_x = 400
baseRectangle_y = 580
# initial speed of the base ractangle
base_r_X = 0
base_r_Y = 0
# initial position of the ball
ball_x = 50
ball_y = 50
# speed of the ball
ball_change_x = 5
ball_change_y = 5
score = 0
# draws the paddle. Also restricts its movement between the edges
# of the window.
def drawrect(screen, x, y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    pygame.draw.rect(screen, blackColor, [x, y, 100, 20])
# game's main loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                base_r_X = -6
            elif event.key == pygame.K_RIGHT:
                base_r_X = 6
            # elif event.key == pygame.K_UP:
            # base_r_Y = -6
            # elif event.key == pygame.K_DOWN:
            # base_r_Y = 6'''
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                base_r_X = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                base_r_Y = 0
    screen.fill(whiteColor)
    baseRectangle_x += base_r_X
    baseRectangle_y += base_r_Y
    ball_x += ball_change_x
    ball_y += ball_change_y
    # this handles the movement of the ball.
    if ball_x < 0:
        ball_x = 0
        ball_change_x = ball_change_x * -1
    elif ball_x > 785:
        ball_x = 785
        ball_change_x = ball_change_x * -1
    elif ball_y < 0:
        ball_y = 0
        ball_change_y = ball_change_y * -1
    elif ball_x > baseRectangle_x and ball_x < baseRectangle_x + 100 and ball_y == 565:
        ball_change_y = ball_change_y * -1
        score = score + 1
    elif ball_y > 600:
        ball_change_y = ball_change_y * -1
        score = 0
    pygame.draw.rect(screen, redColor, [ball_x, ball_y, 15, 15])
    # drawball(screen,ball_x,ball_y)
    drawrect(screen, baseRectangle_x, baseRectangle_y)
    # score board
    font = pygame.font.SysFont('Sans', 25, False, False)
    text = font.render("Score = " + str(score), True, greenColor)
    screen.blit(text, [600, 100])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()