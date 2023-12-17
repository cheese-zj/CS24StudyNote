public interface Eat {
    default void drink(){
        System.out.println("I drink milk");
    }
    void eat();
}
