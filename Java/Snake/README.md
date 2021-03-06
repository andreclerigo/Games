# The Snake Game in Java

This repository contains all the files and documentation needed to create the Snake Game (This version doesn't support LINUX)
# Executable

The executable file is .jar
Snake  
├── lib  
│   └── font
│   │   ├── Premier2019-rPv9.ttf  
│   │   └── game_over.tff  
├── img  
│   └── playagain.png  
├── src  
│   ├── GameFrame.java  
│   ├── GamePanel.java  
│   └── SnakeGame.java  
└── Game.jar

# Version

Built with JDK version LTS 11.0.10  

# Compiling and Building

Change whatever properties you want inside the GamePanel.java such as Delay(Pace of the game), Screen Width/Height, Square Size and inital body size  
Delete the build folder  
Go inside the Snake/src folder and do `javac -d ./../build *.java`  
Download the manifest.mf and copy lib directory and put both inside the build directory
Go inside the build directory and do `jar -cvmf manifest.mf Game.jar Snake/src/*.class Snake/lib/`  
It's done your Game.jar executes the Snake Game  
  
With VSCode  
Create a Java Project with VSCode and copy the files inside Snake directory  
On the Java Projects side bar select Export Jar and for the main class choose SnakeGame  
A file called java.jar will appear on the root folder and that is the executable for the game  
