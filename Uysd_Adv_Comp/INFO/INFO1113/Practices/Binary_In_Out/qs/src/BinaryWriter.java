import java.io.*;
public class BinaryWriter {
    public static void main(String[] args) {
        try {
            FileOutputStream f = new FileOutputStream("newfile.bin");
            DataOutputStream output = new DataOutputStream(f);
            output.writeInt(114514);
            output.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }

    }

}
