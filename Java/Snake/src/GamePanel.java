package Snake.src;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Random;

/**
 * The classic game Snake on Java!
 * @author André Clérigo
 */
public class GamePanel extends JPanel implements ActionListener {
    private static final long serialVersionUID = 1181129953415591504L;
    static final int SCREEN_WIDTH = 600;
    static final int SCREEN_HEIGHT = 600;
    static final int UNIT_SIZE = 25;
    static final int GAME_UNITS = (SCREEN_WIDTH * SCREEN_HEIGHT)/UNIT_SIZE;
    static final int DELAY = 80;
    static final int BODY = 5;

    //Snake won't be bigger then the game space
    final int x[] = new int[GAME_UNITS];  
    final int y[] = new int[GAME_UNITS];

    int bodySize = BODY;
    int applesEaten;
    int appleX;
    int appleY;
    char direction = 'R';
    boolean running = false;    
    Timer timer;
    Random random;

    JButton replay = new JButton("Play Again");

    GamePanel() {
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(Color.BLACK);
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        this.add(replay);
        replay.setVisible(false);
        replay.setBounds(100,100,100,100);
        startGame();
    }

    /**
     * 
     */
    public void startGame() {
        spawnApple();
        running = true;
        timer = new Timer(DELAY, this);
        timer.start();
    }

    
    /** 
     * @param g
     */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        draw(g);
    }
    
    /**
     * 
     * @param g
     */
    public void draw(Graphics g) {
        if(running) {
            for(int i = 0; i < SCREEN_HEIGHT/UNIT_SIZE; i++) {
                g.drawLine(i*UNIT_SIZE, 0, i*UNIT_SIZE, SCREEN_HEIGHT);  // Draws line from top to bottom
                g.drawLine(0, i*UNIT_SIZE, SCREEN_WIDTH, i*UNIT_SIZE);  // Draws line from left to right
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
     * @param g
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
     * 
     */
    public void spawnApple() {
        appleX = random.nextInt((int)SCREEN_WIDTH/UNIT_SIZE) * UNIT_SIZE;
        appleY = random.nextInt((int)SCREEN_HEIGHT/UNIT_SIZE) *UNIT_SIZE;
    }

    /**
     * 
     */
    public void move() {
        for(int i = bodySize; i > 0; i--) {
            x[i] = x[i-1];
            y[i] = y[i-1];
        }

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
     * This method checks if the Snake has eaten the apple
     */
    public void checkApple() {
        if((x[0] == appleX) && (y[0] == appleY)) {
            applesEaten++;
            spawnApple();
            bodySize++;
        }
    }

    public void checkCollisions() {
        //Check head collision with body
        for(int i = bodySize; i > 0; i--) {
            if((x[0] == x[i]) && (y[0] == y[i]))
                running = false;
        }

        //Check head touch lefr border
        if(x[0] < 0) running = false;
        
        //Check head touch right border
        if(x[0] > SCREEN_WIDTH) running = false;

        //Check head touch bottom border
        if(y[0] > SCREEN_HEIGHT) running = false;

        //Check head touch top border
        if(y[0] < 0) running = false;

        if(!running) timer.stop();
    }

    /** 
     * @param g
     */
    public void gameOver(Graphics g) {
        //Game Over text
        g.setColor(Color.RED);
        g.setFont(new Font("Arial", Font.BOLD, 75));
        FontMetrics metrics = getFontMetrics(g.getFont());
        //Center the text
        g.drawString("GAME OVER", (SCREEN_WIDTH - metrics.stringWidth("GAME OVER"))/2, SCREEN_HEIGHT/2);

        scoreDisplay(g);

        // Botao de play again
        replay.setVisible(true);
        replay.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(e.getSource() == replay) {
                    running = true;
                    bodySize = 5;
                    applesEaten = 0;
                    direction = 'R';
                    replay.setVisible(false);
                    repaint();
                    
                    startGame();
                }
            }
        });
    }

    /**
     * @param e An ActionEvent
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        if(running) {
            move();
            checkApple();
            checkCollisions();
        }
        repaint();
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
