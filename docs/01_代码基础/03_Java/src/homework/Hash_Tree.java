package homework;

import java.util.HashSet;
import java.util.Random;
import java.util.TreeSet;

public class Hash_Tree {
    public static void main(String[] args) {
        Random r = new Random();
        HashSet<Integer> h = new HashSet<>(20);
        TreeSet<Integer> t = new TreeSet<>();
        for(int i=0;i<20;i++){
            int temp = r.nextInt(100);
            h.add(temp);
            t.add(temp);
        }
        for(var ht:h){
            System.out.print(ht + " ");
        }
        System.out.println();
        for(var tt:t){
            System.out.print(tt + " ");
        }
        // HashSet 是无序的
        // TreeSet 是有序的

    }
}
