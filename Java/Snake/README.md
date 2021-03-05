# The Snake Game in Java
This repository contains all the files and documentation needed to create the Snake Game 
# Executable
The executable file is .jar (Not working for LINUX)  
Snake  
├── build  
|   └── Game.jar  
├── src  
│   ├── GameFrame.java  
│   ├── GamePanel.java  
│   └── SnakeGame.java  
 
# Version
Built with java version LTS 11.0.10  

# Compiling and Building
Change whatever properties you want inside the GamePanel.java such as Delay(Pace of the game), Screen Width/Height, Square Size and inital body size  
Delete the build folder  
Go inside the Snake/src folder and do `javac -d ./build *.java`  
Download the manifest.mf and keep the 2 empty lines after the text  
Then do `jar -cvmf manifest.mf Game.jar Snake/src/*.class`  
It's done your Game.jar executes the Snake Game  
