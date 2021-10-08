from guizero import App, Box, Picture, PushButton
import os
from random import shuffle

emojis = [os.path.join('assets', f) for f in os.listdir('assets')]
shuffle(emojis)

def setup():
    for picture in pictures:
        picture.image = emojis.pop()
    
    for button in buttons:
        button.image = emojis.pop()

app = App("Emoji Match Game")
pictures_box = Box(app, layout='grid')
buttons_box = Box(app, layout='grid')

pictures = []
buttons = []

for x in range(0, 3):
    for y in range(0, 3):
        picture = Picture(pictures_box, grid=[x, y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid=[x, y])
        buttons.append(button)

setup()
app.display()