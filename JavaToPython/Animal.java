public class Animal
{
    public int age;
    protected double weight;
    private String name;

    public static int numberOfAnimals = 0;

    Animal(String name)
    {
        this.name = name;
        numberOfAnimals++;
    }

    public void setWeight(double newWeight)
    {
        weight = newWeight;
    }

    public double getWeight()
    {
        return weight;
    }

    public static void incrementNumberOfAnimals()
    {
        numberOfAnimals++;
    }

    public String toString()
    {
        return "Name: " + name + " Weight: " + getWeight();
    }

}
