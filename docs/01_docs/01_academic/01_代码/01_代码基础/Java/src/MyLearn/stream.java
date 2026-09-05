package MyLearn;

import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

public class stream {
    public static long fibonacci(long n){
        if( n ==1 || n==2) return 1;
        else return fibonacci(n-1) + fibonacci(n-2);
    }
    public static void test(){
        Stream<Integer> stream = Stream.of(100,200,300);
        String[] names = {"dflk","fasd","fas"};
        // 直接用of创建顺序流
        Stream<String> stream2 = Stream.of(names);
        // 使用Arrays的stream创建顺序流
        Stream<String> stream3 = Arrays.stream(names);
    }
    public static void concat_test(){
        var s1 = Stream.of("北京","上海");
        var s2 = Stream.of("London","Pairs");
        Stream.concat(s1,s2).sorted().forEach(System.out::println);
    }

    public static void sort_test(){
        String[] words = {"this","is","a","long","string"};
        Stream<String> longFirst = Stream.of(words).sorted(
            Comparator.comparing(String::length).reversed());
        longFirst.forEach(System.out::println);
    }

    public static void limit_and_filter_test(){
        Stream<Double> r = Stream.generate(Math::random).limit(10);
        r.forEach(System.out::println);

        List<String> ww = List.of("this","is","a","long","string");
        Stream<String> lws = ww.stream().filter(w->w.length() > 5 );
        lws.forEach(System.out::println);
    }

    public static void stream_cast(){
        // 返回一个具有相同顺序，不包含重复元素的
        Stream<String> uW = Stream.of("one","two","three","one").distinct();
        uW.forEach(System.out::println);

        
        Stream<String> uw = Stream.of("one","two","three","one").distinct();
        // 返回最大值
        Optional<String> largest = uw.max(String::compareToIgnoreCase);
        System.out.println("Largest: " + largest.orElse(""));
    }

    public static void fibonacci_test(){

        // 斐波那契数列

        List<Integer> numbers = List.of(10,20,30,40,50,60);
        Instant start = Instant.now();
        numbers.parallelStream().map((input) -> fibonacci(input))
            .forEach(System.out::println);
        Instant end = Instant.now();
        System.out.println("并行："+Duration.between(start, end).toMillis());
        start = Instant.now();
        numbers.stream().map((input)->fibonacci(input))
            .forEach(System.out::println);
        end = Instant.now();
        System.out.println("顺序：" + Duration.between(start, end).toMillis());

    }
    public static void main(String[] args) {
        stream_cast();
    }
}
