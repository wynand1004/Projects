// ChristianThompson.com
// @TokyoEdTech
// Lesson 11: Classes

class Main {
  public static void main(String[] args) {
    System.out.println("Animals (Three Different Ones)\n");

    Animal lucky = new Animal("Lucky");
    Animal gizmo = new Animal("Gizmo");
    Animal bella = new Animal("Bella");

    lucky.setWeight(20.5);
    gizmo.setWeight(6.2);
    bella.setWeight(5.1);

    System.out.println("Number of Animals: " + Animal.numberOfAnimals);
    
    System.out.println(lucky);
    System.out.println(gizmo);
    System.out.println(bella);
    
    Animal.incrementNumberOfAnimals();
    System.out.println("\nNumber of Animals: " + Animal.numberOfAnimals);

  }
}
