package MyLearn;

import java.util.Objects;

import MyLearn.myException.AgeOutOfBoundsException;
import MyLearn.myException.NameFormatException;

public class Person implements Cloneable { // 克隆
    private String name;
    private int age;
    
    // 只执行一次
    static{
        System.out.println("static代码块执行");
    }

    // 构造减少重复
    {
        System.out.println("Person被创建");
    }

    public Person() {
        // 调用有参构造，传入空参
        this(null, 0);
    }
    public Person(String name,int age){
        this.name = name;
        this.age = age;
    }
    public void setName(String name){
        if( name.length() < 3 | name.length() > 5){
            throw new NameFormatException("格式有误，应该为3-5");
        }
        this.name = name;
    }
    public void setAge(int age){
        if(age < 0 || age > 100){
            throw new AgeOutOfBoundsException("格式有误，应该为0-100");
        }
        else{
            this.age = age;
        }
    }
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }
    public void speak(){
        System.out.println("name = " + name + "  " + "age = " + age);
    }


    @Override 
    public boolean equals(Object obj){ // 传入对象为 终极父类
        if(this == obj) return true; // 是否是同一个对象
        if(obj == null) return false; // 对象是否为空
        if(!(obj instanceof Person)) return false; // 对象是否是相同类型

        Person temp = (Person) obj;
        return getAge() == temp.getAge() && 
                getName() == temp.getName();

    }

    @Override
    public String toString(){
        return "Person:\n" + "名字：" + name
            +  "\n年龄：" + age;
    }

    @Override
    public Object clone()throws CloneNotSupportedException{
        return super.clone(); 
    }

    @Override
    public int hashCode(){
        // hash是可变参数
        // 这种方法是空指针安全
        return Objects.hash(name,age);
    }
}
