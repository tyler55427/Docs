package homework;
import MyLearn.Person;
public class week1 {
    public static void main(String[] args){
        Person p = new Person();
        p.setName("ZhangSan");
        p.setAge(20);
        System.out.println("Name: " + p.getName() + "  " + "age: " + p.getAge());
        p.speak();
        System.out.println(p.toString());
        int a = 10;
        System.out.println(a);
        a = 100;
        System.out.println(a);
    }
}
