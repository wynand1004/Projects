// ChristianThompson.com
// @tokyoedtech
// Lesson 6: Loops

class Main {
  public static void main(String[] args) {
    for (int x=0; x<10; x++){
      System.out.println(x);
    }

    System.out.println("");
    for (int x=0; x<10; x+=2){
      System.out.println(x);
    }    

    System.out.println("");
    for (int x=10; x>=0; x--){
      System.out.println(x);
    }      

    System.out.println("");
    String title = "Pictures of You";
    for(int i=0;i<title.length();i++){
      char letter = title.charAt(i);
      System.out.println(letter);
    }

    System.out.println("");
    for(int i=0;i<title.length();i++){
      System.out.println(title.substring(i,i+1));
    }

    System.out.println("");
    for(char letter : title.toCharArray()) {
      System.out.print(letter);
    }

    System.out.println("");
    int i = 0;
    while(i<title.length()){
      char letter = title.charAt(i);
      System.out.print(letter);
      i++;
    }
    
  }
}
