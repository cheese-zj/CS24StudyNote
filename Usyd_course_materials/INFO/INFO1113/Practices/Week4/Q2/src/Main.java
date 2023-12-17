import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.print("Please input a string: ");
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine().toLowerCase().replaceAll(" ", "");
        HashMap<Character, Integer> charCount = new HashMap<>();
        for (char i : word.toCharArray()){
            if (!charCount.containsKey(i)){
                charCount.put(i,1);
            } else {
                charCount.put(i,charCount.get(i)+1);
            }
        }
        System.out.println(charCount.toString());
    }
}