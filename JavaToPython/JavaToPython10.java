// ChristianThompson.com
// @TokyoEdTech
// Lesson 10: Keyboard Input
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);

      String name;
      int age;
      double height;
      
      System.out.print("What is your name? > ");
      name = sc.nextLine();

      System.out.print("How old are you? > ");
      age = sc.nextInt();

      System.out.print("How tall are you? > ");
      height = sc.nextDouble();

      System.out.println("\nUser Details:");
      System.out.println("Name: " + name + " Age: " + age + " Height: " + height);

  }
}
