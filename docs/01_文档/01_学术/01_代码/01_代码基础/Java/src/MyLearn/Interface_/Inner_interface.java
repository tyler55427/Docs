package MyLearn.Interface_;

public interface Inner_interface {
    public static final int a = 100;
    public abstract void test();
    public default void test1(){
        System.out.println("Interface test ");
    }
}