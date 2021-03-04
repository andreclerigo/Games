package Snake.src;

import javax.swing.JFrame;
import javax.swing.JPanel;

/**
 * Does the JFrame necessary to the game
 * @author André Clérigo
 */
public class GameFrame extends JFrame {
    GameFrame() {
        JPanel panel = new GamePanel();
        this.add(panel);
        panel.setLayout(null);  //Needed to add components
        this.setTitle("Snake Game");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();  //Fit JFrame to the components
        this.setVisible(true);
        this.setLocationRelativeTo(null);
    }
}
