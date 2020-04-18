public class TicTacToe
{
   public static void main(String[] args)
   {
      BoardA board = new BoardA();
      // BoardB board = new BoardB();
      
      System.out.println(board);
      board.addMove("X", 10);
      
      board.addMove("X", 5);
      System.out.println(board);
      
      board.addMove("O", 1);
      System.out.println(board);
      
      board.addMove("X", 1);
      System.out.println(board);
      
      board.addMove("X", 2);
      System.out.println(board);
      
      board.addMove("O", 7);
      System.out.println(board);
      
      board.addMove("X", 8);
      System.out.println(board);
      
      board.clear();
      System.out.println(board);
   }
}