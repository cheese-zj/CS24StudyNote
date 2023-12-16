import java.util.*;
import java.io.*;

public class ooooop {
    public static void print(Object o){
        System.out.println(o);
    }

    public static void main(String[] args){
        File f = new File(".txt");
        String a;
        try {
            Scanner sc = new Scanner(f);
            a = sc.nextLine();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        print(a);

        int x = Integer.parseInt("1");
    }
}
