package homework;

// import MyLearn.Person;

public class My_Exception {

    public static void main(String[] args) {
        // try{
        //     Person t = new Person();
        //     t.setAge(1111);
        // }catch(RuntimeException e){

        // }finally{
        //     System.out.println("This is the FINALLY message.");
        // }
            try{
                int[] arr = {1,2,3};
                System.out.println(arr[4]);
            }catch(Exception e){
                e.printStackTrace();
            }finally{
                System.out.println("这是一个FINALLY输出");
            }
    }
}
