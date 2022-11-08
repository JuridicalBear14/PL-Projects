package AutoCall;

import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;
import java.util.Timer;

import javax.swing.*;
import javax.swing.text.JTextComponent;

public class AutoCall {
    static ACSequence[] sequences = new ACSequence[5];
    public static void main(String[] args) throws FileNotFoundException {
        //System.out.println("Hello World");
        JFrame window = new JFrame("AutoCall");

        //Sets the location of the window
        window.setSize(400, 200);
        window.setLocationRelativeTo(null);
        GridLayout layout = new GridLayout(2, 2);
        window.setLayout(layout);
        window.setLocation(100, 100);
        

        //Sets up text
        JLabel text = new JLabel("AutoCall", JLabel.CENTER);
        window.add(text);

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        //Sets up button
        JButton PFButton = new JButton("PointFinder");
        window.add(PFButton);
        PFButton.addActionListener(new ActionListener(){

            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    PointFinder();
                } catch (InterruptedException e1) {
                    // TODO Auto-generated catch block
                    e1.printStackTrace();
                }
                
            }
        });

        window.setVisible(true);

        String tasks = readData() + "";

        text.setText("Scheduled " + tasks + " sequences"); //Reads data and schedules timers, then returns the number of sequences scheduled
        
    }

    /**
     * Reads the data from the text file
     * Returns number of scheduled sequences
     * @throws FileNotFoundException
     */
    public static int readData() throws FileNotFoundException{
        File data = new File("AutoCall\\AutoCallData.txt");
        Scanner reader = new Scanner(data);
        Timer timer = new Timer();

        int tally = 0; //Tally of how many scheduled tasks, for checking later
        String time;

        reader.next(); //Skips the first words
        reader.next();
        double delay = reader.nextDouble();
        reader.next();


        //System.out.println(delay);

        //Loop to go through the sequences
        for (int seqNum = 0; seqNum < 5; seqNum++){
            sequences[seqNum] = new ACSequence(); //Initializes sequences

            //Parse out time
            reader.next(); //Jumps the scanner forward past the UI text
            time = reader.next();


            //Go to next, if the item is a dash or the word "sequence" then it skips, otherwise read as a number

            //System.out.println(time);

            if (!(time.equals("sequence") || time.equals("-"))){ //Stops the loop and goes to the next item if this one is empty
                //Calculate how long until that time
                Calendar calendar = Calendar.getInstance();
                int hour = Integer.parseInt(time.substring(0, 2));
                int minute = Integer.parseInt(time.substring(3));

                //This will find the number of hours and minutes from current time to given time
                hour -= calendar.get(Calendar.HOUR);
                if (hour < 0){
                    hour += 24;
                }

                minute = calendar.get(Calendar.MINUTE) - minute;
                minute *= -1;

                //Progresses the calendar forward to get a date object for scheduling the sequence
                calendar.add(Calendar.HOUR, hour);
                calendar.add(Calendar.MINUTE, minute);
                Date date = calendar.getTime();

                boolean loop = true; //Bool to stop the while loop
                Point task = new Point();
                //Loop that runs until it hits the end of the sequence's tasks
                while(loop){
                    if (reader.next().equals("-")){ //If the next line is a task, makes it a point object and adds it to the current sequence
                        task.setLocation(reader.nextInt(), reader.nextInt());
                        System.out.println(task);
                        sequences[seqNum].addTask(task);
                    } else {
                        loop = false;
                    }
                }

                //System.out.println("Test");

                //Sets the timer for the sequence
                sequences[seqNum].setDelay(delay);
                timer.schedule(sequences[seqNum], date);

                System.out.println("Scheduled Sequence: " + sequences[seqNum] + " for time: " + hour + ":" + minute);
                tally++;

            } else {
                seqNum += 10; //Exits loop if the next sequence has no time
            }

        }
    
        System.out.println("Scheduled " + tally + " tasks");


        reader.close();

        return(tally);
    }

    /**
     * Method that opens a window for finding coordinate points on the screen
     * @throws InterruptedException
     */
    public static void PointFinder() throws InterruptedException{
        //Window for pointfinder
        JFrame PFWindow = new JFrame("PointFinder");
        GridLayout layout = new GridLayout(2, 1);

        PFWindow.setSize(400, 200);
        PFWindow.setLocationRelativeTo(null);
        PFWindow.setLayout(layout);
        PFWindow.setLocation(300, 300);
        PFWindow.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        //Point text
        JLabel point = new JLabel("Position", JLabel.CENTER);
        PFWindow.add(point);

        PFWindow.setVisible(true);



       //button that starts a timer before recording position
        JButton posButton = new JButton("Find point");
        PFWindow.add(posButton);
        posButton.addActionListener(new ActionListener(){

            @Override
            public void actionPerformed(ActionEvent e) {
                double x;
                double y;

                try {
                    Thread.sleep(3000);

                    x = MouseInfo.getPointerInfo().getLocation().getX();
                    y = MouseInfo.getPointerInfo().getLocation().getY();
            
                    point.setText("X = " + x + " Y = " + y);
                } catch (InterruptedException e1) {
                    // TODO Auto-generated catch block
                    e1.printStackTrace();
                }
                
            }
        });
    }
}