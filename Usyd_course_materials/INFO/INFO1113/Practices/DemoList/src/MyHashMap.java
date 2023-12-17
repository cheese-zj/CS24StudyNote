import java.util.ArrayList;


public class MyHashMap<K,V extends Number> {
    private ArrayList<K> keys = new ArrayList<>();
    private ArrayList<V> values = new ArrayList<>();
    ArrayList<Object[]> hash;

    public MyHashMap(){
        this.hash = new ArrayList<>();
    }

    public ArrayList<K> keyset(){
        return keys;
    }

    public void put(K key,V value){

        for (Object[] ref : hash){
            if (ref[0] == key){
                ref[1] = value;
                break;
            }
        }

        Object[] reflect = {key, value};
        hash.add(reflect);
    }

    public Object get(K key){
        for (Object[] ref : hash){
            if (ref[0].equals(key)){
                return ref[1];
            }
        }
        return null;
    }

    public static void main(String[] args){
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put("HEY",10);
        System.out.println(myHashMap.get("HEY"));
    }

}

