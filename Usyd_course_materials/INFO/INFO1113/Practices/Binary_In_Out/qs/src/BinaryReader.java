import java.io.*;
public class BinaryReader {
    public static void main(String[] args){
        try{
            FileInputStream f = new FileInputStream("newfile.bin");
            DataInputStream input = new DataInputStream(f);
            int n = input.readInt();
            System.out.println(n);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
