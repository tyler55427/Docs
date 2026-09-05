package homework;


public class Point<T>{
    private T x,y;
    public Point(){

    }
    public Point(T x,T y){
        this.x = x;
        this.y = y;
    }
    public void setX(T x){
        this.x = x;
    }
    public void setY(T y){
        this.y = y;
    }
    public T getX(){
        return x;
    }
    public T getY(){
        return y;
    }
    public void translate(T x,T y){
        this.x = x;
        this.y = y;
    }
    public static void main(String[] args) {
        Point<Integer> point =new Point<Integer>(3,4);
        System.out.println("The begin: (" + point.getX() + "," + point.getY() + ")");
        point.translate(7, 8);
        System.out.println("The end: (" + point.getX() + "," + point.getY() + ")");
    }
}
