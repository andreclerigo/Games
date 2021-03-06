package Snake.src;

import java.nio.file.*;

public class SnakeGame {
    /**
     * Starts the game
     * @param args the command line arguments - unused
     * @throws Exception
     * @author André Clérigo
     * @version 1.00 Windows and Linux Supported
     */
    public static void main(String[] args) throws Exception {
        Path path = Paths.get("/temp/");
        if(!isUnix()) {
            try {
                if (!Files.exists(path))
                    Files.createDirectory(path);
            } catch(Exception e) {
                e.printStackTrace();
            }
        }

        new GameFrame();
    }

    /**
     * Getting the OS name
     * @return returns a String with the name of the OS
     */
    public static String getOsName() {
        String OS = null;
        if(OS == null) { OS = System.getProperty("os.name"); }
        return OS;
    }

    /**
     * Tells if the system is UNIX
     * @return when true the OS is LINUX
     */
    public static boolean isUnix() { return getOsName().startsWith("Linux"); }
}
