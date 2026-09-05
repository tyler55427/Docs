package MyLearn.Example;

import java.util.Arrays;
import java.util.Comparator;

public class Circle implements Comparable<Circle>{
    private double r;
    public Circle(){

    }
    public Circle(double radius){
        r = radius;
    }
    public double getPerimeter(){
        return 2 * r * Math.PI;
    }
    public double getArea(){
        return r * r * Math.PI;
    }
    @Override
    public int compareTo(Circle o) {
        if(r > o.r) return 1;
        else if(r < o.r) return -1;
        else return 0;
    }

    public static void main(String[] args) {
        Circle[] c = new Circle[]{
            new Circle(3.4),new Circle(2.5),new Circle(5.8)
        };
        Arrays.sort(c);
        for(var i:c){
            System.out.printf("%6.2f%n",i.getArea());
        }


        String[] s = {"this","is","java","a","string"};
        Arrays.sort(s, new Comparator<String>() {
            @Override
            public int compare(String f,String s){
                return f.length() - s.length();
            }
        });
        for(var str:s){
            System.out.print(str + " ");
        }
    }
}
