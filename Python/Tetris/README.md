# Tetris in Python
This repository contains all the files and documentation needed to create Tetris .exe not supported on LINUX

# Dependencies
`pip install pygame`  
`pip install pyinstaller`

# Building
Go into the source folder for the game and type  
`pyinstaller --onefile tetris.py`

This will create four important items:
<pre>
- a main_game_script.spec file in the game_dir
- a 'build' dir in the game_dir
- a 'dist' directory in the game_dir
- a main_game_script.exe will be created in the 'dist' directory.
</pre>

Inside the current folder a file called tetris.spec was created edit it and add the following line(s)  
`a.datas += [('name_of_the_foont.ttf','ABSOLUTE_PATH_TO_FONT', "DATA")]`  
`a.datas += [('sound.mp3','ABSOLUTE_PATH_TO_SOUND', "DATA")]`  
Save and do `pyinstaller tetris.spec`  
It's done the .exe will now have the custom fonts and the game will be playable!
