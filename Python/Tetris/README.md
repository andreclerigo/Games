# Tetris in Python
This repository contains all the files and documentation needed to create Tetris  

# Dependencies
`pip install pygame`  
`pip install pyinstaller`

# Building
Go into the source folder for the game and type  
`pyinstaller --onefile tetris.py`

This will create four important items:
```
- a main_game_script.spec file in the game_dir
- a 'build' dir in the game_dir
- a 'dist' directory in the game_dir
- a main_game_script.exe will be created in the 'dist' directory.
```
