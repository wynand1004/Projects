public class BoardA
{
   private String c1 = " ";
   private String c2 = " ";
   private String c3 = " ";
   private String c4 = " ";
   private String c5 = " ";
   private String c6 = " ";
   private String c7 = " ";
   private String c8 = " ";
   private String c9 = " ";
   
   BoardA()
   {
      System.out.println("Board A is Ready!");
   }
   
   public void addMove(String player, int position)
   {
      System.out.println("Player: " + player + " Position: " + position);
      // Check if it is in the right range
      if(position >= 1 && position <= 9)
      {
         if(position == 1 && c1.equals(" "))
         {
            c1 = player;
         }
         else if(position == 2 && c2.equals(" "))
         {
            c2 = player;
         }
         else if(position == 3 && c3.equals(" "))
         {
            c3 = player;
         }
         else if(position == 4 && c4.equals(" "))
         {
            c4 = player;
         }
         else if(position == 5 && c5.equals(" "))
         {
            c5 = player;
         }
         else if(position == 6 && c6.equals(" "))
         {
            c6 = player;
         }
         else if(position == 7 && c7.equals(" "))
         {
            c7 = player;
         }
         else if(position == 8 && c8.equals(" "))
         {
            c8 = player;
         }
         else if(position == 9 && c9.equals(" "))
         {
            c9 = player;
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
      c1 = " ";
      c2 = " ";
      c3 = " ";
      c4 = " ";
      c5 = " ";
      c6 = " ";
      c7 = " ";
      c8 = " ";
      c9 = " ";
   }
   
   public String toString()
   {
      String output = "";
      output += " "+c1+" | "+c2+" | "+c3+" \n";
      output += "-----------\n";
      output += " "+c4+" | "+c5+" | "+c6+" \n";
      output += "-----------\n";      
      output += " "+c7+" | "+c8+" | "+c9+" \n\n";
      
      return output;
   }
}