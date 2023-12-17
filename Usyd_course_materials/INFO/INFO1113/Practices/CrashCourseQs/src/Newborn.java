public class Newborn extends Child implements Eat {
    public Newborn(String name){
        super(name);
    }
    public void eat(){
        System.out.println("Newborn eating?");
    }
}
