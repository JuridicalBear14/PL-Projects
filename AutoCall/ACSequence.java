package AutoCall;

import java.awt.*;
import java.awt.event.InputEvent;
import java.util.ArrayList;
import java.util.TimerTask;

public class ACSequence extends TimerTask{
    double delay;
    ArrayList<Point> tasks = new ArrayList<Point>();

    public ACSequence(){

    }

    /**
     * Method to run the sequence
     * Clicks the cursor at each point
     */
    public void run(){
        Robot mouse;
        try {
            mouse = new Robot();

            int x;
            int y;

            //Loop moves the cursor and clicks at each point
            for (int task = 0; task < tasks.size(); task++){
                x = (int)tasks.get(task).getX();
                y = (int)tasks.get(task).getY();

                mouse.mouseMove(x, y);
                System.out.println("Move to " + x + " " + y);
                mouse.mousePress(InputEvent.BUTTON1_DOWN_MASK);
                System.out.println("Press down");
                Thread.sleep(700);
                mouse.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
                System.out.println("Release");
                Thread.sleep((long) delay);
            }

        } catch (AWTException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    /**
     * Sets the intra-sequence delay
     * @param delay
     */
    public void setDelay(double delay){
        this.delay = delay * 1000; //Times 1000 since Java works in miliseconds
    }

    /**
     * Adds a new task to the sequence
     * @param task
     */
    public void addTask(Point task){
        Point newPoint = new Point();
        newPoint.setLocation(task.getX(), task.getY());
        tasks.add(newPoint);
    }

    /**
     * Clears all tasks in the sequence
     */
    public void clearTasks(){
        tasks.clear();
    }

    /**
     * Returns the number of tasks in the sequence
     * @return
     */
    public int getNumTasks(){
        return tasks.size();
    }

}
