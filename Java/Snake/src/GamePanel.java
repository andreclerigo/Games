package Snake.src;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import java.util.Random;

/**
 * The classic game Snake on Java!
 * @author André Clérigo
 */
public class GamePanel extends JPanel implements ActionListener {
    private static final long serialVersionUID = 1181129953415591504L;
    static final int SCREEN_WIDTH = 600;  //Window Width
    static final int SCREEN_HEIGHT = 600;  //Window Height
    static final int UNIT_SIZE = 25;  //Square size
    static final int GAME_UNITS = (SCREEN_WIDTH * SCREEN_HEIGHT)/UNIT_SIZE;
    static final int DELAY = 85;  //Pace of the game
    static final int BODY = 5;  //Body count at the beginning

    //Snake won't be bigger then the game space
    final int x[] = new int[GAME_UNITS];  
    final int y[] = new int[GAME_UNITS];

    boolean grid = true;  //Show a grid in-game
    int bodySize = BODY;
    int applesEaten;
    int appleX;
    int appleY;
    int HIGH_SCORE;
    char direction = 'R';
    boolean running = false;    
    Timer timer;
    Random random;
    
    JButton replay = new JButton("Play Again");

    /**
     * At the beginning it retrieves information from the Serialization and if this exists the game will use the High Score stored in there
     * Starts the window with the correct dimensions and starts the game
     */
    GamePanel() {
        try {
            GamePanel g = rescueGame("/temp/SnakeGameInformation.ser");
            HIGH_SCORE = g.HIGH_SCORE;
        } catch(Exception e) {
            e.printStackTrace();
        }
        
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        this.add(replay);
        replay.setVisible(false);
        replay.setBounds(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT - 130, 100, 60);
        startGame();
    }

    /**
     * Starts the game and spawns an apple
     */
    public void startGame() {
        spawnApple();
        running = true;
        timer = new Timer(DELAY, this);
        timer.start();
    }
    

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        draw(g);
    }
    
    /**
     * Calls the gameOver functions when the game isn't running anymore and also paints the snake blocks
     * Also this method is used to paint lines to guide the user (if wanted)
     * @param g graphics used in the game
     */
    public void draw(Graphics g) {
        if(running) {
            if (grid) {
                for(int i = 0; i < SCREEN_HEIGHT/UNIT_SIZE; i++) {
                    g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);  // Draws line from top to bottom
                    g.drawLine(0, i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);  // Draws line from left to right
                }
            }

            g.setColor(Color.RED);
            g.fillOval(appleX, appleY, UNIT_SIZE, UNIT_SIZE);

            for(int i = 0; i < bodySize; i++) {
                if(i != 0) {
                    g.setColor(new Color(45, 180, 0));
                    g.fillRect(x[i], y[i], UNIT_SIZE, UNIT_SIZE);
                } else {
                    g.setColor(Color.GREEN);
                    g.fillRect(x[0], y[0], UNIT_SIZE, UNIT_SIZE);
                }
            }
            
            scoreDisplay(g);
        } else {
            gameOver(g);
        }
    }
    
    /** 
     * Displays the players actual score on the top of the screen
     * @param g graphics used in the game
     */
    public void scoreDisplay(Graphics g) {
        //Drawing apple count
        g.setColor(Color.RED);
        g.setFont(new Font("Arial", Font.BOLD, 40));
        FontMetrics metrics = getFontMetrics(g.getFont());
        //Center the text
        g.drawString("Score: " + applesEaten, (SCREEN_WIDTH - metrics.stringWidth("Score: " + applesEaten))/2, g.getFont().getSize());
    }

    /**
     * Displays the player High Score at game over
     * @param g graphics used in the game
     * @param newHS used to see if it's a new High Score
     */
    public void highScoreDisplay(Graphics g, boolean newHS) {
        //Drawing High Score
        g.setColor(Color.YELLOW);
        g.setFont(new Font("Arial", Font.BOLD, 40));
        FontMetrics metrics = getFontMetrics(g.getFont());
        //Center the text
        if(!newHS)
            g.drawString("High Score: " + HIGH_SCORE, (SCREEN_WIDTH - metrics.stringWidth("High Score: " + HIGH_SCORE))/2, g.getFont().getSize() *2);
        else
            g.drawString("New High Score: " + HIGH_SCORE, (SCREEN_WIDTH - metrics.stringWidth("New High Score: " + HIGH_SCORE))/2, g.getFont().getSize() *2);
    }

    /**
     * Spawns a new apple randomly in the game
     */
    public void spawnApple() {
        appleX = random.nextInt((int)SCREEN_WIDTH/UNIT_SIZE) * UNIT_SIZE;
        appleY = random.nextInt((int)SCREEN_HEIGHT/UNIT_SIZE) *UNIT_SIZE;
    }

    /**
     * Moves the snake head and body
     */
    public void move() {
        //Body movement
        for(int i = bodySize; i > 0; i--) {
            x[i] = x[i-1];
            y[i] = y[i-1];
        }
        
        //Head movement
        switch(direction) {
            case 'U': 
                    y[0] = y[0] - UNIT_SIZE;
                    break;

            case 'D':
                    y[0] = y[0] + UNIT_SIZE;
                    break;

            case 'L':
                    x[0] = x[0] - UNIT_SIZE;
                    break;
            
            case 'R':
                    x[0] = x[0] + UNIT_SIZE;
                    break;
        }
    }

    /**
     * This method checks if the Snake has eaten the apple, if so the snake gets bigger, the score increases and another apple is spawned
     */
    public void checkApple() {
        if((x[0] == appleX) && (y[0] == appleY)) {
            applesEaten++;
            spawnApple();
            bodySize++;
        }
    }
    
    /**
     * This function will check collisions beteween the snake's head with the body and all the borders of the screen
     */
    public void checkCollisions() {
        //Check head touch right border
        if(x[0] >= SCREEN_WIDTH) running = false;

        //Check head touch top border
        if(y[0] < 0) running = false;

        //Check head touch bottom border
        if(y[0] >= SCREEN_HEIGHT) running = false;

        //Check head touch left border
        if(x[0] < 0) running = false;
        
        //Check head collision with body
        for(int i = bodySize; i > 0; i--) {
            if((x[0] == x[i]) && (y[0] == y[i]))
                running = false;
        }

        if(!running) timer.stop();
    }

    /** 
     * Displays the GAME OVER text with the current score, high score of the user and a button to play again
     * @param g graphics used in the game
     */
    public void gameOver(Graphics g) {
        //Game Over text
        g.setColor(Color.RED);
        g.setFont(new Font("Arial", Font.BOLD, 75));
        FontMetrics metrics = getFontMetrics(g.getFont());
        //Center the text
        g.drawString("GAME OVER", (SCREEN_WIDTH - metrics.stringWidth("GAME OVER"))/2, SCREEN_HEIGHT/2);

        scoreDisplay(g);

        // Updates the High Score
        if(applesEaten > HIGH_SCORE) {  
            HIGH_SCORE = applesEaten;
            highScoreDisplay(g, true);
        } else {
            highScoreDisplay(g, false);
        }

        try {
            saveGame("/temp/SnakeGameInformation.ser");
        } catch(Exception e) {
            e.printStackTrace();
        }

        //Play again button
        replay.setVisible(true);
        replay.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(e.getSource() == replay) {
                    JComponent comp = (JComponent) e.getSource();
                    Window win = SwingUtilities.getWindowAncestor(comp);
                    win.dispose();  //It will close the current window
                    new GameFrame();  //It will create a new game
                }
            }
        });
    }

    /**
     * Everytime there an action it moves the snake and checks for collisions if the game isn't over it will repaint the game
     * @param e ActionEvent performed by the user
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        if(running) {
            move();
            checkCollisions();
            checkApple();
        }
        repaint();
    }
    
    /**
     * Saves the game information in the temp folder
     * @param file the path used to store the information for the game
     * @throws IOException
     */
    public void saveGame(String file) throws IOException {
        ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(file));
        out.writeObject(this);
        out.close();
    }

    /**
     * /**
     * Returns an object that contains the game information
     * @param file the path used to retreive the information for the game
     * @return returns an object of GamePanel type with all the information of the previous game
     * @throws IOException
     * @throws ClassNotFoundException
     */
    public GamePanel rescueGame(String file) throws IOException, ClassNotFoundException {
        ObjectInputStream in = new ObjectInputStream(new FileInputStream(file));
		GamePanel g = (GamePanel)in.readObject();
        in.close();
        return g;
    }

    /**
     * KeyAdaptater that accpets input form W,A,S,D and Arrows
     */
    public class MyKeyAdapter extends KeyAdapter {
        /**
         * Changes the direction (char) according to the input
         * @param e KeyEvent that is being listened to
         */
        @Override
        public void keyPressed(KeyEvent e) {
            switch(e.getKeyCode()) {
                case KeyEvent.VK_LEFT:
                                    if(direction != 'R')
                                        direction = 'L';
                                    break;

                case KeyEvent.VK_A:
                                    if(direction != 'R')
                                        direction = 'L';
                                    break;

                case KeyEvent.VK_RIGHT:
                                    if(direction != 'L')
                                        direction = 'R';
                                    break;

                case KeyEvent.VK_D:
                                    if(direction != 'L')
                                        direction = 'R';
                                    break;

                case KeyEvent.VK_UP:
                                    if(direction != 'D')
                                        direction = 'U';
                                    break;

                case KeyEvent.VK_W:
                                    if(direction != 'D')
                                        direction = 'U';
                                    break;

                case KeyEvent.VK_DOWN:
                                    if(direction != 'U')
                                        direction = 'D';
                                    break;
                
                case KeyEvent.VK_S:
                                    if(direction != 'U')
                                        direction = 'D';
                                    break;
            }
        }
    }
}
