package homework;

import java.util.Arrays;
import java.util.Comparator;

public class Outer {
    public String[] array;
    public class Inner implements Comparator<String>{
        @Override
        public int compare(String o1,String o2) {
            return o2.compareTo(o1);
        }
    }
}


class TestSort {
    public static void main(String[] args) {
        //Outer.Inner oi = new Outer().new Inner();
           Outer outer = new Outer();
           System.out.println("-----------");
           outer.array = new String[] {"abc","as","ewqoriy","zxcvbv","abcdf"};
           for (String s : outer.array) {  
               System.out.print(s + " ");  
           }  
           System.out.println();
           Arrays.sort(outer.array, outer.new Inner());  
           System.out.println("-----------");
           for (String s : outer.array) {  
               System.out.print(s + " ");  
           }
       }
}