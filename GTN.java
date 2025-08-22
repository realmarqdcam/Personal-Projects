import java.util.Random;
import java.util.Scanner;

public class GTN {
    public static void main ( String [] args ) {
        Random lump = new Random();
        Scanner plug = new Scanner(System.in);

        int winner = lump.nextInt(0, 100);
        int guessCount = 0;

        System.out.println("Welcome to the Guessing Number Game!");
        System.out.println("I am thinking of a number....");


        while (true) {

            System.out.println("Guess count: " + guessCount);
            System.out.print("Guess the number: ");
                int guess = plug.nextInt();

        if (guess == winner) {
            System.out.println("Congratulations! You guessed correctly!");
            guessCount++;
            System.out.println("It took you " + guessCount + " attempts.");
            break;
        } else if ( guess != winner ) {
            System.out.println("Sorry, that's not correct. Try again.");
            guessCount++;
        }

        }

        plug.close();
    }
}