# Pygame is an open-source library that is designed for making video games.
# It has inbuilt graphics and sounds libraries.
# It is beginner-friendly, and cross-platform.
import pygame
import time
import random
# init(): Initializes all of the imported Pygame modules (returns a tuple indicating success and failure of initializations).
pygame.init()
# Display size.
dis_width = 600
dis_height = 400
# Initializing the color variables using RGB color scheme.
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
# Variable defining width and height of snake block.
snake_block = 10
# display.set_mode(): Takes a tuple or a list as its parameter to create a surface (tuple preferred)
dis = pygame.display.set_mode((dis_width, dis_height))
# display.update(): Updates the screen.
pygame.display.update()
# display.set_caption(): Will set the caption text on the top of the display screen.
pygame.display.set_caption('Snake Game by Bunny Studio')
# Create an object to help track time
clock = pygame.time.Clock()
# Speed for movement of snake.
snake_speed = 15
# Create a Pygame font from the System font resources with arguments (Name, Size).
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)
# Defining the snake of length equivalent to number of tuples in snake_list tuple.
# Each tuple is in the form [x1,y1].


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])
# Defining the score.


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
# Message for Game Over.


def message(msg, color):
    # render(): Draw text on a new Surface with arguments (text, anti-alias, color).
    text_surface = font_style.render(msg, True, color)
    # blit(): Take the surface/content from the 1st argument and position it at [x,y] or in center as defined below.
    dis.blit(text_surface, text_surface.get_rect(center=dis.get_rect().center))


def gameLoop():
    # Setting the flag values.
    game_over = False
    game_close = False
    # Variales defining initial position of snake.
    x1 = dis_width/2
    y1 = dis_height/2
    # Variables defining change in position of snake on key press.
    x1_change = 0
    y1_change = 0
    # Will store the tuples in the form of [x1,y1].
    snake_List = []
    # Initially length of snake has to be 01.
    Length_of_snake = 1
    # Variales defining the position of snake food.
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Game Over! Press Q-Quit or C-Play Again", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # event.get(): Returns list of all events take place over screen.
        for event in pygame.event.get():
            # Specifying that the screen should exit on close button.
            if event.type == pygame.QUIT:
                game_over = True
            # Key events are present in the KEYDOWN class of Pygame.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        # fill(): Fill the surface with a solid color.
        dis.fill(black)
        # draw.rect(): Help you draw the rectangle with the desired color and size in format [left,top,width,height].
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        # Creation of tuple that has to be in snake_List in the form of [x1,y1]
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        # snake_List will be of form [[x1,y1],[x1,y1],...,[xn,yn]]
        snake_List.append(snake_Head)
        # One tuple has been added to snake_List on every iteration.
        # This way the length of snake will increase on every iteration.
        # To inhibit the increase in snake's length, untill unless it swallow the food.
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # To let the game over if sanke collides by itself.
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        # Function Call for the display of snake.
        our_snake(snake_block, snake_List)
        # Function Call for the display of score.
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        # To change the location of food, once it get swallowed by the snake.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            # length will increase with every intake of food.
            Length_of_snake += 1
        # Used to help limit the runtime speed (frames per second) of a game.
        clock.tick(snake_speed)
    # quit(): Used to uninitialize everything.
    pygame.quit()
    # quit(): Used to exit the program.
    quit()


gameLoop()
