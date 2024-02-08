import pygame
import random
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 502
SCREEN_HEIGHT = 760

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
FONT_SIZE = 24
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
score = 0
lives = 3
game_over = False

def draw_asteroid(expression_str, x, y, asteroid_image):
    # Load font and render text
    font = pygame.font.Font(None, FONT_SIZE)
    text_surface = font.render(expression_str, True, WHITE)
    
    # Get the dimensions of the text surface
    text_width, text_height = text_surface.get_size()
    
    # Calculate the position to center-align the text within the rectangle
    text_x = x + (asteroid_image.get_width() - text_width) // 2
    text_y = y + (asteroid_image.get_height() - text_height) // 2 + 25
    
    # Blit asteroid image onto the screen
    screen.blit(asteroid_image, (x, y))
    
    # Blit text onto the screen at the center position
    screen.blit(text_surface, (text_x, text_y))

asteroid_image = pygame.image.load(r"C:\Users\hp5cd\Downloads\asteroid2.png")

# Function to generate a random mathematical expression
def generate_expression():
    global eqn1
    eqn = "ax^3+bx^2+cx+d"
    dic = {"a":random.randint(0,3),"b":random.randint(0,3),"c":random.randint(0,3),"d":random.randint(0,3)}
    for x in list(dic.keys())[0:3]:
        if dic[x]==1:
            dic.update({x:""})
    for x in dic.keys():
        for y in eqn:
            if y==x:
                eqn = eqn.replace(y,str(dic[x]))
    l = eqn.split("+")
    l1=[]
    for index,x in enumerate(l):
        if "0" in x:
            continue
        l1.append(x)
    eqn = "+".join(l1)
    l2=[]
    for x in eqn:
        if x=="^":
            l2.append("")
        else:
            l2.append(x)    
    eqn1="".join(l2)
    return str(eqn1)

def generate_point():
    global b
    numbers = [0,1,2,3,4]
    b=random.choice(numbers)
    return b

# Function to calculate the derivative of an expression
def calculate_derivative(eqn1,b):
    l3=[]
    x1=b
    for y in eqn1.split("+"):
        try:
            if y.index("x")!=0:
                if y[y.index("x")-1].isnumeric()==True:
                    l3.append(y.replace("x",f"*{b}"))
                else:
                    l3.append(str(b))
            else:
                l3.append(y.replace("x",str(b)))
        except:
                l3.append(y)
    #print(l3)
    try:
        y1=eval("+".join(l3))
    except: pass
    #print(y1)
    x2=x1-0.005
    l4=[]
    for y in eqn1.split("+"):
        try:
            if y.index("x")!=0:
                if y[y.index("x")-1].isnumeric()==True:
                    l4.append(y.replace("x",f"*{x2}"))
                else:
                    l4.append(str(x2))
            else:
                l4.append(y.replace("x",str(x2)))
        except:
                l4.append(y)

    y2 = eval("+".join(l4))
    slope = round((y1-y2)/(x1-x2))
    #print(slope)
    return slope

# Function to display text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw rectangles representing expressions
def draw_expression_rect(expression_str, x, y, color):
    rect_width = 200
    rect_height = 50
    pygame.draw.rect(screen, color, (x, y, rect_width, rect_height))
    draw_text(expression_str, BLACK, x + 10, y + 10)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Derivative Drop")

clock = pygame.time.Clock()

# Timer variables
last_drop_time = 0
drop_interval = 3000  # Drop every 3 seconds (in milliseconds)

# User input variables
input_text = ""
input_rect = pygame.Rect(10, SCREEN_HEIGHT - 40, SCREEN_WIDTH - 20, 30)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
bg = pygame.image.load(r"C:\Users\hp5cd\Downloads\SPACE THEME FINAL (2).png")

expression = generate_expression()
number = generate_point()
expression_str = str(expression)+" at "+str(number)
#last_drop_time = current_time
# Initial position of the falling rectangle
rect_x = random.randint(0, SCREEN_WIDTH - 200)  # Random x-coordinate within screen width
rect_y = 50  # Start above the screen
# Reset color
rect_color = (255, 165, 0)

# Main game loop
while not game_over:
    #screen.fill(BLACK)
    screen.blit(bg, (0, 0))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box, toggle active
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False
            # Change the color of the input box
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            # If the input box is active, handle text input
            if active:
                if event.key == pygame.K_RETURN:
                    if input_text == "":
                        # If the input is empty, do nothing
                        pass
                    else:
                        # Check if the entered derivative is correct
                        expression = generate_expression()
                        number = generate_point()
                        derivative = calculate_derivative(str(expression), number)
                        #derivative = str(derivative.subs(x,number))
                        derivative_str = str(derivative)
                        if input_text == derivative_str:
                            # Change color to blue
                            expression, number = generate_expression()
                            expression_str = str(expression)+" at "+str(number)
                            last_drop_time = current_time
                            # Initial position of the falling rectangle
                            rect_x = random.randint(0, SCREEN_WIDTH - 200)  # Random x-coordinate within screen width
                            rect_y = 50  # Start above the screen
                            # Reset color
                            rect_color = (255, 165, 0)
                            # Increase score by 1
                            score += 1
                            input_text = " "
                            pygame.display.flip()
                        input_text = ' '
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace key
                    input_text = input_text[:-1]
                else:
                    # Append characters to the input text
                    input_text += event.unicode

    # Draw input box
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = font.render(input_text, True, WHITE)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Calculate time since the last drop
    current_time = pygame.time.get_ticks()
    time_since_last_drop = current_time - last_drop_time

    # Drop a new rectangle if enough time has passed
    #print(rect_y)
    if rect_y>=550:
        # Generate falling rectangle
        expression = generate_expression()
        number = generate_point()
        expression_str = str(expression)+" at "+str(number)
        last_drop_time = current_time
        # Initial position of the falling rectangle
        rect_x = random.randint(0, SCREEN_WIDTH - 200)  # Random x-coordinate within screen width
        rect_y = 50  # Start above the screen
        # Reset color
        rect_color = (255, 165, 0)

    # Draw falling rectangle
    #draw_expression_rect(expression_str, rect_x, rect_y, rect_color)
    draw_asteroid(expression, rect_x, rect_y, asteroid_image)
    # Update rectangle's y-coordinate for falling effect
    rect_y += 1.5  # Adjust falling speed as needed

    # If the rectangle reaches the bottom of the screen
    if rect_y >= 500:
        # Change color to red
        #rect_color = RED
        # Decrease score by 1
        score = -1
        #screen.blit(blast, (0, 400))
    
    # Calculate and display derivative
    derivative = calculate_derivative(str(expression), number)
    derivative_str = str(derivative)
    #draw_text(f"Derivative: {derivative_str}", WHITE, SCREEN_WIDTH / 2 - 100, 70)

    # Draw score
    draw_text(f"Score: {score}", WHITE, 20, 20)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
