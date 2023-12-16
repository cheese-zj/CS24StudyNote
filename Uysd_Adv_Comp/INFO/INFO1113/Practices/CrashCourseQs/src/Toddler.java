public class Toddler extends Walk{
    private String name;
    public Toddler(String name){
        this.name = name;
    }
    public String getName(){
        return this.name;
    }

    public void walk(){
        System.out.println("Imagine toddler actually walking, INSANE");
    }
}
