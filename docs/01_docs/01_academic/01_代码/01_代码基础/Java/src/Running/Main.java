package Running;

import java.math.BigInteger;
// import java.util.Scanner;

// import MyLearn.class_Tool.ArrayUtil;



public class Main{  
    public static final int DAYS_PER_WEEK = 7;// 定义常量

    //自定义函数必须要加上static ，main中的变量时静态变量，赋值必须也是静态方法
    public static int add(int num1, int num2) {  
        int sum = num1 + num2;  
        return sum;  
    }  

    public static void test(){
        double aa =23.43;
        double bb = 3.2;
        // java支持小数除法
        System.out.println(aa%bb);
    }

    public static BigInteger f(long n){
        BigInteger result = BigInteger.ONE;// 大整数常量 1 
        for (long i=1;i<=n;++i){
            result = result.multiply(new BigInteger(i + ""));
        }
        return result;
    }
    public static double test__(double...a){
        double sum = 0;
        for(var i : a){
            sum += i*i;
        }
        return Math.sqrt(sum);
    }

    public static void test(int x,int y){
//         Scanner input = new Scanner(System.in);
        // int a = input.nextInt();
        // double b = input.nextDouble();
        // String str;
        // str = input.next();
        // str = input.nextLine();
        // System.out.println(str);
        // System.out.println(a);
        // System.out.println(b);
    }


    public static void main(String[] args){ 
        // Scanner input = new Scanner(System.in);
        System.out.println(test__(3, 4, 5));
        // ArrayIndexOutOfBoundsException
    } 
}