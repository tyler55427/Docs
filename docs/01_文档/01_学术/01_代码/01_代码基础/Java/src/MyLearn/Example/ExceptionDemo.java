package MyLearn.Example;

import java.util.Scanner;

import MyLearn.Person;
import MyLearn.myException.AgeOutOfBoundsException;
import MyLearn.myException.NameFormatException;

public class ExceptionDemo {


        public static void class_test(){
        Person p1 = new Person();
        try{
            p1.setAge(123);
        }catch(RuntimeException e){
            System.out.println("年龄不对哦");
        }
        }


        public static void test_trycatch(){
            int[] arr = {1,2,3,4,5};
        // out of range
        try{
            System.out.println(arr[10]);
            //产生错误
            //new ArratIndexOutOfBoundsException()
            //与catch()对比，相同则捕获，并执行代码
            //继续执行
        }catch(ArrayIndexOutOfBoundsException e){
            // System.out.println(e.getMessage());
            // System.out.println(e.toString());
            e.printStackTrace();
            System.out.println("out of range");
        }

        System.out.println("1111111111111111");
        }


        public static int getMax(int[] arr)throws NullPointerException,ArrayIndexOutOfBoundsException{
            //调用本方法可能出现的异常
            //运行异常可以省略
            if(arr == null){
                // 手动创建对象
                throw new NullPointerException();
            }

            if(arr.length == 0){
                throw new ArrayIndexOutOfBoundsException();
            }

            int max = arr[0];
            for(int i=1;i<arr.length;++i){
                if(arr[i]>max) max = arr[i];
            }
            return max;
        }


        public static void arr_test(){
        int[] arr1 = null;//第一种
        int[] arr2 = new int[0];//第二种
        try{
            System.out.println(getMax(arr1));
            System.out.println(getMax(arr2));
        }catch(NullPointerException e){
            System.out.println("空指针");
        }catch(ArrayIndexOutOfBoundsException e){
            System.out.println("数组越界");
        }
        }


        public static void loopInput(){
            try (Scanner input = new Scanner(System.in)) {
                Person p = new Person();
                while(true){
                    try{
                        System.out.println("Please input the name");
                        String name = input.nextLine();
                        p.setName(name);
                        System.out.println("Please input the age");
                        String ageStr = input.nextLine();
                        int age = Integer.parseInt(ageStr);
                        p.setAge(age);
                        break;
                    }catch(NumberFormatException e){
                       e.printStackTrace();
                    }catch(NameFormatException e){
                        e.printStackTrace();
                    }catch(AgeOutOfBoundsException e){
                        e.printStackTrace();
                    }
                }
                System.out.println(p);
            }
        }

        public static void myDef_test(){

        }
    public static void main(String[] args) {
        loopInput();
    }
}
