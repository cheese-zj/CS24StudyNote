public class InterfaceTest{

    public static void main(String[] args){

        Newborn cutie1 = new Newborn("Fiona");

        System.out.println("\nMy name is " + cutie1.getName());

        cutie1.drink();

        cutie1.eat();


        Infant cutie2 = new Infant("Raya");

        System.out.println("\nMy name is " + cutie2.getName());

        cutie2.drink();

        cutie2.eat();

        cutie2.speak();



        Toddler cutie3 = new Toddler("Ted");

        System.out.println("\nMy name is " + cutie3.getName());

        cutie3.drink();

        cutie3.eat();

        cutie3.speak();

        cutie3.walk();

    }

}
