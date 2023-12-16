import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class q14 {
    static void readLongLines(String fileName, int length){
        if (length < 0){
            System.out.println("Invalid length");
        }
        try{
            File f = new File(fileName);
            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()){
                String line = sc.nextLine();
                if(line.length() > length){
                    System.out.println(line);
                }
            }
        } catch(FileNotFoundException e) {
            System.out.println("No such file");
        }
    }

    public static void main(String[] args){
        readLongLines(args[0], Integer.parseInt(args[1]));
    }
}
