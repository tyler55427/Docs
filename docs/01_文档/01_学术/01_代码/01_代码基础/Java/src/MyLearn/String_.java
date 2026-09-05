package MyLearn;

public class String_ {
    public static void main(String[] args) {
        String ss = "one little,two little,three little";
        String[] str = ss.split("[,.]");
        for(var s:str){
            System.out.println(s);
        }


        String joined = String.join("\\","C:","javastudy","com");
        System.out.println(joined);
        String[] seasons = {"spring","summer","autumn","winter"};
        String temp = String.join("-",seasons);
        System.out.println(temp);


    }
}
