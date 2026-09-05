package MyLearn.class_Tool;

public class ArrayUtil {
    private ArrayUtil(){}

    public static String printArr(int[] arr){
        StringBuilder temp = new StringBuilder();
        temp.append("[");
        for(int i=0;i<arr.length;i++){
            if( i == arr.length -1){
                temp.append(arr[i]);
            }
            else{
                temp.append(arr[i]).append(",");
            }
        }
        temp.append("]");
        return temp.toString();
    }

    public static double getAverage(double[] arr){
        double sum = 0;
        for(int i=0;i<arr.length;i++){
            sum += arr[i];
        }
        return sum/arr.length;
    }
}
