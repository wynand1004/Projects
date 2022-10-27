// Wordle (In the Terminal)
// By @TokyoEdtech
// Java
// Topics: Scanner, substring, loops, ANSI color codes
import java.util.Scanner;

class Wordle
{
    public static void main(String[] args)
    {
        final String BG_GREEN = "\u001b[42m";
        final String BG_YELLOW = "\u001b[43m";
        final String RESET = "\u001b[0m";
        
        System.out.println("WORDLE!");
        
        String[] words = {"SHAKE", "SHARE", "PANIC", "AMUSE", "SHADE"};
        
        int wIndex = (int)(Math.random() * words.length);
        String correct = words[wIndex];
        
        Scanner sc = new Scanner(System.in);
        String guess = ""; 
        
        // Loop for six guesses
        for(int round=0;round<6;round++)
        {
            System.out.print("Please guess. > ");
            guess = sc.nextLine().toUpperCase();
            
            // Create a loop to iterate through each letter
            for(int i=0;i<5;i++)
            {
                if(guess.substring(i, i+1).equals(correct.substring(i, i+1)))
                {
                    // Letter matches
                    System.out.print(BG_GREEN + guess.substring(i, i+1) + RESET);
                }
                else if(correct.indexOf(guess.substring(i, i+1)) > -1)
                {
                    // Letter is in word, but different location
                    System.out.print(BG_YELLOW + guess.substring(i, i+1) + RESET);
                }
                else
                {
                    // Letter not in word
                    System.out.print(guess.substring(i, i+1));
                }
            }
            
            System.out.println("");
            
            // If the guess is correct
            if(guess.equals(correct))
            {
                System.out.println("Correct! You win!");
                break;
            }
            
        }
        
        // Print correct answer if player loses
        if(!guess.equals(correct))
        {
            System.out.println("Wrong! The correct word is " + correct + ".");
        }
    }
}
