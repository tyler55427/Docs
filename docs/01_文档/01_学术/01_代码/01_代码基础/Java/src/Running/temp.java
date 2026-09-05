package Running;


public class temp implements Runnable{
    public void run()
    {
        for (int i = 0; i < 100; i++)
        {
            System.out.println(Thread.currentThread().getName() + " = " + i);
            try
            {
                Thread.sleep((int) (Math.random() * 100));
            }
            catch (Exception e)
            {
                System.out.println("Error: " + e);
            }
        }
    }


    public static void test1()
    {
        temp tt = new temp();
        Thread t1 = new Thread(tt, "A");
        Thread t2 = new Thread(tt, "B");
        t1.start();
        t2.start();
    }

    public static void test2()
    {
        // 主线程
        var t = Thread.currentThread();
        System.out.println(t);
        System.out.println(t.getName());
        t.setName("MyThread");
        System.out.println(t);
    }
    public static void main(String[] args) {
    }
}
