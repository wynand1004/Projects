// ChristianThompson.com
// @TokyoEdTech
// Lesson 5: Conditionals

class Main {
  public static void main(String[] args) {
    System.out.println("Does 3 equal 3?");
    if(3 == 3){
      System.out.println(true);
    }

    System.out.println("");
    int x = 3;
    int y = 2;
    System.out.println(String.format("Is %s greater than %s?", x, y));
    if (x > y){
      System.out.println(true);
    } else {
      System.out.println(false);
    }

    System.out.println("");
    x = 2;
    y = 3;
    System.out.println(String.format("Is %s greater than %s?", x, y));
    if (x > y){
      System.out.println(true);
    } else {
      System.out.println(false);
    }

    System.out.println("");
    String playerA = "rock";
    String playerB = "scissors";

    if (playerA.equals("rock") || playerB.equals("rock")){
      System.out.println("Someone chose rock!");
    }

    if (playerA.equals("rock") && playerB.equals("scissors")){
      System.out.println("Player A Wins!");
    } else if (playerA.equals("rock") && playerB.equals("paper")){
      System.out.println("Player B Wins!");
    } else {
      System.out.println("Tie!");
    }

  }
}
