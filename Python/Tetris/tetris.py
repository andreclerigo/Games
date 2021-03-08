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
    pass
 
def valid_space(shape, grid):
    pass
 
def check_lost(positions):
    pass

#Generate a random shape
def get_shape():
    #Generate the piece in the middle of the screen and on the top
    return Piece(grid_columns/2 , 0, random.choice(shapes))
 
def draw_text_middle(text, size, color, surface):
    pass
   
def draw_grid(surface, grid):  #Rows
    for i in range(len(grid)):  #Columns
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

def clear_rows(grid, locked):
    pass
 
def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    surface.fill({0, 0, 0})

    pygame.font.init()

    #Type of font
    font = pygame.font.SysFont('arial', 60)
    label = font.render('Tetris', 1, (255, 255, 255))  #Label text, antialiasing, color

    surface.blit(label, (top_left_x + play_height/2 - (label.get_width()/2), 30))  #Center the label on the screen
    
    draw_grid()

    pygame.display.update()
    
def main():
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
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    current_piece.x += 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    current_piece.rotation += 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    current_piece.x -= 1
                    
def main_menu():
    run = True
    
 
main_menu()