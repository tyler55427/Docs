package Running;

import java.net.InetAddress;

public class internet {
    public static void test()
    {
        String hostname = "www.bilibili.com";
        try{
            InetAddress[] addresses = InetAddress.getAllByName(hostname);
            for(InetAddress address : addresses){
                System.out.println(address);
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args)
    {
        test();
    }
}
