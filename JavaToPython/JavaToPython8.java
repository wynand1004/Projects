// ChristianThompson.com
// @TokyoEdTech
// Lesson 8: Hashmaps
 
import java.util.HashMap;

class Main {
  public static void main(String[] args) {
    HashMap<String, String> capitals = new HashMap<String, String>();
    String country;
    String capital;

    capitals.put("Japan", "Tokyo");
    capitals.put("China", "Beijing");
    capitals.put("South Korea", "Seoul");

    capital = capitals.get("Japan");
    System.out.println("Japan: " + capital);

    System.out.println("");
    country = "South Korea";
    capital = capitals.get(country);
    System.out.println(country + ": " + capital);

    System.out.println("");
    for (String key : capitals.keySet()){
      capital = capitals.get(key);
      System.out.println(key + ": " + capital);
    } 

  }
}
