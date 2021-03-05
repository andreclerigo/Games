# The Snake Game in Java
This repository contains all the files and documentation needed to create the Snake Game<br>
# Executable
The executable file is .jar (Not working for LINUX)<br>
Snake<br>
├── build<br>
|   └── Game.jar<br>
├── src<br>
│   ├── GameFrame.java<br>
│   ├── GamePanel.java<br>
│   └── SnakeGame.java<br>
<br>
# Version
Built with java version LTS 11.0.10<br>

# Compiling and Building
Change whatever properties you want inside the GamePanel.java such as Delay(Pace of the game), Screen Width/Height, Square Size and inital body size<br>
Delete the build folder<br>
Go inside the Snake/src folder and do `javac -d ./build *.java`<br>
Download the manifest.mf and keep the 2 empty lines after the text<br>
Then do `jar -cvmf manifest.mf Game.jar Snake/src/*.class`<br>
It's done your Game.jar executes the Snake Game<br>