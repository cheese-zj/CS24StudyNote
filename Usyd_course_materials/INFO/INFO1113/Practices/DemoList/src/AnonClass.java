public class AnonClass {

    public static void main(String[] main){
        TestClass obj1 = new TestClass() {
            public void displayIt() {
                System.out.println("Definitely a anon class");
            }

            public void displayAbs(){
                System.out.print("\nPrinting in abstract method.");
            }
        };
        obj1.displayIt();
        obj1.disSome();
        obj1.displayAbs();
    }
}

abstract class TestClass{
    public void displayIt(){
        System.out.println("Something");
    }

    public void disSome(){
        System.out.println("Something222");
    }

    public abstract void displayAbs();
}

