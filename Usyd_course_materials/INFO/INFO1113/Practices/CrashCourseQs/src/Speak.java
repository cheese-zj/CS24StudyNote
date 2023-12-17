public interface Speak extends Eat {
    default void eat(){
        System.out.println("I eat solid food now");
    }
    void speak();
}
