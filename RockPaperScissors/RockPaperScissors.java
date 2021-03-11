// Simple Rock Paper Scissors Tutorial
// by @TokyoEdtech
// Java using Geany Editor
// Ubuntu Linux (Mac and Windows Compatible)

// Topics: Scanner, Strings, Random
import java.util.Scanner;
import java.util.Random;

class RockPaperScissors
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        int num;
        String userChoice = "";
        String computerChoice = "";
        
        System.out.println("Welcome to Rock, Paper, and Scissors!");
        System.out.print("Please choose R)ock, P)aper, or S)cissors. > ");
        
        userChoice = sc.nextLine();
        
        // Computer choice
        num = rand.nextInt(3);
        
        if(num == 0)
        {
            computerChoice = "R";
        }
        else if(num == 1)
        {
            computerChoice = "P";
        }
        else if(num == 2)
        {
            computerChoice = "S";
        }
        
        // Print the computer choice
        if(computerChoice.equals("S"))
        {
            System.out.println("The computer chose scissors.");
        }
        
        else if(computerChoice.equals("R"))
        {
            System.out.println("The computer chose rock.");
        }
        
        else if(computerChoice.equals("P"))
        {
            System.out.println("The computer chose paper.");
        }
        
        // Determine a winner
        if(userChoice.equals("R") && computerChoice.equals("S"))
        {
            System.out.println("The user won!");
        }
        
        else if(userChoice.equals("P") && computerChoice.equals("R"))
        {
            System.out.println("The user won!");
        }
        
        else if(userChoice.equals("S") && computerChoice.equals("P"))
        {
            System.out.println("The user won!");
        }
        
        else if(userChoice.equals("S") && computerChoice.equals("R"))
        {
            System.out.println("The computer won!");
        }
        
        else if(userChoice.equals("R") && computerChoice.equals("P"))
        {
            System.out.println("The computer won!");
        }
        
        else if(userChoice.equals("P") && computerChoice.equals("S"))
        {
            System.out.println("The computer won!");
        }
        
        else if(userChoice.equals(computerChoice))
        {
            System.out.println("Tie!");
        }
    }
}
