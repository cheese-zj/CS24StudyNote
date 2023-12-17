interface SayHello {
    public default void howAreYou() {
        //hello();
        greeting();
        System.out.println("How are you today?");
    }
    //public void hello();
    public void greeting();
}

public class Hello {
    public static void main(String[] args) {
        SayHello hi = () -> {
            System.out.println("Hello!");
            System.out.println("GO WATCH PLUTO BY NETFLIX.");
        };
        hi.howAreYou();
    }
}
