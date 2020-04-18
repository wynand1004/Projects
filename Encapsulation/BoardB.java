public class BoardB
{
   private String[] cells = {" ", " ", " ", " ", " ", " ", " ", " ", " ", " "};
   
   BoardB()
   {
      System.out.println("Board B is Ready!");
   }
   
   public void addMove(String player, int position)
   {
      System.out.println("Player: " + player + " Position: " + position);
      // Check if it is in the right range
      if(position >= 1 && position <= 9)
      {
         if(cells[position].equals(" "))
         {
            cells[position] = player;
         }
         else
         {
            System.out.println("Illegal move. Space is already occupied.\n");
         }
         
      }
      else
      {
         System.out.println("Illegal move. The position must be between 1 and 9.\n");
      }
   }
   
   public void clear()
   {
      System.out.println("Clear Board\n");
      for(int position=1;position<10;position++)
      {
         cells[position] = " ";
      }
   }
   
   public String toString()
   {
      String output = "";
      output += " "+cells[1]+" | "+cells[2]+" | "+cells[3]+" \n";
      output += "-----------\n";
      output += " "+cells[4]+" | "+cells[5]+" | "+cells[6]+" \n";
      output += "-----------\n";      
      output += " "+cells[7]+" | "+cells[8]+" | "+cells[9]+" \n\n";
      
      return output;
   }
}