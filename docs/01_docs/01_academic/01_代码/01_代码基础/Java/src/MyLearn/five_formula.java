package MyLearn;

import java.util.Arrays;
// import java.util.Comparator;

public class five_formula {
    public static void main(String[] args) {
        Person p1 = new Person ("zhangsan",18);
        Person p2 = new Person ("lisi",19);
        Person p3 = new Person ("huangwu",19);
        Person[] arr = {p1,p2,p3};
    
    // Arrays.sort(arr,new Comparator<Person>(){
    //     @Override
    //     public int compare(Person o1,Person o2){
    //         double temp = o1.getAge() - o2.getAge();
    //         temp = temp == 0?o1.getName().compareTo(o2.getName()):temp;
    //         if(temp > 0){
    //             return 1;
    //         }
    //         else if( temp < 0){
    //             return -1;
    //         }
    //         else 
    //             return 0;
    //     }
    // });

    // lambda 表达式
    Arrays.sort(arr,(o1,o2) -> {
            double temp = o1.getAge() - o2.getAge();
            temp = temp == 0?o1.getName().compareTo(o2.getName()):temp;
            if(temp > 0){
                return 1;
            }
            else if( temp < 0){
                return -1;
            }
            else 
                return 0;
        
    });



    System.out.println(Arrays.toString(arr));
}
}
