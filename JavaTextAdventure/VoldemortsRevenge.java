import java.util.Scanner;

class VoldemortsRevenge
{
    public static void main(String[] args)
    {
        // Initialize the game
        int score = 0;
        String command = "";
        int room = 1;
        boolean hasAmulet = false;
        
        Scanner sc = new Scanner(System.in);
        
        while(true)
        {
            // Print Room Information
            if(room==1)
            {
                System.out.println("You are in Dumbledore's Office");
                System.out.println("Dumbledore looks worried. There is a magic mirror in the corner.");
            }
            else if(room==2)
            {
                System.out.println("You are on a path.");
                System.out.println("To the north is the Forbidden Forest. To the east, Voldemort's Castle, and to the south, a river.");
            }
            else if(room==3)
            {
                System.out.println("You are at the entrance to Voldemort's Castle.");
                System.out.println("There is a path to the west.");
            }
            
            // Print inventory and score
            System.out.print("You have: ");
            if(hasAmulet)
            {
                System.out.print("amulet ");
            }
            System.out.println();
            System.out.println("Score: " + score);
            
            // Get player command
            System.out.print("> ");
            command = sc.nextLine();
            
            // Deal with player input
            if(room==1)
            {
                if(command.equals("ask dumbledore"))
                {
                    System.out.println("Hermione and Ron have been kidanpped by Lord Voldemort.");
                    System.out.println("You need to rescue them. Here is a magic amulet it will glow when you get close.");
                    System.out.println("When you find them, say 'returnus'");
                    score += 10;
                    hasAmulet = true;
                }
                
                else if(command.equals("exa mirror")||command.equals("exa magic mirror"))
                {
                    System.out.println("The mirror is large and has ancient writing. It says 'To useth this myrror, sayeth thou tralfaz'");
                }
                
                else if(command.equals("say tralfaz"))
                {
                    System.out.println("You float up and through the mirror...");
                    room = 2;
                    score += 10;
                }
                else
                {
                    System.out.println("Sorry, I don't know how to do that.");
                }
            }
            else if(room==2)
            {
                if(command.equals("e"))
                {
                    room=3;
                }
            }
            
        }
    }
}
