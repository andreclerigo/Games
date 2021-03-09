import sys
import os
import pygame
import random
from pygame import draw
from pygame.display import update
from pygame.version import PygameVersion
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()
 
s_width = 800  #Screen width
s_height = 700  #Screen height
play_width = 300  #300 // 10 = 30 width per block
play_height = 600  #600 // 20 = 30 height per block
block_size = 30
grid_rows = 20
grid_columns = 10
 
top_left_x = (s_width - play_width) // 2  #Play area
top_left_y = s_height - play_height 
 
#Shape formats
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
 
shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

#Contrustor for the Piece (Shape in-game)
class Piece(object):
    #Constructor for the shape
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]  #Get the color by the shape_colors list
        self.rotation = 0


#Create and define the grid for the game
def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(grid_columns)] for x in range(grid_rows)]  #Create a 10 by 20 grid with the color black(0,0,0)

    for i in range(len(grid)):  #Rows
        for j in range(len(grid[i])):  #Columns
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


#Conver the shape (list of dots and zeros) to a format interpreted by the game
def convert_shape_format(shape):
    positions = []  #Positions that the shape will occupy
    
    format = shape.shape[shape.rotation % len(shape.shape)]  #The shape will always have one of the rotations no matter the rotation counter (using mod)

    for i, line in enumerate(format):
        row = list(line)                    #Will get the row on the shape [..0..] and iterate it
        for j, column in enumerate(row):    #Will iterate the columns on the row (getting the character '.' or '0')
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)  #The object will be created above the play screen so the piece is already sliding down

    return positions


#Returns if the movement is to a valid position (a position that the piece can go onto)
def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]  #Make a list of empty positions (color is black)
    accepted_pos = [j for sub in accepted_pos for j in sub]  #Flatten the list

    formated = convert_shape_format(shape)  #Get the shape on the correct format

    for pos in formated:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


#Returns if the game is lost
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


#Generate a random shape
def get_shape():
    global shapes, shape_colors

    #Generate the piece in the middle of the screen and on the top
    return Piece(grid_columns//2 , 0, random.choice(shapes))


#General function used to write any text ont the middle of the window
def draw_text_middle(text, size, color, surface):
    font = pygame.font.Font(resource_path("game_over.ttf"), size)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width()/2), top_left_y +  (play_height / 2) - (label.get_height())))


#Draws the grid (the playable area)
def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):  #Rows
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*block_size), (sx + play_width, sy + i*block_size))  #Horizontal lines
        for j in range(len(grid[i])):  #Columns
            pygame.draw.line(surface, (128,128,128), (sx + j*block_size, sy), (sx + j*block_size, sy + play_height))  #Vertical lines
    

#Delete complete rows
def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):  #Loop the row backwards
        row = grid[i]

        #If the row doesn't contain a black squares
        if (0, 0, 0) not in row:  
            inc += 1                #Number of rows going to be deleted
            ind = i                 
            for j in range(len(row)):
                try:
                    del locked[(j, i)]  #Delete the row
                except:
                    continue
    
    if inc > 0:  #If a row has been deleted
        #Sort the locked list by yaxis value and iterate it backwards
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


#Draws the next shape outside the playable area so the player can know what's next
def draw_next_shape(shape, surface):
    font = pygame.font.Font(resource_path("Premier2019-rPv9.ttf"), 30)  #Type of font and size
    label = font.render('Next Shape', 1, (255, 255, 255))  #Text, antialiasing and color

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation  % len(shape.shape)]

    #Iterate through the coordinates of the shape and draw it
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 45))  #Position the next shape on the window outside the grid (change the constants to ger)


#Draws the window (not to be confuse with the grid)
def draw_window(surface, grid, score=0):
    surface.fill((0, 0, 0))  #Fill the window with black background

    font = pygame.font.Font(resource_path("Premier2019-rPv9.ttf"), 70)  #Type of font and size
    label = font.render('Tetris', 1, (255, 255, 255))  #Label text, antialiasing, color

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 10))  #Center the title on the screen
    
    font = pygame.font.Font(resource_path("Premier2019-rPv9.ttf"), 30)  #Type of font and size
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))  #Text, antialiasing and color

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx + 30, sy + 180))  #Set the source text on the correct place

    #Information text for mute
    font = pygame.font.Font(resource_path("Premier2019-rPv9.ttf"), 30)  #Type of font and size
    label = font.render('Press M to mute', 1, (255, 255, 255))  #Text, antialiasing and color
    surface.blit(label, ((top_left_x - label.get_width())/2 , top_left_y + play_height - label.get_height()))

    for i in range(len(grid)):  #Rows
        for j in range(len(grid[i])):  #Columns
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* block_size, top_left_y + i * block_size, block_size, block_size), 0)
    
    draw_grid(surface, grid)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)  #Draw the rectangle that limits the play space
  

def main(win):
    pygame.init()
    pygame.mixer.music.load(resource_path("tetris-gameboy-02.mp3"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    locked_positions = {}

    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    paused = False
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        
        if level_time/1000 > 30:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid) and current_piece.y > 0):
                current_piece.y -=1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.mixer.music.stop()
                pygame.display.quit()
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                #Python doesn't have a proprietary switch case structurer -.-
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -=1

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -=1

                elif event.key == pygame.K_SPACE:
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                        pygame.display.update()
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -=1

                elif event.key == pygame.K_m:
                    if paused:
                        paused = False
                        pygame.mixer.music.unpause()
                    else:
                        paused = True
                        pygame.mixer.music.pause()

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions)*10

        
        draw_window(win, grid, score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            win.fill((0, 0, 0))
            draw_text_middle("GAME OVER", 300, (255, 0, 0), win)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False


def main_menu(win):
    run = True
    while run:
        #Waiting screen for the player to be ready
        win.fill((0, 0, 0))
        draw_text_middle("Press Any Key To Play", 150, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)