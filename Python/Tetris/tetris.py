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
 

class Piece(object):
    #Constructor for the shape
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]  #Get the color by the shape_colors list
        self.rotation = 0

def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(grid_columns)] for x in range(grid_rows)]  #Create a 10 by 20 grid with the color black(0,0,0)

    for i in range(len(grid)):  #Rows
        for j in range(len(grid[i])):  #Columns
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c

    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]  #Make a list of empty positions
    accepted_pos = [j for sub in accepted_pos for j in sub]  #Flatten the list

    formated = convert_shape_format(shape)

    for pos in formated:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


#Generate a random shape
def get_shape():
    #Generate the piece in the middle of the screen and on the top
    return Piece(grid_columns/2 , 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):  #Rows
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i*block_size), (sx + play_width, sy + i*block_size))
        for j in range(len(grid[i])):  #Columns
            pygame.draw.line(surface, (128, 128, 128), (sx, j*block_size, sy), (sx + j*block_size, sy + play_height))
    

def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass


def draw_window(surface, grid):
    surface.fill((0, 0, 0))

    pygame.font.init()

    #Type of font
    font = pygame.font.SysFont('arial black', 60)
    label = font.render('Tetris', 1, (255, 255, 255))  #Label text, antialiasing, color

    surface.blit(label, (top_left_x + play_height/2 - (label.get_width()/2), 30))  #Center the label on the screen
    
    draw_grid(surface, grid)

    pygame.display.update()
  

def main(win):
    locked_positions = {}

    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                #Python doesn't have switch case? rlly?
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
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -=1

        draw_window(win, grid)


def main_menu(win):
    main(win)


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)