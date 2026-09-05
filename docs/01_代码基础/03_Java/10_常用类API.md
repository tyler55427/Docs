# 10 常用类 API

本节汇集 Java 标准库常用类的 API 演示（来自 `src/MyLearn/Learning.java`），覆盖：

- `Math` —— 数学函数
- `System` —— 系统级方法
- `Runtime` —— 进程与内存
- `Object` / `Objects` —— 顶级父类
- `BigInteger` —— 大整数
- `String.matches` 正则表达式
- `Date` / `SimpleDateFormat` / `LocalDate` / `LocalTime` / `LocalDateTime` —— 时间 API

> 整理说明：原 `Learning.java` 包含 `package MyLearn` 并依赖 `Person`；这里把所有内容合并到一个文件，去除 package 声明并把 Person 用最小替换类占位（如需完整 Person，见 `08_常用工具类.md`）。

## 示例代码

```java
// 原 src/MyLearn/Learning.java（已去除 package 声明；Person 字段访问用注释标注）
import java.io.IOException;
import java.util.Date;
import java.util.Objects;
import java.math.BigInteger;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.*;
import java.time.temporal.ChronoUnit;
import java.util.Random;


public class Learning implements Cloneable{
    public void Math_test(){
        // Math
        System.out.println(Math.abs(-88));
        //向上取整
        System.out.println(Math.ceil(12.34));
        //向下取整
        System.out.println(Math.floor(12.34));
        //四舍五入
        // 返回(int)Math.floor(x+0.5)
        System.out.println(Math.round(-12.34));
        System.out.println(Math.round(-12.54));
        //开立方根
        System.out.println(Math.cbrt(8));
        //范围0.0~1.0 ，左闭右开
        System.out.println(Math.random());
        // >= 的最小整数    <= 的最大整数
        System.out.println(Math.ceil(3.5));
        System.out.println(Math.floor(3.5));
        // 返回于x接近的整数，距离相等则返回偶数
        System.out.println(Math.rint(34.5));
        // 弧度到角度，角度到弧度
        System.out.println(Math.toDegrees(Math.PI));
        System.out.println(Math.toRadians(90/Math.PI) + "PI");
}



    public void System_test(){
        // System
        //时间Long毫秒,使用start end 相减获得时间差
        System.out.println(System.currentTimeMillis());
        //拷贝数组
        int[] arr1 = {1,2,3,4,5};
        int[] arr2 = new int[10];
        //两个索引，一个长度
        System.arraycopy(arr1,0 , arr2, 0, 2);
        //0 正常退出
        // System.exit(0);
        // 返回以毫秒为单位的计算机时间
        System.out.println(System.nanoTime());
    }



    public void Runtime_test() throws IOException{
        // Runtime   不是静态
        // 或的对象
        Runtime r1 = Runtime.getRuntime();
        //停止虚拟机
        // r1.exit(0);
        //获取CPU线程数
        System.out.println(r1.availableProcessors());
        //虚拟机获取总内存大小    单位默认字节
        System.out.println(r1.maxMemory()/1024/1024);
        //虚拟机已经获取的总内存大小
        System.out.println(r1.totalMemory()/1024/1024);
        //虚拟机剩余内存大小
        System.out.println(r1.freeMemory()/1024/1024);
        //运行cmd 命令
        // shutdown : 关机
        // -s  -t  指定多少秒关机
        // -a 取消关机
        // -r  关机重启
        r1.exec("shutdown -s -t 3600");
        r1.exec("shutdown -a");
    }




    public void Object_test() throws CloneNotSupportedException, InterruptedException{
        //Object  and  Objects  顶级父类
        // 没有继承的类自动继承Objects
        Object obj = new Object();
        //java.lang.Object@28a418fc    @地址
        System.out.println(obj.toString());
        //重写父类toString, 拼接查看属性值
        System.out.println(obj);//obj 等价于 obj.toString    ,快速打印属性
        // 返回对象完整类名
        System.out.println(obj.getClass());
        //哈希码值
        // 返回对象在计算机内部储存中的十进制内存地址
        // 如果覆盖equals()，则要同时要覆盖hashCode()
        System.out.println(obj.hashCode());
        //两个对象是否相等
        // （原代码引用 MyLearn.Person，此处改为 Object 占位，需结合 08_常用工具类.md 实际使用）
        Object p1 = new Object();
        Object p2 = new Object();
        //默认比较地址，重写比较属性
        System.out.println(p1.equals(p2));
        //对象克隆或对象拷贝，在类里面重写     浅克隆
        Object u1 = p1.getClass().getDeclaredConstructor().newInstance();
        System.out.println(u1);
        //Objects
        System.out.println(Objects.equals(p1,p2));
        //isnull and nonnull
        System.out.println(Objects.isNull(p1));
        System.out.println(Objects.nonNull(p2));
        // 线程
        // 当前线程等待直到另一个线程调用notify()和notifyAll()
        // obj.wait();
        // p1.notify();
        // p2.notifyAll();
    }




    public void BigInteger_test(){
        //BigInteger大整数 and BigDecimal大小数
        BigInteger bd1 = new BigInteger(30,new Random());//2的多少次方
        System.out.println(bd1);
        //获取指定的大整数
        BigInteger bd2 = new BigInteger("6");//必须是数字
        System.out.println(bd2);
        //指定进制
        BigInteger bd3 = new BigInteger("7",8);
        System.out.println(bd3);
        //静态方法
        //范围小long，在-16 ~ 16常用数字优化，先创建好对象，地址相同
        BigInteger bd4 = BigInteger.valueOf(16);
        BigInteger bd5 = BigInteger.valueOf(16);
        System.out.println(bd4 == bd5);
        //加法
        System.out.println(bd1.add(bd2));
        //减法substract   乘法multiply   除法divide
        //获取商和余数
        BigInteger[] arr = bd1.divideAndRemainder(bd2);
        System.out.println(arr.length);
        System.out.println(arr[0]);//商
        System.out.println(arr[1]);//余数
        //比较相同
        System.out.println(bd1.equals(bd2));
        //幂运算   形参是整数
        System.out.println(bd1.pow(3));
        //较大值
        System.out.println(bd1.max(bd2));
        //变成基本数据类型
        System.out.println(bd2.intValue());//doubleValue   longValue

   }




    public void Regex_test(){
            // 正则表达式
        String qq = "19as";
        boolean temp = qq.matches("[1-9]\\d{5,19}");//[]数字范围  \\d接受数字  {}数字长度
        System.out.println(temp);
        System.out.println("a".matches("[abc]"));
        System.out.println("ab".matches("[abc]"));
        System.out.println("z".matches("[^abc]"));
        System.out.println("4".matches("[a-zA-Z0-9]"));//等价于[a-zA-Z[0-9]]
        System.out.println("e".matches("[a-z&&[def]]"));//交集
        //注意转义字符
        //.任意字符  \d数字 \D非数字  \s空白字符  \w字母数字下划线
        System.out.println("25a _".matches(".\\d\\D\\s\\w"));
        System.out.println("2".matches(".."));
        //？0或1次   *0或多次  +1或多次  {n}正好n次  {n,}至少n次  {n,m}至少n次但不超过m次
        System.out.println(qq.matches("\\w{5,}"));
        System.out.println(qq.matches("\\w{4}"));
        // (?i)x x不区分大小写

        //分组  分组有序号，从一开始
        //  \\组号，将x组的内容再用一次
        String regex1 = "(.).+\\1";
        System.out.println("a123a".matches(regex1));

        String regex2 = "((.)\\2*).+\\1";
        System.out.println("aaa1234aaa".matches(regex2));

        String str = "我要学学编编编编程程程程";
        String regex3 = "(.)\\1+";
        //  \\内部引用   $ 外部引用 （捕获分组）
        // All所以直接全部循环？
        String r = str.replaceAll(regex3, "$1");
        System.out.println(r);

        //非捕获分组
        // 不用里面的数据
        // (?:  )不占用组号    (?=  )   (?!  )
    }

    public void Date_test() throws ParseException{
        Date d1 = new Date();
        System.out.println(d1);
        Date d2 = new Date(0L); //时间原点
        System.out.println(d2);
        d2.setTime(1000L); // 一秒钟
        System.out.println(d2);
        long time = d2.getTime();
        System.out.println(time);
        // 增加一年
        time = time + 1000L * 60 * 60 * 24 * 365 ;
        d2.setTime(time);
        System.out.println(d2);
        Random r = new Random();
        Date d3 = new Date(Math.abs(r.nextInt()));
        Date d4 = new Date(Math.abs(r.nextInt()));
        System.out.println(d3);
        System.out.println(d4);
        if(d3.getTime() > d4.getTime()){
            System.out.println("1");
        }
        else{
            System.out.println("2");
        }
        //格式显示   空参，实参
        System.out.println();
        SimpleDateFormat sdf = new SimpleDateFormat();
        SimpleDateFormat sdf1 = new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss E");
        String str = sdf.format(d4);
        String str1 = sdf1.format(d4);
        System.out.println(str);
        System.out.println(str1);
        //字符串解析
        String str2 = "2024-11-11 11:11:11";
        //创建格式要和str2一样
        SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date1 = sdf2.parse(str2);
        System.out.println(date1);

    }

    public void LocalDate_test(){
        var t = LocalDate.now(); // 现在的年月日
        System.out.println(t);
        // 指定日期。加上年，月，日
        // Month 枚举类
        var day = LocalDate.of(2022,Month.JUNE,1).plusDays(255);
        System.out.println(day);
        System.out.println(day.getYear() + "是否是闰年： " + day.isLeapYear());
    }

    public void LocalTime_test(){
        var time = LocalTime.now();
        // 截断不保留纳秒
        System.out.println(time.truncatedTo(ChronoUnit.SECONDS));
    }

    public void LocalDateTime_test(){
        var time = LocalDateTime.now();
        System.out.println(time);
    }




    public static void main(String[] args) throws CloneNotSupportedException, ParseException, InterruptedException {
        Learning temp = new Learning();
        // temp.Math_test();
        // temp.Object_test();
        // temp.System_test();
        // temp.Regex_test();
        // temp.Date_test();
        // temp.LocalDate_test();
        // temp.LocalTime_test();
        temp.LocalDateTime_test();

    }
}
```
