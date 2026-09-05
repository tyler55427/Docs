package MyLearn;

import java.util.ArrayList;

public class ArrayList_ {
    public static void main(String[] args) {
    // 集合不能存储基本类型，只能把基本数据类型转化为包装类
    // 集合存储引用类型
    // 泛型，限定数据类型<E>  类似c++的模板T
    ArrayList<String> list = new ArrayList<>();  // 后面可以省略，但要有<>
    System.out.println(list);
    // 加入数据
    list.add("zhangsan");  //boolean
    list.add(1,"zhangsan");  //boolean
    list.add("zhangsan");  //boolean
    list.add("lisi");
    list.add("lisi");
    System.out.println(list);
    // 删除指定数据，删除指引数据
    list.remove("lisi");  //boolean
    String str = list.remove(0);  //返回删除的数据，pop
    System.out.println(str);
    System.out.println(list);
    // 修改索引数据，返回被修改元素
    String str1 = list.set(0,"sansan");
    System.out.println(str1);
    System.out.println(list);
    // 查询
    String str2 = list.get(0);
    System.out.println(str2);
    // 获取长度
    for(int i=0;i<list.size();++i){
        System.out.print(i + " " + list.get(i) + " ");
    }
    }
}
