package MyLearn;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Random;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class lambda {
    // 定义函数式接口，只要接口有一个抽象方法
    @FunctionalInterface
    interface Converter<F,T>{
        T convert(F from);
    }

    @FunctionalInterface
    interface Calculator{
        public abstract double calculate(double a,double b);
        public default double add(double a,double b){
            return a+b;
        }
        public default double subtract(double a,double b){
            return a-b;
        }
    }

    public static void test1(){
        String[] ss = {"this","is","a","javastring"};
        Arrays.sort(ss, new Comparator<String>() {
            @Override
            public int compare(String a,String b){
                return a.length()-b.length();
            }
        });
        
        // 使用匿名类创建一个类
        // a，b的类型可以不写，可以自动推导
        Arrays.sort(ss,(a,b)->{
            return a.length()-b.length();
        });
        for(var s:ss){
            System.out.println(s+" ");
        }
}
    public static void test2(){
        // ()->{
        // for(int i=0;i<10;i++)
        //     System.out.println(i);
        // }
        Converter<String,Integer> converter = (from) -> Integer.valueOf(from);
        Integer converted = converter.convert("234");
        System.out.println(converted);
    }

    public static void Consumer_test(){
        // 重写reverse，参数是input，指针花括号是抽象函数的具体实现
        Consumer <String> reverse = (input) ->{
            String result = new StringBuilder(input).reverse().toString();
            System.out.println(result);
        };
        reverse.accept("asdfghjk");

        // 有些方法是Consumer<T>类型，可以为它传递lambda表达式
        // default void forEach(Consumer<? super T> action)
        var myList = List.of("one","two","three");
        myList.forEach((input)->System.out.println(input));
        // 使用方法引用
        myList.forEach(System.out::println);
    }

    public static void Supplier_test(){
        Supplier<Integer> oneDigitRandom = ()->{
            Random random = new Random();
            return random.nextInt(10);
        };
        for(int i=0;i<5;i++){
            System.out.println(oneDigitRandom.get());
        }
    }

    public static void Predicate_test(){
        Predicate<String> numbersOnly = (input)->{
            for(int i=0;i<input.length();i++){
                char c = input.charAt(i);
                if("0123456789".indexOf(c) == -1 ){
                    return false;
                }
            }
            return true;
        };
        System.out.println(numbersOnly.test("12345"));
        System.out.println(numbersOnly.test("100a"));
    }

    public static void Function_test(){
        Function<Integer,Double> milesToKms = (input) -> {
            return 1.6*input;
        };
        int miles = 3;
        double kms = milesToKms.apply(miles);
        System.out.println(kms);
    }

    public static void BiFuntion_test(){
        // 直接返回值的可以简化的写，当作函数使用
        BiFunction<Double,Double,Double> area = (width,length) -> width*length;
        double width = 7.0F;
        double length = 10.0F;
        System.out.println(area.apply(width, length));
    }


    public static void methodLink(){

        // 构造方法的引用
        // 类名::new  数组::new
        // List<String> names = Arrays.asList("salkdf","dsfa");
        // Stream <Person> stream = names.stream().map(Person::new);

        // 正常返回的是Object类型
        // Object[] Persons = stream.toArray();
        // 使用特殊方法使返回的是Person类型
        // Person[] persons = stream.toArray(Person[]::new);
    }

    public static void SelfTest(){
        // First
        Calculator c = new Calculator() {
            @Override
            public
            double calculate(double a,double b){
                return (this.add(a,b)*this.add(a,b) + this.subtract(a,b)*this.subtract(a,b))/2;
            }
        };
        System.out.println(c.calculate(4, 3));

        // Second
        Calculator aa = new Calculator() {
            @Override
            public double calculate(double a,double b){
                return 0;
            }
        };
        Calculator bbCalculator = (a,b) -> (aa.add(a,b)*aa.add(a,b) + aa.subtract(a,b)*aa.subtract(a,b))/2;
        System.out.println(bbCalculator.calculate(5, 12));
    }
    public static void main(String[] args) {
    }
}