package Snake.src;

import java.nio.file.*;

public class SnakeGame {
    /**
     * Starts the game
     * @param args the command line arguments - unused
     * @throws Exception
     * @author André Clérigo
     */
    public static void main(String[] args) throws Exception {
        Path path = Paths.get("/temp/");
        try {
            if (!Files.exists(path))
                Files.createDirectory(path);
        } catch(Exception e) {
            e.printStackTrace();
        }
        new GameFrame();
    }
}
