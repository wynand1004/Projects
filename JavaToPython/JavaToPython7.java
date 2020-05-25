// ChristianThompson.com
// @TokyoEdTech
// Lesson 7: Arrays

class Main {
  public static void main(String[] args) {
    int[] scores = new int[3];

    scores[0] = 85;
    scores[1] = 90;
    scores[2] = 100;

    System.out.println("");
    for(int i=0; i<scores.length; i++){
      System.out.println("Score "+i+": "+ scores[i]);
    }

    double averageScore = (scores[0] + scores[1] + scores[2]) / 3.0;
    System.out.println("Average Score: " + averageScore);
    
    int heights[] = {150, 160, 170, 180};
    
    System.out.println("");
    for(int i=0; i<heights.length; i++){
      System.out.println("Height "+i+": "+ heights[i]);
    }
    
    System.out.println("");
    for(int height: heights){
        System.out.println(height);
    }
    
    System.out.println("");
    double averageHeight = (heights[0] + heights[1] + heights[2] + heights[3]) / 4.0;
    System.out.println("Average Height: " + averageHeight);

    

  }
}
