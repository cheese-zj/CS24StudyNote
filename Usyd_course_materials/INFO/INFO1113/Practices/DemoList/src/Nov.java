import java.util.ArrayList;
import java.util.List;

public class Nov {
    public static void addNumbersToList(List<? super Double> list){

        Number a = new Integer(10);
        list.add(Double.parseDouble("1203.012"));

    }
    public static void main(String[] args){
        List<Object> objects = new ArrayList<>();
        List<Number> numbers = new ArrayList<>();
        addNumbersToList(objects);
        addNumbersToList(numbers);
        System.out.println(objects.toString());
        System.out.println(numbers.toString());
    }
}
