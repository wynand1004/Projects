// ChristianThompson.com
// @tokyoedtech
// Lesson 3: Strings

class Main {
  public static void main(String[] args) {
    String name = "Robert Smith";
    System.out.println(name);
    System.out.println(name.length());

    System.out.println();
    System.out.println("name");
    System.out.println("Name: " + name);
    System.out.println(String.format("Name: %s", name));

    System.out.println();
    System.out.println("String Methods");
    System.out.println("heLLo".toUpperCase());
    System.out.println("heLLo".toLowerCase());


    System.out.println();
    System.out.println("Substrings");
    System.out.println("good morning".substring(0, 4));
    System.out.println("good morning".substring(5, 12));
    System.out.println("good morning".substring(5, 6));
    System.out.println("good morning".substring(5));
  }
}
