interface ShowAd{
    public void showAd();
    public static void main(String[] args){
        //nothing;
    }
}

class App{
    private String name;


    public App(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }
}

class iPhoneApp extends App implements ShowAd{

    public iPhoneApp(){
        super("iPhone App");
    }
    public void showAd(){
        System.out.println("Showing Ad");
    }
}

public class MyApp{
    public static void main(String[] params){
        boolean paidVersion = false;
        iPhoneApp i = new iPhoneApp();
        System.out.println(i.getName());
        if(!paidVersion)
            i.showAd();
    }
}