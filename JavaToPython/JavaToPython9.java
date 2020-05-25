// ChristianThompson.com
// @TokyoEdTech
// Lesson 9: Functions/Methods

class Main {
  public static void main(String[] args) {
    printPi();
    printDouble(2);

    double pi = getPi();
    System.out.println(pi);

    int y = getDouble(4);
    System.out.println(y);

    int greatest = getGreatest(42, 16);
    System.out.println(greatest);

    if(isEven(42)){
      System.out.println("Even!");
    } else {
      System.out.println("Odd!");
    }
  }

  public static void printPi(){
    System.out.println(3.14159);
  }

  public static void printDouble(int x){
    System.out.println(x * 2);
  }

  public static double getPi(){
    return 3.14159;
  }
  
  public static int getDouble(int x){
      return x * 2;
  }

  public static int getGreatest(int x, int y){
    if(x > y){
      return x;
    } else{
      return y;
    }
  }

  public static boolean isEven(int x){
    if(x % 2 == 0){
      return true;
    } else {
      return false;
    }
  }

}
